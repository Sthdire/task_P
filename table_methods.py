from datetime import datetime

from models import db, client, message, mailing_list


class TM:
    def add_mailing_list(self, ml_name, phone_n='', message=''):
        now = datetime.now()
        x = datetime.now()
        r = x.day + 2
        x = x.replace(day=r)
        new_Mlist = mailing_list(date_time_start=now, ml_name=ml_name, phone_n=phone_n, message=message, date_time_close=str(x))
        db.session.add(new_Mlist)
        db.session.commit()

    def add_client(self, phone_n, timezone=''):
        new_client = client(phone_n=phone_n, timezone=timezone)
        db.session.add(new_client)
        db.session.commit()

    def add_message(self, message_, ml_name, phone_n, status='false'):
        now = datetime.now()
        new_message = message(date_time_create=now, status=status, ml_name=ml_name, phone_n=phone_n, message=message_)
        db.session.add(new_message)
        db.session.commit()

    def change_ml_attributes(self, ml_name, phone_n, message_):
        ml = mailing_list.query.filter_by(ml_name=ml_name).first()
        ml.message = message_
        ml.phone_n = phone_n
        db.session.commit()

    def change_client_attributes(self, phone_n, timezone):
        ph = client.query.filter_by(phone_n=phone_n).first()
        ph.timezone = timezone
        db.session.commit()

    def delete_mailing_list(self, ml_name):
        ml = mailing_list.query.filter_by(ml_name=ml_name).first()
        db.session.delete(ml)
        db.session.commit()

    def delete_client(self, phone_n):
        c = client.query.filter_by(phone_n=phone_n).first()
        db.session.delete(c)
        db.session.commit()

    def delete_message(self, message_):
        m = message.query.filter_by(message=message_).first()
        db.session.delete(m)
        db.session.commit()

    def get_date(self, ml_name):
        arr_mess = []
        arr_phone = []
        for ml in mailing_list.query:
            if ml.ml_name == ml_name:
                if not ml.phone_n in arr_phone:
                    arr_phone.append(ml.phone_n)
                if not ml.message in arr_mess:
                    arr_mess.append(ml.message)
        return arr_phone, arr_mess

    def get_statistick(self, ml_name):
        arr_mess = []
        arr_phone = []
        for ml in mailing_list.query:
            if ml.ml_name == ml_name:
                if not ml.phone_n in arr_phone:
                    arr_phone.append(ml.phone_n)
                if not ml.message in arr_mess:
                    arr_mess.append(ml.message)
        return len(arr_phone), len(arr_mess)





tm = TM()
# tm.get_date('sasa112')
# for x in range(13):
#     tm.add_mailing_list('sasa112', str(x+1), 'sdjjsdjsjdj')
print(tm.get_statistick('sasa112'))
