import psutil
import argparse
import json
from datetime import datetime

parser = argparse.ArgumentParser(description="System logger with alert and JSON output")
parser.add_argument('--interval', type=int, default=3, help='Interval in seconds between logs')
args = parser.parse_args()

while True:
    cpu = psutil.cpu_percent(interval=args.interval)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_msg = f"[{time}] INFO - CPU usage {cpu}%, RAM usage: {ram}%, Disk usage: {disk}%"
    log_data = {
        "timestamp": time,
        "level": "INFO",
        "cpu": cpu,
        "ram": ram,
        "disk": disk
    }

    print(log_msg)
    with open("logging.log", "a") as f:
        f.write(log_msg + "\n")

    with open("logging.json", "a") as f_json:
        f_json.write(json.dumps(log_data) + "\n")

    if cpu > 80:
        warning_msg = f"[{time}] WARNING - High CPU usage detected: {cpu}%"
        warning_data = {
            "timestamp": time,
            "level": "WARNING",
            "message": f"High CPU usage: {cpu}%"
        }

        print(warning_msg)
        with open("logging.log", "a") as f:
            f.write(warning_msg + "\n")
        with open("logging.json", "a") as f_json:
            f_json.write(json.dumps(warning_data) + "\n")
