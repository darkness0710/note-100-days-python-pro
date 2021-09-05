import requests

# python -m pip install requests

response = requests.get("http://api.open-notify.org/astros.json")

if (response.status_code == 200):
    print(response.json())