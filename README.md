# Real-Time Radiation Monitoring Application

## Overview

This application provides a real-time dashboard to monitor Beta and Gamma radiation levels. It simulates radiation data, displays it on a web interface with a dynamic graph, and logs the data to a file. This tool is intended for demonstration and educational purposes.

## Features

- **Real-time Monitoring**: Simulates and displays Beta and Gamma radiation levels updated every few seconds.
- **Graphical Display**: Visualizes radiation levels over time on a Plotly-based interactive graph.
- **Data Logging**: Records timestamped radiation levels (Beta and Gamma) in a `radiation_log.txt` file.
- **Configurable Threshold**: Allows setting a radiation warning threshold (details on configuration below).

## Setup and Installation

### Prerequisites

- Python 3.x

### Steps

1.  **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
    *(Replace `<repository-url>` and `<repository-directory>` with the actual URL and directory name)*

2.  **Install Dependencies**:
    The project includes a `requirements.txt` file listing all necessary dependencies. Install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Start the Application**:
    ```bash
    python app.py
    ```

2.  **View the Dashboard**:
    Open your web browser and navigate to:
    ```
    http://localhost:5000
    ```
    You should see the real-time radiation monitoring dashboard.

## Configuration

The radiation warning threshold for the application can be configured using an environment variable named `RADIATION_THRESHOLD`.

-   **How to set**:
    -   On Linux/macOS:
        ```bash
        export RADIATION_THRESHOLD=75
        ```
    -   On Windows (Command Prompt):
        ```bash
        set RADIATION_THRESHOLD=75
        ```
    -   On Windows (PowerShell):
        ```bash
        $env:RADIATION_THRESHOLD="75"
        ```
-   **Default Value**: If the `RADIATION_THRESHOLD` environment variable is not set, the application will default to a threshold of `50` µSv/h.

You can change `75` to your desired threshold value. The application reads this value upon starting.

## Running Tests

This project uses Python's built-in `unittest` module for testing. To run the tests:

1.  Ensure you are in the root directory of the project.
2.  Run the following command in your terminal:

    ```bash
    python -m unittest discover -s tests
    ```
    This command will discover and run all tests within the `tests` directory.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details (if one exists).
