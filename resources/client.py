from flask_restful import Resource

from models import client, db


class Client(Resource):
    def post(self, phone_n):
        new_client = client(phone_n=phone_n, timezone='')
        db.session.add(new_client)
        db.session.commit()
        return {"phone_n": phone_n}

    def post(self, phone_n, timezone=''):
        new_client = client(phone_n=phone_n, timezone=timezone)
        db.session.add(new_client)
        db.session.commit()
        return {"phone_n": phone_n, "timezone": timezone}

    def put(self, phone_n, timezone):
        ph = client.query.filter_by(phone_n=phone_n).first()
        ph.timezone = timezone
        db.session.commit()
        return {"phone_n": phone_n, "timezone": timezone}

    def delete(self, phone_n):
        c = client.query.filter_by(phone_n=phone_n).first()
        db.session.delete(c)
        db.session.commit()
        return {"phone_n": phone_n}
