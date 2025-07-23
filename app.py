import psutil
import socket
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "dashboard_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    # Default data
    return {
        "userName": "Danny Morrisey",
        "links": [
            {"id": "1", "name": "Google", "url": "https://www.google.com"},
            {"id": "2", "name": "GitHub", "url": "https://github.com"},
            {"id": "3", "name": "Stack Overflow", "url": "https://stackoverflow.com"},
            {"id": "4", "name": "MDN Web Docs", "url": "https://developer.mozilla.org"}
        ],
        "apiKey": ""
    }

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

@app.route("/api/dashboard", methods=["GET"])
def get_dashboard():
    return jsonify(load_data())

@app.route("/api/dashboard", methods=["POST"])
def update_dashboard():
    data = request.json
    save_data(data)
    return jsonify({"status": "success"})

@app.route("/api/systeminfo", methods=["GET"])
def system_info():
    # CPU usage
    cpu = psutil.cpu_percent(interval=0.5)
    # RAM usage
    ram = psutil.virtual_memory().percent
    # Disk usage
    disk = psutil.disk_usage('/').percent
    # Uptime
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
    # IP address
    try:
        ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        ip = 'N/A'
    return jsonify({
        "cpu": round(cpu, 1),
        "ram": round(ram, 1),
        "disk": round(disk, 1),
        "uptime": uptime,
        "ip": ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
