from flask_restful import Resource

from models import mailing_list
from probe_server_form import mail


class Mass(Resource):
    def get(self, ml_name):
        ml = mailing_list.query.filter_by(ml_name=ml_name).first()
        resp = mail(text=ml.message, number=ml.phone_n)
        return {'if 200 all is ok': resp}
