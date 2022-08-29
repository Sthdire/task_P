from flask_restful import Resource

from table_methods import TM

tm = TM()
class Detail(Resource):
    def get(self):
        return {'Get detailed statistic:': tm.get_detailed_statistick()}
