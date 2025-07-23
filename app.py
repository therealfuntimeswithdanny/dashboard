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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
