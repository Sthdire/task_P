from flask_restful import Resource

from probe_server_form import mail
from table_methods import TM

tm = TM()
class Mass(Resource):
    def get(self, ml_name):
        ml = tm.get_date(ml_name)
        resp = mail(text=ml[0], number=ml[1])
        return {'if 200 all is ok': resp}
