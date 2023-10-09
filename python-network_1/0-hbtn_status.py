#!/usr/bin/python3

import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
else:
    print(f"Error: Status code {response.status_code}")



   




