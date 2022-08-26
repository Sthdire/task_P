import requests

req = requests.post('http://127.0.0.1:5000/api/add_client/phone=abraham')
print(req.text)