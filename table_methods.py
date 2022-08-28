from datetime import datetime

from models import db, client, message, mailing_list


class TM:
    def add_mailing_list(self, ml_name, phone_n, message):
        now = datetime.now()
        x = datetime.now()
        r = x.day + 2
        x = x.replace(day=r)
        new_Mlist = mailing_list(date_time_start=now, ml_name=ml_name, phone_n=phone_n, message=message, date_time_close=str(x), id_message=tm.add_message(message, ml_name, phone_n,))
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
        return message.query[-1].id_message

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

    '''ненужный метод'''
    # def delete_message(self, message_):
    #     m = message.query.filter_by(message=message_).first()
    #     db.session.delete(m)
    #     db.session.commit()

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
        arr_phone, arr_mess = tm.get_date(ml_name)
        return len(arr_phone), len(arr_mess)

    def get_detailed_statistick(self):
        arr_ml = []
        stf = ''
        for ml in mailing_list.query:
            if not ml.ml_name in arr_ml:
                arr_ml.append(ml.ml_name)
        for x in arr_ml:
            f = 0
            s = 0
            for h in mailing_list.query:
                if h.ml_name == x:
                    m = message.query.filter_by(id_message=h.id_message).first()
                    if m.status == 'false':
                        f += 1
                    else:
                        s += 1
            stf += 'list: ' + x  + '     no sended:  ' + str(f) + '     sended:  ' + str(s) +'\n'
        return stf
tm = TM()
