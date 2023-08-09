import sys
import requests

def search_user_by_letter(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {'q': letter}

    response = requests.post(url, params=params)

    try:
        response_json = response.json()
        if response_json:
            user_id = response_json.get('id', '')
            user_name = response_json.get('name', '')
            if user_id and user_name:
                print(f"[{user_id}] {user_name}")
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user_by_letter(letter)
