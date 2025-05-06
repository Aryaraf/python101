import subprocess
from datetime import datetime

while True: 
    command = input("Enter command: ").split()
    time = datetime.now().strftime("%Y-%m-%d ")
    
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    
    text = "\nCommand: {} \nDate: {} \nOutput: {}".format(command, time, result.stdout)
    
    with open("log_activity.txt", "a") as log_file:
        log_file.write(text)
        
    print("\n==Result==")
    with open ("log_activity.txt", "r") as log_file:
        print(log_file.read())
        
    loop = input("You want use this program again? (Y/n): ")
    if loop.lower() != "y":
        break
    
        
    