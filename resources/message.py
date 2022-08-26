from datetime import date

from flask_restful import Resource

from models import db, message
from table_methods import TM

tm = TM()
class Message(Resource):
    def post(self, message_):
        tm.add_message(message_)
        return {'message': message_, 'added': 'True'}

    def delete(self, message_):
        tm.delete_message(message_)
        return {'message': message_, 'deleted': 'True'}
