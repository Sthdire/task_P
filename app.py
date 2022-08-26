from api import api_bp
from datetime import date
from init import app

from models import db, client, message, mailing_list

app.register_blueprint(api_bp, url_prefix='/api')


# def add_mailing_list(ml_name, phone_n='', message=''):
#     today = date.today()
#     new_Mlist = mailing_list(date_time_start=today, ml_name=ml_name, phone_n=phone_n, message=message)
#     db.session.add(new_Mlist)
#     db.session.commit()

#надо пофиксить баг: почему-то в таблицу все записывается по 2 раза

# def add_client(phone_n, timezone=''):
#     new_client = client(phone_n=phone_n, timezone=timezone)
#     db.session.add(new_client)
#     db.session.commit()


# def add_message(message_):
#     today = date.today()
#     new_message = message(date_time_create=today, status='false', id_send=0, id_client=0, message=message_)
#     db.session.add(new_message)
#     db.session.commit()
#     msg = message.query.filter_by(message=message_)
#     return message_, today, msg.id_message

# def change_client_attributes(phone_n, timezone):
#     ph = client.query.filter_by(phone_n=phone_n).first()
#     ph.timezone = timezone
#     db.session.commit()

# def change_ml_attributes(ml_name, phone_n, message):
#     ml = mailing_list.query.filter_by(ml_name=ml_name).first()
#     ml.message = message
#     ml.phone_n = phone_n
#     db.session.commit()


# def delete_client(phone_n):
#     c = client.query.filter_by(phone_n=phone_n).first()
#     db.session.delete(c)
#     db.session.commit()

def delete_message(message_):
    m = message.query.filter_by(message=message_).first()
    db.session.delete(m)
    db.session.commit()

# def delete_mailing_list(ml_name):
#     ml = mailing_list.query.filter_by(ml_name=ml_name).first()
#     db.session.delete(ml)
#     db.session.commit()

def get_date(ml_name):
    ml = mailing_list.query.filter_by(ml_name=ml_name).first()
    return ml.message, ml.phone_n




# add_client(91078791 , "121212")
# change_client_attributes(98078792, 'utd')

# delete_client(91078791)
# add_mailing_list('test')
# delete_mailing_list('test')
# print(get_date('test'))

if __name__ == '__main__':
    app.run(debug=True)
