# Schedule-1-Cheat
This is a python script that allows you to change the value of your cash and card in Schedule 1.

It uses the pymem library to attach to the game's process and access its memory. The script monitors the cash and card values continuously, increasing them whenever they drop below the initial value.

## Features

- Attaches to a running process (Schedule I.exe).
- Resolves pointer chains to locate memory addresses for cash and card values.
- Writes the initial values to both cash and card memory locations.
- Continuously monitors for changes in cash and card values, adjusting them if they drop.
- Outputs updates to the console showing the changes in cash and card values.

## Prerequisites

Make sure to have the following installed:
- Python 3.x
- `pymem` library (`pip install pymem`)

## How It Works

1. **Process Attachment**: The script attaches to the specified game process (`Schedule I.exe`).
2. **Memory Address Resolution**: Using pointer chains, the script resolves the memory addresses of cash and card values in the game.
3. **Value Modification**: The script writes the initial value (1,000,000) to the cash and card addresses.
4. **Continuous Monitoring**: It continuously checks the cash and card values every 0.25 seconds. If either value decreases, it is restored by doubling the difference from the previous value.
5. **Error Handling**: Any issues encountered during the process are printed as errors.

![image](https://github.com/user-attachments/assets/62861417-ec7f-4c67-96e6-742795c5742f)
