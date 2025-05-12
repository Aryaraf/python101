import psutil
import time
from datetime import datetime

def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    times = datetime.now().strftime("[%Y-%m-%d]")
    return f"{times} INFO - CPU usage {cpu}%, RAM usage: {ram}%, Disk usage: {disk}%\n"

while True:    
    log = get_stats()   
    with open ("logging.log", "a") as f:
        f.write(log)
    print(log.strip())
    time.sleep(5)