import requests
import sys

def send_post_request(url, email):
    data = {'email': email}
    response = requests.post(url, data=data)
    return response.text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: hr@holbertonschool.com <URL> <email>")
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)

    print("Response body:")
    print(response_body)
