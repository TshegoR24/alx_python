#!/usr/bin/python3
import requests
import sys

def get_x_request_id(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Check if the 'X-Request-Id' header is present in the response
            if 'X-Request-Id' in response.headers:
                # Print the value of the 'X-Request-Id' header
                print(f"X-Request-Id: {response.headers['X-Request-Id']}")
            else:
                print("X-Request-Id header not found in the response.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)





