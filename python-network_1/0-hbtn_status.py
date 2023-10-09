#!/usr/bin/python3

import requests

url = 'https://alu-intranet.hbtn.io/status'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

    # Display the response body with tabulation before each line
    lines = response.text.split('\n')
    formatted_response = '\n'.join(['\t' + line for line in lines])

    print(formatted_response)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

   




