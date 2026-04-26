🛡 License
    This project is open-source and available under the MIT License. Tips for your GitHub profile:

    Add a Screenshot: If you have a screenshot of the Telegram alert or the system_history.jsonl data, add it to the repository and link it in the "Features" section.

    Keep secrets safe: Double-check that your git push didn't include your config.py with real tokens. Your .gitignore is now correctly placed in the root directory to prevent this .


Monitoring Service (Python + systemd)

A lightweight system monitoring utility designed for Debian 13 (Trixie). This service tracks CPU and RAM usage in real-time, logs historical data in JSONL format, and sends alerts via Telegram when system load exceeds defined thresholds.
🚀 Features

    Real-time Monitoring: Tracks total CPU load, RAM percentage, and top resource-consuming processes

    systemd Integration: Runs as a background daemon with auto-restart capabilities on Debian systems.

    Automatic Logging: Stores data in system_history.jsonl with built-in log rotation (10MB limit) to prevent disk overflow .

    Telegram Alerts: Sends instant notifications when CPU usage exceeds the user-defined threshold (default: 80%) .

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

📊 Data Analyzer Module

This module is designed to process and visualize system logs collected by the monitoring utility. It leverages the Pandas library to provide high-performance analytics for large JSONL datasets.
Key Features

    Average Metrics: Automatically calculates mean CPU and RAM utilization across the entire monitoring session.

    Peak Detection: Identifies the exact moments of maximum resource consumption.

    Process Filtering: Isolates specific applications consuming more than 20% of CPU capacity at any given timestamp.

    Nested Data Support: Correctly handles complex top_processes lists nested within JSON objects using efficient lambda filtering.

Usage
Python

from analyzer import analyze_data

# Retrieve the full DataFrame and statistical metrics
df, avg_cpu, avg_ram, peak_cpu, peak_ram = analyze_data()

print(f"Peak CPU Usage: {peak_cpu}%")

Input Data Format

The analyzer expects a system_history.jsonl file where each line is a standalone JSON object:
JSON

{"timestamp": "2026-04-26T18:00:00", "cpu_total": 15.4, "ram_percent": 42.1, "top_processes": [...]}

    Pro Tip: Since you're already using Counter for your "Lonely Letters" task, you could easily add a feature to this analyzer that counts which program is the most frequent "offender" (appears most often in the heavy-load list).