# Keylogger Tool 

This Python-based command-line interface (CLI) tool is meticulously designed to log keystrokes, serving exclusively for **ethical security research, educational purposes, and controlled simulations of malware behavior.**


## ✨ Features

* **Author Banners:** Clear on-screen and log banners emphasizing ethical use and developer attribution.

* **Keystroke Logging:** Captures and logs all pressed keys (both regular characters and special keys).

* **Session Management:** Creates unique log files for each session, organized within a dedicated directory (`keylogger_logs`).

* **Directory & Log Management:** Automatically creates the `keylogger_logs` directory if it doesn't exist.

* **User Notifications:** Provides clear prompts for starting and stopping the logging process.

* **Graceful Exit (ESC Key):** Stops logging and saves the log file upon detection of the `ESC` key.

* **Graceful Exit (Ctrl+C):** Handles `KeyboardInterrupt` (Ctrl+C) gracefully, ensuring logs are saved and providing a clean exit message.

* **Detailed Logging:** Logs timestamps for each keystroke, aiding in analysis.

* **Error Handling:** Basic error handling for unexpected issues during execution.

## 📦 Dependencies

This project requires the `pynput` library to monitor keyboard input.

### Installation

It is highly recommended to use a Python [virtual environment](https://docs.python.org/3/library/venv.html) to manage dependencies and avoid conflicts with your system's Python packages.

1.  **Navigate to your project directory:**

    ```bash
    cd your_project_directory
    ```

    (Replace `your_project_directory` with the actual path to your project folder, e.g., `~/Desktop/project`)

2. **Install the required library:**

    ```bash
    pip install pynput
    ```

## 🚀 How to Run

Once the dependencies are installed and your virtual environment is active, you can run the script:

```bash
python keylogger_tool.py
```

## 💡 Usage

  * **Execute the script from your terminal.**

  * **A banner will display, showing the log file path and instructions.**

  * **The keylogger will start monitoring keystrokes.**

  * **To stop the logging session, press the ESC key.**

  * **Alternatively, you can press Ctrl+C in the terminal to interrupt the logging gracefully.**

The tool will then confirm that the session has ended and the log file is saved.
## 📁 Output Logs Example

The logs are saved in the keylogger_logs directory with filenames like session_YYYYMMDD_HHMMSS.log. An example of the log content:

2025-05-21 18:45:10 | Key Pressed: h
2025-05-21 18:45:11 | Key Pressed: e
2025-05-21 18:45:12 | Key Pressed: l
2025-05-21 18:45:13 | Key Pressed: l
2025-05-21 18:45:14 | Key Pressed: o
2025-05-21 18:45:15 | Special Key: Key.space
2025-05-21 18:45:16 | Key Pressed: w
2025-05-21 18:45:17 | Key Pressed: o
2025-05-21 18:45:18 | Key Pressed: r
2025-05-21 18:45:19 | Key Pressed: l
2025-05-21 18:45:20 | Key Pressed: d

## 🧪 Intended Use Cases (Ethical)

  * **Simulate malware behavior:** For defensive research and understanding how keyloggers operate.

  * **Train anomaly-based EDR/AV systems:** By generating realistic input data for security tool development.

  * **Study keystroke forensics:** Analyze logged keystrokes to understand user activity patterns (in authorized contexts).

  * **Educate others on the danger of keyloggers:** Serve as a practical example to raise awareness about input capture threats.

## 🛡️ Security Tip: Detect Keyloggers

To detect keyloggers like this (and more sophisticated ones):

  **Monitor specific libraries:** Look for processes that use pynput, pyxhook (Linux), or Windows API hooks related to input capture.

  **Abnormal file creations:** Be vigilant about unusual .log files or other data files appearing in suspicious directories.

  **Behavior-based EDR tools:** Utilize Endpoint Detection and Response (EDR) solutions that can detect unauthorized input capture or suspicious process behavior.

  **Network Activity:** Advanced keyloggers might try to exfiltrate data; monitor unusual outbound network connections.

## 🧑‍💻 Author

Developed by Yuva Prasath

