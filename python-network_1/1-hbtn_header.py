"""
This module defines a class that sends a GET request to a given URL and displays the value of the X-Request-Id header from the response.
"""

import requests
import sys

class XRequestIdFetcher:
    """
    A class for fetching and displaying the X-Request-Id header from a given URL's response.

    Attributes:
        url (str): The URL to send the GET request to.
    """

    def __init__(self, url):
        """
        Initialize the XRequestIdFetcher class with a URL.

        Args:
            url (str): The URL to send the GET request to.
        """
        self.url = url

    def get_x_request_id(self):
        """
        Send a GET request to the provided URL and display the value of the X-Request-Id header.

        Returns:
            None
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception if the response status code is not 2xx
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id header not found in the response.")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            sys.exit(1)

def fetch_x_request_id(url):
    """
    Fetch the X-Request-Id header from a provided URL.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        None
    """
    fetcher = XRequestIdFetcher(url)
    fetcher.get_x_request_id()

if __name__ == "__main__":
    input_url = input("Enter the URL: ")
    fetch_x_request_id(input_url)

