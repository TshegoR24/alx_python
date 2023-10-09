#!/usr/bin/python3

import requests
import sys

# Define the URL
url = "http://0.0.0.0:5000/search_user"

# Check if there is a command line argument for the letter, set q to "" if none provided
if len(sys.argv) == 2:
    q = sys.argv[1]
else:
    q = ""

# Send a POST request with the letter as a parameter
response = requests.post(url, data={"q": q})

# Check the response status code
if response.status_code != 200:
    print("Error: Unable to access the server.")
    sys.exit(1)

# Try to parse the response JSON
try:
    data = response.json()
except ValueError:
    print("Not a valid JSON")
    sys.exit(1)

# Check if the JSON is empty
if not data:
    print("No result")
else:
    # Display id and name for each item in the JSON
    for item in data:
        print(f"[{item['id']}] {item['name']}")
