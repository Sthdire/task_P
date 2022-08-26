import requests
from flask_restful import Resource
from requests.structures import CaseInsensitiveDict

from probe_server_form import mail


class Mass(Resource):
    def get(self):
        resp = mail()
        return resp
