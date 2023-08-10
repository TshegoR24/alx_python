#!/usr/bin/python3
"""
GitHub User ID Retrieval Script

This script takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your user ID. Basic Authentication with a personal
access token is used to access your information (only read:user permission is needed).

Usage: python script.py <username> <access_token>

You must use the package requests and sys.
You are not allowed to import packages other than requests and sys.

Note: Storing credentials directly in the script is not recommended for security reasons.
"""

import requests
import sys

def get_user_id(username, access_token):
    """
    Get the user ID for the given GitHub username using the provided personal access token.

    Args:
        username (str): Your GitHub username.
        access_token (str): Your personal access token.

    Returns:
        int: The user's GitHub ID.
    """
    url = f'https://api.github.com/users/{TshegoR24}'
    headers = {'Authorization': f'Basic {access_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data['id']
    else:
        print(f"Error: {response.status_code}")
        sys.exit(1)

class GitHubIDScript:
    """
    A class representing a GitHub User ID Retrieval Script.

    This class provides methods to interact with the GitHub API and retrieve user ID.
    """

    def __init__(self):
        pass

    @staticmethod
    def get_user_id(username, access_token):
        """
        Get the user ID for the given GitHub username using the provided personal access token.

        Args:
            username (str): Your GitHub username.
            access_token (str): Your personal access token.

        Returns:
            int: The user's GitHub ID.
        """
        url = f'https://api.github.com/users/{username}'
        headers = {'Authorization': f'Basic {access_token}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            user_data = response.json()
            return user_data['id']
        else:
            print(f"Error: {response.status_code}")
            sys.exit(1)

def main():
    """
    Main function to execute the script.

    Parses command line arguments, retrieves GitHub user ID,
    and prints the result.
    """
    if len(sys.argv) < 3:
        print("Usage: python script.py <username> <access_token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    user_id = get_user_id(username, access_token)
    print(f"User ID for {username}: {user_id}")

if __name__ == "__main__":
    main()


