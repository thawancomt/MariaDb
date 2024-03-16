from flask.views import MethodView
from flask import jsonify, request

from ..app import db
from ..services.operation import Operations


class summation(MethodView):

    def post(self):
        # get the sum1 and sum2 from the request
        sum1 = request.get_json().get('sum1')
        sum2 = request.get_json().get('sum2')

        # calculate the sum
        result = sum1 + sum2

        # Creating the table before trying to insert data
        db.create_all()
        
        # Intantiate the Operations class
        
        operation = Operations(sum1, sum2, result)
        operation.save() # And then save the result to the database

        return jsonify({'sum': sum1 + sum2})