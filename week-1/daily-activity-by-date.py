import json
import os
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
filename = f"log_{date}.json"
 
if os.path.exists(filename):
    with open(filename, "r") as file:
        data = json.load(file)
else:
    data = []
    
while True:
    print("Log activity by date")
    
    activity = input("Enter activity: ")
    data.append({"Activity": activity, "Time": date})
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        
        print("\nList Log")
    for i, item in enumerate(data, start=1):
        print(f"{i}. Activity: {item['Activity']}, Time: {item['Time']},")    
        
    loop = input("You want repeat again? (Y/n): ")
    if loop.lower() != "y":
        break