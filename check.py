import json

import requests

url = "http://127.0.0.1:8000/login/"
data = {
    "username": "superuser",
    "password": "superuser"
}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
cookie = r.cookies.get_dict()
headers['X-csrftoken'] = cookie['csrftoken']

url = "http://127.0.0.1:8000/won-lotteries/"

r = requests.get(url, cookies=cookie, data=json.dumps(data), headers=headers)
print(r.json())
