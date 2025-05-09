import psutil
from datetime import datetime

while True:    
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    time = datetime.now().strftime("%Y-%m-%d")
        
    total = (f"\n[{time}] INFO - CPU usage {cpu}%, RAM usage: {ram}%, Disk usage: {disk}%")
        
    with open ("logging.log", "a") as f:
        f.write(total)
        
    print(f"[{time}] INFO - CPU usage {cpu}%, RAM usage: {ram}%, Disk usage: {disk}%")