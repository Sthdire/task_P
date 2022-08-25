from flask import Flask
from api import api_bp
from datetime import date

from models import db, client, message, mailing_list

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')


def add_mailing_list(message_):
    message__, date_time_start, id_message =add_message(message_)
    new_Mlist = mailing_list(message=message__, date_time_start=date_time_start, id_message=id_message)
    db.session.add(new_Mlist)
    db.session.commit()

#надо пофиксить баг: почему-то в таблицу все записывается по 2 раза

def add_client(phone_n, timezone=''):
    new_client = client(phone_n=phone_n, timezone=timezone)
    db.session.add(new_client)
    db.session.commit()

def add_message(message_):
    today = date.today()
    new_message = message(date_time_create=today, status='false', id_send=0, id_client=0, message=message_)
    db.session.add(new_message)
    db.session.commit()
    msg = message.query.filter_by(message=message_)
    return message_, today, msg.id_message

def change_client_attributes(phone_n, timezone):
    ph = client.query.filter_by(phone_n=phone_n).first()
    ph.timezone = timezone
    db.session.commit()

# add_client(98078792, "121212")
# change_client_attributes(98078792, 'utd')
# obj = client.query.filter_by(phone_n=98078792).first()
# db.session.delete(obj)
# db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
