import os, time

def ping():
    hostname = "127.0.0.1"
    response = os.system("ping -c 10 " + hostname)
    print(response)

while True:
    ping()
    time.sleep(3)