from flask_restful import Resource

from models import client
from probe_server_form import mail
from table_methods import TM

tm = TM()
class Mass(Resource):
    def get(self, ml_name):
        resp = 0
        arr_phone, arr_mess = tm.get_date(ml_name)
        for i in arr_phone:
            if not client.query.filter_by(phone_n=i).first():
                tm.add_client(i)
            for x in arr_mess:
                resp = mail(text=x, number=i)
                tm.add_message(x, ml_name, i, 'sended')
        return {'if 200 all is ok': resp}
