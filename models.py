from flask_sqlalchemy import SQLAlchemy

from init import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rEtyuol44@localhost/t_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.create_all()


class mailing_list(db.Model):
    id_send = db.Column(db.Integer, primary_key=True, unique=True)
    ml_name = db.Column(db.String, nullable=False)
    message = db.Column(db.String)
    date_time_start = db.Column(db.String, nullable=False)
    phone_n = db.Column(db.String)
    date_time_close = db.Column(db.String)
    id_message = db.Column(db.Integer)


class client(db.Model):
    id_client = db.Column(db.Integer, unique=True, primary_key=True)
    phone_n = db.Column(db.String, nullable=False)
    timezone = db.Column(db.Integer, nullable=False)


class message(db.Model):
    id_message = db.Column(db.Integer, primary_key=True)
    date_time_create = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    ml_name = db.Column(db.String, nullable=False)
    phone_n = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
