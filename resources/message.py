from datetime import date

from flask_restful import Resource

from models import db, message


class Message(Resource):
    def post(self, message_):
        today = date.today()
        new_message = message(date_time_create=today, status='false', id_send=0, id_client=0, message=message_)
        db.session.add(new_message)
        db.session.commit()
        return {'message': message_}

    def delete(self, message_):
        m = message.query.filter_by(message=message_).first()
        db.session.delete(m)
        db.session.commit()
        return {'message': message_}
