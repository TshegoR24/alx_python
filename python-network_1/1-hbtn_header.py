import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(f"X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id not found in response headers.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
