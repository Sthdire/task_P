from flask import Flask, Blueprint
from flask_restful import Api
from resources.client import Client
from resources.mailing import Mailing
from resources.all_mailing_stats import All
from resources.detail_mailing_stats import Detail


app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Client, '/add_client', '/update_client', '/delete_client')
api.add_resource(Mailing, '/add_mailing', '/update_mailing', '/delete_mailing') #
api.add_resource(All, '/all_mailing_stats')
api.add_resource(Detail, '/detail_mailing_stats')
# api.add_resource(Hello, '/я хз че тут писать что за функция') обработки активных рассылок и отправки сообщений клиентам
