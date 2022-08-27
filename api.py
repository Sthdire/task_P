from flask import Blueprint
from flask_restful import Api
from resources.client import Client
from resources.mailing import Mailing
from resources.all_mailing_stats import All
from resources.detail_mailing_stats import Detail
from resources.mass_mailing import Mass
from resources.message import Message

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(Client, '/add_client/phone=<phone_n>', '/add_client/phone=<phone_n>/timezone=<timezone>', '/update_client/phone=<phone_n>/timezone=<timezone>', '/delete_client/phone=<phone_n>')
api.add_resource(Mailing, '/add_mailing/mailing_name=<ml_name>/phone_number=<phone_n>/message=<message>', '/update_mailing/mailing_name=<ml_name>/phone=<phone_n>/message=<message>', '/delete_mailing/mailing_name=<ml_name>')
api.add_resource(Message, '/add_message/message=<message_>', '/delete_message/message=<message_>')
api.add_resource(All, '/all_mailing_stats')
api.add_resource(Detail, '/detail_mailing_stats/mailing=<mailing_mame>')
api.add_resource(Mass, '/mass_mailing/mail=<ml_name>')
