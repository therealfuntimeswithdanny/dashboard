# Deploy and Update the Dashboard on Raspberry Pi (via Git)

## 1. Clone the Repository

On your Raspberry Pi, open a terminal and run:
```sh
git clone https://github.com/therealfuntimeswithdanny/dashboard.git ~/simpleserver
cd ~/simpleserver
```

## 2. Install Python and pip
```sh
sudo apt update
sudo apt install python3 python3-pip python3-venv zsh
```

## 3. Set Up Virtual Environment
```sh
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install Dependencies
```sh
pip install flask flask-cors psutil
```

## 5. Start the Servers
```sh
chmod +x start_servers.sh
zsh start_servers.sh
```

## 6. Access the Dashboard
- Find your Pi's IP address: `hostname -I`
- On any device on your network, open a browser and go to:
  - `http://<raspberry-pi-ip>:8000`

## 7. Update the Dashboard
To update to the latest version:
```sh
cd ~/simpleserver
git pull
zsh start_servers.sh
```

## 8. Troubleshooting
- If you change Python files, restart the servers:
  ```sh
  pkill -f app.py
  pkill -f server.py
  zsh start_servers.sh
  ```
- For port issues, check your router/firewall settings.
- For dependency issues, re-run `pip install flask flask-cors psutil` inside your venv.

---
For more details, see the main README.md.
