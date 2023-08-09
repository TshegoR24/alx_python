import requests
response = requests.get("https://alu-intranet.hbtn.io/status")
if response.status_code == 200:
    print("Status Code:", response.status_code)
    print("Content Type:", response.headers.get('content-type'))
    print("Body:")
    print(response.text)
else:
    print("Error:", response.status_code)
