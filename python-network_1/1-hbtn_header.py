#!/usr/bin/python3

"""
This script retrieves the value of the 'X-Request-Id' header from an HTTP response.

Usage:
    python script_name.py <url>

Arguments:
    <url>: The URL to send an HTTP GET request to.

The 'X-Request-Id' header value from the response will be displayed.
"""

import requests
import sys


def get_x_request_id(url):
    """
    Send an HTTP GET request to the given URL and display the 'X-Request-Id' header value from the response.

    Args:
        url (str): The URL to send the HTTP GET request to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id not found in the response header.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


class XRequestIdRetriever:
    """
    A class to retrieve the 'X-Request-Id' header value from an HTTP response.

    Attributes:
        url (str): The URL to send the HTTP GET request to.
    """

    def __init__(self, url):
        self.url = url

    def get_x_request_id(self):
        """
        Send an HTTP GET request to the URL and display the 'X-Request-Id' header value from the response.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            x_request_id = response.headers.get('X-Request-Id')

            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id not found in the response header.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)



