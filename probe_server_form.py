import json
import requests
from requests.structures import CaseInsensitiveDict


def mail(id=0, number=0, text=''):
    url = "https://probe.fbrq.cloud/v1/send/0"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI2OTgzNTEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6InN0aF9kIn0.BI27wHykGwbUOndVR4vlocGc1VDF977JDSn0sVFzlsY"
    headers["Content-Type"] = "application/json"

    data = {'id': id, 'phone': number, 'text': text}
    data = json.dumps(data)

    resp = requests.post(url, headers=headers, data=data)

    return resp.status_code
