import psutil
import time
import json
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
import config
from tg_sender import send_telegram

class SystemMonitor:
    def __init__(self, log_file="system_history.jsonl"):
        self.log_file = log_file
        self.max_bytes = 10 * 1024 * 1024  # 10 MB
        self.backup_count = 5             # save a maximum of 5 log files
        self.cpu_threshold = 80.0
        self._setup_logging()
        print(f"--- Monitoring started. Rotation: {self.max_bytes/1024/1024}MB ---")

    def _setup_logging(self):
        # setting up a rotating file handler
        handler = RotatingFileHandler(
            self.log_file, 
            maxBytes=self.max_bytes, 
            backupCount=self.backup_count,
            encoding='utf-8'
        )
        
        # setting up the logger
        self.logger = logging.getLogger("SystemMonitor")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def collect_data(self):
        # collecting CPU and RAM usage data
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        
        top_procs = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                info = proc.info 
                if info['cpu_percent'] > 1.0:
                    top_procs.append(info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
            
        top_procs.sort(key=lambda x: x['cpu_percent'], reverse=True)
    
        return {
            "timestamp": datetime.now().isoformat(),
            "cpu_total": cpu_usage,
            "ram_percent": ram.percent,
            "top_processes": top_procs[:5]
        }

    def run(self):
        try:
            while True:
                data = self.collect_data()

                if data['cpu_total'] > self.cpu_threshold:
                    if self.last_alert_time is None or \
                        (datetime.now() - self.last_alert_time).total_seconds() > 300:  # 5 minutes
                        msg = f"⚠️ CRITICAL LOAD: CPU {data['cpu_total']}%"

                        send_telegram(msg)
                        self.last_alert_time = datetime.now()

                    self.logger.info(json.dumps(data, ensure_ascii=False))
                    print(f"[{data['timestamp']}] CPU: {data['cpu_total']}% | Recorded in log")    

                # Recording JSON as a single line in the log
                self.logger.info(json.dumps(data, ensure_ascii=False))
                
                print(f"[{data['timestamp']}] CPU: {data['cpu_total']}% | Recorded in log")
                time.sleep(60)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.run()