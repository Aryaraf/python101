import psutil
import time
import requests
from datetime import datetime

API_ID = "8110307750:AAFMazaZ_UQLgMMa2TnGT0C14fkaplSDzj8"
ID_CLIENT = 6252040922
url = f"https://api.telegram.org/bot{API_ID}/sendMessage"

while True:
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    if cpu > 80:
        requests.post(url, data={
            "chat_id": ID_CLIENT,
            "text": f"CPU Alert! usage: {cpu}% is higher than 80% at {time_now}"
        })
    
    print(f"[{time_now}] CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%")
    
    with open("system_log.txt", "a") as f:
        f.write(f"\n[{time_now}] \nCPU: {cpu}%  \nRAM: {ram}%  \nDisk: {disk}%")
        
    time.sleep(5)