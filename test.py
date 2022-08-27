import requests

req = requests.get('http://127.0.0.1:5000/api/mass_mailing/mail=sasa112')
print(req.text)
