import sys
import requests

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        return

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Response body:")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    main()
