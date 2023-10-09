#!/usr/bin/python3

python
import requests
import sys

def get_request_id(url):
    try:
        response = requests.get(url)
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(f'The value of X-Request-Id is: {request_id}')
        else:
            print('The X-Request-Id header is not present in the response.')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
        sys.exit(1)

if __name__ == '__main__':
    url = 'https://www.example.com'
    get_request_id(url)



