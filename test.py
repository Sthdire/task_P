import requests

req = requests.delete('http://127.0.0.1:5000/api/delete_message/message=zaebal')
print(req.text)
