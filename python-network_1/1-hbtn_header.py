import requests
import sys
url = sys.argv[1]
response = requests.get(url)
if response.status_code == 200:
    print("X-Request-Id:", response.headers.get('X-Request-Id'))
else:
    print("Error:", response.status_code)
