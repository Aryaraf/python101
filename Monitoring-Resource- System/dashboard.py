import os
import psutil
import requests
from rich.table import Table
from rich.console import Console

API_ID = "YOUR API TOKEN"
ID_CLIENT = "YOUR ID CLIENT"
url =  f"https://api.telegram.org/bot{API_ID}/sendMessage"

console = Console()

while True:
    
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    network = psutil.net_io_counters()
    
    sent = network.bytes_sent
    recv = network.bytes_recv
    
    os.system('clear')
    
    table = Table(title="Montitoring Resource System")
    table.add_column("METRIC", justify="left")
    table.add_column("VALUE", justify="right")
    
    table.add_row("CPU", f"{cpu}%")
    table.add_row("RAM", f"{ram}%")
    table.add_row("DISK", f"{disk}%")
    table.add_row("NETWORK SENT", f"{sent} byte")
    table.add_row("NETWORK RECEIVE", f"{cpu} byte")
    
    if cpu >80:
        table.columns[1].style = "bold red"
        requests.post(url, data={
            "chat_id": ID_CLIENT,
            "text": f"CPU Alert! usage: {cpu}% is higher than 80% at"
        })
        
    console.print(table)
    
    