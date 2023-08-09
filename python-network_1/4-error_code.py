import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    print("Response body:")
    print(response.text)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

if __name__ == "__main__":
    main()
