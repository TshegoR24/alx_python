#!/usr/bin/python3

python
import requests
import sys

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    response = requests.post(url, data=params)

    if response.status_code == 200:
        try:
            json_data = response.json()
            if json_data:
                for user in json_data:
                    print(f"[{user['id']}] {user['name']}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print(f"Request failed with status code {response.status_code}")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
