from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask.views import MethodView
from flask_restful import Api

app = Flask(__name__)

# import the configuration file
app.config.from_object('config')

# Setting the database / Maria DB
db = SQLAlchemy(app)
    

# importing methods

from api.views.summation_view import summation
from api.views.mariadb import mariadbconnector
from api.views.division_view import division
from api.views.cheese_view import chesse_calculation, updateChesseAmount


api = Api(app)

api.add_resource(summation, '/sum')
api.add_resource(mariadbconnector, '/mariadbconnector')
api.add_resource(division, '/division')
api.add_resource(chesse_calculation, '/chesse')
api.add_resource(updateChesseAmount, '/cheese/update')


