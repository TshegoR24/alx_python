#!/usr/bin/python3
import requests

def fetch_and_display_status(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    fetch_and_display_status(url)


