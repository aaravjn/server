import datetime
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

url = "http://127.0.0.1:8000/d466072c4f71832b3ee11ac6afa6dec0/"
r = requests.post(url, cookies=cookie, data=json.dumps(data), headers=headers)
with open('/home/shubham/Desktop/server/debug.log', mode='a') as file:
    file.write('\n')
    file.write('Accessed at ' + str(datetime.datetime.now()) + ' hours!    ')
    file.write(r.__str__())
    file.write('\n')
    if r.status_code == 200:
        file.write(r.json().__str__())
file.close()
