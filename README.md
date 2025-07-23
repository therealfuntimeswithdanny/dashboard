# Deploying Your Python Dashboard on Raspberry Pi

## Prerequisites
- Raspberry Pi running Raspberry Pi OS (or similar)
- Python 3 installed
- Internet connection
- SSH

## 1. Transfer Your Project
Copy your entire `simpleserver` folder to your Raspberry Pi using SCP:
```sh
scp -r /Users/danny/Desktop/simpleserver <user-name>@<raspberry-pi-ip>:~/
```
Replace `<raspberry-pi-ip>` with your Pi's IP address (e.g. `10.0.0.187` or `raspberrypi.local`).
Replace `<user-name>` with your Pi username (often `pi` or `danny`).

## 2. SSH into your Pi
```sh
ssh <user-name>@<raspberry-pi-ip>
```

## 3. Install Python and pip
Make sure Python 3 and venv are installed:
```sh
sudo apt update
sudo apt install python3 python3-pip python3-venv zsh
```

## 4. Set Up Virtual Environment
Navigate to your project folder:
```sh
cd ~/simpleserver
rm -rf .venv  # Remove any broken venv
python3 -m venv .venv
source .venv/bin/activate
```

## 5. Install Dependencies
```sh
pip install flask flask-cors
```

## 6. Start the Servers
Make the script executable:
```sh
chmod +x start_servers.sh
```
Run the script (use zsh or bash):
```sh
zsh start_servers.sh
```
Or, if you prefer bash, edit the first line of `start_servers.sh` to `#!/bin/bash` and run:
```sh
bash start_servers.sh
```

## 7. Access the Dashboard
- Find your Pi's IP address: `hostname -I`
- On any device on your network, open a browser and go to:
  - `http://<raspberry-pi-ip>:8000`

## 8. Stopping the Servers
To stop both servers, use the `kill` command shown by the script, or:
```sh
pkill -f app.py
pkill -f server.py
```

## 9. (Optional) Autostart on Boot
To run the servers automatically on boot, add the start command to your crontab:
```sh
crontab -e
```
Add this line at the end:
```
@reboot cd ~/simpleserver && zsh start_servers.sh
```

## 10. Updating Files on Your Pi
If you make changes to files on your Mac, copy only the updated files to your Raspberry Pi using `scp`:
```sh
scp /Users/danny/Desktop/simpleserver/<filename> <user-name>@<raspberry-pi-ip>:~/simpleserver/
```
Replace `<filename>`, `<user-name>`, and `<raspberry-pi-ip>` as needed.

If you update Python files, restart the servers on your Pi:
```sh
pkill -f app.py
pkill -f server.py
zsh start_servers.sh
```
Or use `bash start_servers.sh` if you switched to bash.

**Tip:** For syncing entire folders, use `rsync`:
```sh
rsync -avz /Users/danny/Desktop/simpleserver/ <user-name>@<raspberry-pi-ip>:~/simpleserver/
```

---
**Tip:** If you want to access your dashboard from outside your home network, you will need to set up port forwarding on your router.
