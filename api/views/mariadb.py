from flask import jsonify
from flask.views import MethodView
from api.models.summation_model import db

from sqlalchemy import text

class mariadbconnector(MethodView):
    def get(self):
        result = db.session.execute(text('SHOW DATABASES;'))
        list_result = [row[0] for row in result]
        return jsonify({'result' : f'{list_result}'})