import requests
from requests.structures import CaseInsensitiveDict

url = "https://probe.fbrq.cloud/v1/send/0"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI2OTgzNTEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6InN0aF9kIn0.BI27wHykGwbUOndVR4vlocGc1VDF977JDSn0sVFzlsY"
headers["Content-Type"] = "application/json"

data = """
{
  "id": 0,
  "phone": 0,
  "text": "string"
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
