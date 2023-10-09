#!/usr/bin/python3

import requests
import sys

def send_post_request(url, email):
    # Create a dictionary with the email parameter
    data = {'email': email}

    try:
        # Send a POST request to the specified URL with the email parameter
        response = requests.post(url, data=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Display the body of the response
            print("Response Body:")
            print(response.text)
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if both URL and email arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function to send the POST request and display the response
    send_post_request(url, email)




