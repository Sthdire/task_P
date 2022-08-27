from flask_restful import Resource

from table_methods import TM

tm = TM()

class Client(Resource):
    def post(self, phone_n):
        if phone_n != '':
            tm.add_client(phone_n)
        return {"phone_n": phone_n}

    def post(self, phone_n, timezone=''):
        if timezone != '':
            tm.add_client(phone_n, timezone)
        return {"phone_n": phone_n, "timezone": timezone}

    def put(self, phone_n, timezone):
        tm.change_client_attributes(phone_n, timezone)
        return {"phone_n": phone_n, "timezone": timezone}

    def delete(self, phone_n):
        tm.delete_client(phone_n)
        return {"phone_n": phone_n}
