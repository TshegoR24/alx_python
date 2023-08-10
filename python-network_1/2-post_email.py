#!/usr/bin/python3

import requests
import sys

def send_post_request(url, email):
    data = {'email': email}
    response = requests.post(url, data=data)
    return response.text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = "hr@holbertonschool.com"

    response_body = send_post_request(url, email)

    print("Response body:")
    print(response_body)

