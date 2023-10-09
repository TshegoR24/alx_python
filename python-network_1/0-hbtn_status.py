#!/usr/bin/python3

python
import requests

def fetch_status():
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

status = fetch_status()

if status:
    for key, value in status.items():
        print(f"{key}\t- {value}")
else:
    print("Failed to fetch status.")

   




