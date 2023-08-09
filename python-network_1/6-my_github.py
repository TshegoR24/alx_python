import sys
import requests

def get_user_id(username, token):
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        return user_id
    else:
        print(f"Error: Unable to fetch user information. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <token>")
        sys.exit(1)
    
    username = sys.argv[1]
    token = sys.argv[2]
    
    user_id = get_user_id(username, token)
    if user_id is not None:
        print(f"Your GitHub user id is: {user_id}")
