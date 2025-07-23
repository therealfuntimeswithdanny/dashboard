# Deploying Your Python Dashboard on Raspberry Pi

## Prerequisites
- Raspberry Pi running Raspberry Pi OS (or similar)
- Python 3 installed
- Internet connection

## 1. Transfer Your Project
Copy your entire `simpleserver` folder to your Raspberry Pi, e.g. using SCP:
```sh
scp -r /Users/danny/Desktop/simpleserver pi@<raspberry-pi-ip>:/home/pi/
```
Replace `<raspberry-pi-ip>` with your Pi's IP address.

## 2. Install Python and pip
Make sure Python 3 and pip are installed:
```sh
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

## 3. Set Up Virtual Environment
Navigate to your project folder:
```sh
cd ~/simpleserver
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install Dependencies
```sh
pip install flask flask-cors
```

## 5. Start the Servers
Make the script executable:
```sh
chmod +x start_servers.sh
```
Run the script:
```sh
./start_servers.sh
```

## 6. Access the Dashboard
- Find your Pi's IP address: `hostname -I`
- On any device on your network, open a browser and go to:
  - `http://<raspberry-pi-ip>:8000`

## 7. Stopping the Servers
To stop both servers, use the `kill` command shown by the script, or:
```sh
pkill -f app.py
pkill -f server.py
```

## 8. (Optional) Autostart on Boot
To run the servers automatically on boot, add the start command to your crontab:
```sh
crontab -e
```
Add this line at the end:
```
@reboot cd /home/pi/simpleserver && ./start_servers.sh
```

---
**Tip:** If you want to access your dashboard from outside your home network, you will need to set up port forwarding on your router.
