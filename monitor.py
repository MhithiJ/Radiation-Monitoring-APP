import time
import random
import os
from datetime import datetime

class RadiationMonitor:
    def __init__(self, threshold=50):
        self.threshold = threshold
        self.log_file = "radiation_log.txt"  # Add log_file attribute

    def get_radiation_levels(self):
        beta_level = round(random.uniform(0, 100), 2)
        gamma_level = round(random.uniform(0, 100), 2)
        return beta_level, gamma_level

    def log_radiation_levels(self, beta_level, gamma_level):
        with open(self.log_file, "a") as log_file:  # Use self.log_file
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - Beta Level: {beta_level:.2f} µSv/h, Gamma Level: {gamma_level:.2f} µSv/h\n")

    def monitor(self, socketio, radiation_data):
        """
        Monitors radiation levels, logs them, emits them via SocketIO,
        and checks against the threshold.
        """
        print("Starting Radiation Monitoring (from monitor.py)...")
        while True:
            beta_level, gamma_level = self.get_radiation_levels()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Append to the shared radiation_data list
            radiation_data.append({"time": timestamp, "beta": beta_level, "gamma": gamma_level})
            if len(radiation_data) > 100:
                radiation_data.pop(0)

            # Emit data through the provided socketio instance
            socketio.emit("new_data", {"time": timestamp, "beta": beta_level, "gamma": gamma_level})

            # Log levels
            self.log_radiation_levels(beta_level, gamma_level)

            # Check threshold
            if beta_level > self.threshold or gamma_level > self.threshold:
                print(f"WARNING: Radiation level exceeded safe threshold! Beta: {beta_level}, Gamma: {gamma_level}, Threshold: {self.threshold}")

            time.sleep(2)
