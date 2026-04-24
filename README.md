Monitoring Service (Python + systemd)

A lightweight system monitoring utility designed for Debian 13 (Trixie). This service tracks CPU and RAM usage in real-time, logs historical data in JSONL format, and sends alerts via Telegram when system load exceeds defined thresholds.
🚀 Features

    Real-time Monitoring: Tracks total CPU load, RAM percentage, and top resource-consuming processes [cite: 2026-04-23].

    systemd Integration: Runs as a background daemon with auto-restart capabilities on Debian systems [cite: 2026-04-23].

    Automatic Logging: Stores data in system_history.jsonl with built-in log rotation (10MB limit) to prevent disk overflow [cite: 2026-04-24].

    Telegram Alerts: Sends instant notifications when CPU usage exceeds the user-defined threshold (default: 80%) [cite: 2026-04-24].

    Self-Contained: Utilizes Python virtual environments (.venv) for clean dependency management.

📁 Project Structure
Plaintext

Monitoring/
├── monitoring_cpu.py    # Main monitoring logic & systemd loop
├── config.py            # API tokens and threshold settings (Hidden via .gitignore)
├── tg_sender.py         # Telegram Bot API integration
├── system_history.jsonl # Historical log data (JSON Lines format)
├── install.sh           # Automated installation script for Debian
└── .gitignore           # Prevents secrets and venv from being pushed

🛠 Installation & Setup
1. Prerequisites

Ensure you are running a Debian-based system and have a Telegram Bot token from @BotFather.
2. Clone and Configure
Bash

git clone https://github.com/Karasy-linux/monitoring_service.git
cd monitoring_service

Create a config.py file:
Python

TOKEN = "your_telegram_bot_token"
CHAT_ID = "your_chat_id"
CPU_THRESHOLD = 80.0

3. Run the Installer

The included install.sh script automates the creation of the virtual environment and the systemd service registration.
Bash

chmod +x install.sh
./install.sh

📊 Usage

Once installed, the service starts automatically. You can manage it using standard systemctl commands:

    Check Status: sudo systemctl status sysmon

    Restart Service: sudo systemctl restart sysmon

    View Live Logs: journalctl -u sysmon.service -f

🛡 License

This project is open-source and available under the MIT License.
Tips for your GitHub profile:

    Add a Screenshot: If you have a screenshot of the Telegram alert or the system_history.jsonl data, add it to the repository and link it in the "Features" section.

    Keep secrets safe: Double-check that your git push didn't include your config.py with real tokens. Your .gitignore is now correctly placed in the root directory to prevent this [cite: 2026-04-23].