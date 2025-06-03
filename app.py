import os
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from monitor import RadiationMonitor # Import RadiationMonitor

app = Flask(__name__)
socketio = SocketIO(app)

radiation_data = [] # Keep radiation_data in app.py

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    return jsonify(radiation_data)

@socketio.on("connect")
def handle_connect():
    print("Client connected. Starting radiation monitoring...")
    # Pass socketio and radiation_data to the monitor method
    socketio.start_background_task(target=monitor_instance.monitor, socketio=socketio, radiation_data=radiation_data)

# Fetch threshold from environment variable, default to 50
threshold = int(os.environ.get("RADIATION_THRESHOLD", 50))
monitor_instance = RadiationMonitor(threshold=threshold) # Rename to monitor_instance

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
