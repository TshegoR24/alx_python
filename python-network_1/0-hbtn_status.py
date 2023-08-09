"""
Fetches and displays the status from a given URL using the requests package.
"""

import requests


def fetch_and_display_status(url):
    """
    Fetches the status from the specified URL and displays the response body.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None

    Raises:
        requests.exceptions.RequestException: If an error occurs during the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        body_lines = response.text.strip().split('\n')
        formatted_body = "\n".join(['\t- ' + line.strip() for line in body_lines])

        print(formatted_body)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


class StatusFetcher:
    """
    A class for fetching and displaying the status from a given URL.

    Attributes:
        url (str): The URL to fetch the status from.

    Methods:
        __init__: Initializes a StatusFetcher instance.
        fetch_and_display: Fetches the status from the specified URL and displays the response body.
    """

    def __init__(self, url):
        """
        Initializes a StatusFetcher instance.

        Args:
            url (str): The URL to fetch the status from.
        """
        self.url = url

    def fetch_and_display(self):
        """
        Fetches the status from the specified URL and displays the response body.

        Returns:
            None

        Raises:
            requests.exceptions.RequestException: If an error occurs during the request.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            body_lines = response.text.strip().split('\n')
            formatted_body = "\n".join(['\t- ' + line.strip() for line in body_lines])

            print(formatted_body)

        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    """
    Entry point of the script.
    """
    url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(url)

    status_fetcher = StatusFetcher(url)
    status_fetcher.fetch_and_display()

