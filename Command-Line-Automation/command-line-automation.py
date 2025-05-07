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
    

# Examples of basic commands you can try:
# - pwd                   Displays the current directory.
# - ls                    Displays a list of files and directories in a given directory.
# - whoami                Displays the name of the currently active user.
# - date                  Displays the current date and time
# - df -h                 Displays disk usage (in easy-to-read format)
# - ps aux                Displays running processes
# - uptime                Displays the system's active time and system load.
# - free -h               Displays RAM usage
# - top -n 1              Show processes and resources, single run (not live)
# - ping google.com -c 4  Ping to server to check network connection
# - cat filename.txt      Displays the contents of the file