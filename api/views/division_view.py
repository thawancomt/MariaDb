from flask.views import MethodView
from flask import jsonify, request

from ..app import db
from ..services.operation import Operations

from api.schemas.division_schema import OperationSchema, ValidationError

class division(MethodView):
    def post(self):
        data = request.get_json()

        # Validate input data against the schema
        schema = OperationSchema() 
        try:
            valid_data = schema.load(data)
        except ValidationError as err:
            return err.messages, 400



        # get the sum1 and sum2 from the request
        sum1 = request.get_json().get('sum1')
        sum2 = request.get_json().get('sum2')

        # calculate the sum
        result = sum1 / sum2

        # Creating the table before trying to insert data
        db.create_all()
        
        # Intantiate the Operations class
       
        
        operation = Operations(sum1, sum2, result)
        operation.save_division()

        return jsonify({'division': sum1 / sum2})