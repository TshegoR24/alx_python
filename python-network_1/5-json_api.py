#!/usr/bin/python3

import sys
import requests

def get_user_id(username, password):
    # Define the GitHub API URL for the authenticated user
    api_url = f'https://api.github.com/user'

    # Create a basic authentication header with the username and personal access token
    auth = (username, password)

    # Send a GET request to the GitHub API using Basic Authentication
    response = requests.get(api_url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the user ID
        user_data = response.json()
        user_id = user_data['id']
        return user_id
    else:
        print(f"Failed to retrieve user data. Status code: {response.status_code}")
        return None

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python github_user_id.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    user_id = get_user_id(username, personal_access_token)

    if user_id is not None:
        print(f"User ID for {username}: {user_id}")
    else:
        print("User ID retrieval failed.")


