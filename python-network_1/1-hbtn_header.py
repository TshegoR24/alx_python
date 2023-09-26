#!/usr/bin/python3


import requests
import sys

def main():
    url = sys.argv[1]
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        print(f'X-Request-Id: {request_id}')
    else:
        print('X-Request-Id not found in response header')

if __name__ == '__main__':
    main()



