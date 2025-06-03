import unittest
import os
from datetime import datetime
# Adjust the import path if necessary, assuming 'monitor.py' is in the parent directory
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from monitor import RadiationMonitor

class TestRadiationMonitor(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.monitor_instance = RadiationMonitor(threshold=50)
        self.test_log_file = "test_radiation_log.txt"
        # Ensure test log file does not exist before a test that creates it
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)

    def tearDown(self):
        """Clean up after test methods."""
        # Clean up the test log file if it was created
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)

    def test_get_radiation_levels(self):
        """Test the get_radiation_levels method."""
        beta, gamma = self.monitor_instance.get_radiation_levels()

        self.assertIsInstance(beta, float, "Beta level should be a float")
        self.assertIsInstance(gamma, float, "Gamma level should be a float")

        self.assertTrue(0 <= beta <= 100, "Beta level should be between 0 and 100")
        self.assertTrue(0 <= gamma <= 100, "Gamma level should be between 0 and 100")

    def test_log_radiation_levels(self):
        """Test the log_radiation_levels method for file creation and content."""
        # Override the log file for this test
        self.monitor_instance.log_file = self.test_log_file

        test_beta = 15.75
        test_gamma = 30.25
        self.monitor_instance.log_radiation_levels(test_beta, test_gamma)

        self.assertTrue(os.path.exists(self.test_log_file), "Log file should be created")

        with open(self.test_log_file, "r") as f:
            content = f.read()

        self.assertIn(f"Beta Level: {test_beta:.2f} µSv/h", content, "Log content should contain correct Beta level")
        self.assertIn(f"Gamma Level: {test_gamma:.2f} µSv/h", content, "Log content should contain correct Gamma level")

        # Check timestamp (presence and basic format)
        # Example: 2023-10-27 (this will vary, so we check for pattern)
        self.assertRegex(content, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", "Log content should contain a timestamp")

if __name__ == '__main__':
    unittest.main()
