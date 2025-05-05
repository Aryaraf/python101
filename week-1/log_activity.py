import json
import os
from datetime import datetime

data = []
    
if os.path.exists("log_activity.json"):
    with open("log_activity.json", "r") as file:
        data = json.load(file)

while True:
            
    print("=================")
    print("LOG ACTIVITY")
    print("=================")
    
    activity = input("Masukkan aktifitas: ")   
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data.append({"Aktifitas": activity, "Waktu": time})
    
    with open("log_activitiy.json", "w") as file:
        json.dump(data, file, indent=4)
        
    print("\n==Daftar Log==")
    for i, item in enumerate(data, start=1):
        print(f"{i}. Aktifitas: {item['Aktifitas']}, Waktu: {item['Waktu']}")
        
    lanjut = input("\nApakah anda ingin masukkan aktifitas lagi? (Y/n): ")
    if lanjut.lower() != "y":
        break
    