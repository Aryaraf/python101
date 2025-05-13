import psutil
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Simple system resources logger")
parser.add_argument('--interval', type=int, default=3, help='Interval in second between logs')
args = parser.parse_args()

while True:
    
    cpu = psutil.cpu_percent(interval=args.interval)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    total = (f"[{time}] INFO - CPU usage: {cpu}% RAM usage: {ram}% DISK usage: {disk}%")
    
    with open ("logger.log", "a") as f:
        f.write(total)
        
    print(total)