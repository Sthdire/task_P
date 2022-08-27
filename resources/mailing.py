from flask_restful import Resource

from table_methods import TM

tm = TM()

class Mailing(Resource):
    def post(self, ml_name, phone_n='', message=''):
        tm.add_mailing_list(ml_name, phone_n, message)
        return {"ml_name": ml_name, "phone_n": phone_n, "message": message}

    def put(self, ml_name, phone_n, message):
        tm.change_ml_attributes(ml_name, phone_n, message)
        return {"ml_name": ml_name, "phone_n": phone_n, "message": message}

    def delete(self, ml_name):
        tm.delete_mailing_list(ml_name)
        return {"deleted_mailing": ml_name}
