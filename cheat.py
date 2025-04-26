import pymem
import pymem.process
import struct
import time

process_name = "Schedule I.exe"
module_name = "GameAssembly.dll"

cash_offset_from_module = 0x037976F8
cash_offsets = [0xB8, 0x10, 0x108, 0x38]

card_offset_from_module = 0x037C4798
card_offsets = [0xB8, 0x10, 0x128]

initial_value = 1_000_000.0

def resolve_pointer_chain(pm, base, offsets):
    address = pm.read_ulonglong(base)
    for offset in offsets[:-1]:
        address = pm.read_ulonglong(address + offset)
    return address + offsets[-1]

def read_float(pm, address):
    return struct.unpack("<f", pm.read_bytes(address, 4))[0]

def write_float(pm, address, value):
    pm.write_bytes(address, struct.pack("<f", value), 4)

def main():
    try:
        pm = pymem.Pymem(process_name)
        print(f"[+] Attached to process: {process_name}")

        gameassembly = pymem.process.module_from_name(pm.process_handle, module_name)
        base = gameassembly.lpBaseOfDll

        cash_addr = resolve_pointer_chain(pm, base + cash_offset_from_module, cash_offsets)
        card_addr = resolve_pointer_chain(pm, base + card_offset_from_module, card_offsets)

        write_float(pm, cash_addr, initial_value)
        write_float(pm, card_addr, initial_value)
        print(f"[+] Initial cash & card set to {initial_value:.2f}")

        last_cash = initial_value
        last_card = initial_value

        print("[*] Monitoring for changes... Press CTRL+C to stop.")

        while True:
            time.sleep(0.25)

            current_cash = read_float(pm, cash_addr)
            current_card = read_float(pm, card_addr)

            if current_cash < last_cash:
                delta = last_cash - current_cash
                new_cash = current_cash + (delta * 2)
                write_float(pm, cash_addr, new_cash)
                print(f"[+] Cash increased from {current_cash:.2f} → {new_cash:.2f}")
                last_cash = new_cash
            else:
                last_cash = current_cash

            if current_card < last_card:
                delta = last_card - current_card
                new_card = current_card + (delta * 2)
                write_float(pm, card_addr, new_card)
                print(f"[+] Card increased from {current_card:.2f} → {new_card:.2f}")
                last_card = new_card
            else:
                last_card = current_card

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    main()
