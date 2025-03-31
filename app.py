import time
import random
from datetime import datetime
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

radiation_data = []

class RadiationMonitor:
    def __init__(self, threshold=50):
        self.threshold = threshold

    def get_radiation_levels(self):
       
        beta_level = round(random.uniform(0, 100), 2)
        gamma_level = round(random.uniform(0, 100), 2)
        return beta_level, gamma_level

    def log_radiation_levels(self, beta_level, gamma_level):
        
        with open("radiation_log.txt", "a") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - Beta Level: {beta_level:.2f} µSv/h, Gamma Level: {gamma_level:.2f} µSv/h\n")

    def monitor(self):
       
        print("Starting Radiation Monitoring...")
        while True:
            beta_level, gamma_level = self.get_radiation_levels()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            radiation_data.append({"time": timestamp, "beta": beta_level, "gamma": gamma_level})
            if len(radiation_data) > 100:
                radiation_data.pop(0)

            socketio.emit("new_data", {"time": timestamp, "beta": beta_level, "gamma": gamma_level})
            self.log_radiation_levels(beta_level, gamma_level)

            if beta_level > self.threshold or gamma_level > self.threshold:
                print("WARNING: Radiation level exceeded safe threshold!")

            time.sleep(2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    return jsonify(radiation_data)

@socketio.on("connect")
def handle_connect():
    print("Client connected. Starting radiation monitoring...")
    socketio.start_background_task(target=monitor.monitor)

monitor = RadiationMonitor(threshold=50)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
