#!/usr/bin/python3

python
import requests
import sys

def send_post_request(url, email):
    response = requests.post(url, data={'email': email})
    return response.text

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_post_request(url, email)
    print(response_body)




