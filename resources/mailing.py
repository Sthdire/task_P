from datetime import date

from flask_restful import Resource

from models import mailing_list, db


class Mailing(Resource):
    def post(self, ml_name, phone_n='', message=''):
        today = date.today()
        new_Mlist = mailing_list(date_time_start=today, ml_name=str(ml_name), phone_n=phone_n, message=message)
        db.session.add(new_Mlist)
        db.session.commit()
        return {"ml_name": ml_name, "phone_n": phone_n, "message": message}

    def put(self, ml_name, phone_n, message):
        ml = mailing_list.query.filter_by(ml_name=ml_name).first()
        ml.message = str(message)
        ml.phone_n = str(phone_n)
        db.session.commit()
        return {"ml_name": ml_name, "phone_n": phone_n, "message": message}

    def delete(self, ml_name):
        ml = mailing_list.query.filter_by(ml_name=ml_name).first()
        db.session.delete(ml)
        db.session.commit()
        return {"deleted_mailing": ml_name}
