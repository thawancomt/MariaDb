from flask.views import MethodView
from flask import jsonify, request


from api.schemas.cheese_schema import cheeseSchema, ValidationError

from api.services.chesse import chesseService

class chesse_calculation(MethodView):

    def __init__(self):
        self.amount = 0
        self.end = 0
        self.result = 0

    @property
    def amount(self):
        return self._amount
    
    # the setter method will update the result when the amount is updated
    @amount.setter
    def amount(self, value):
        o = chesseService(value, 0)

        self.result = o.calculate_chesse()
        self._amount = value

    def get(self):
        return {'message': 'Welcome to the chesse calculation API, send a post to the endpoint with the amount of reposts'}
    
    def post(self):
        data = request.get_json() # Get the data from the json sent

        try: # validate the data against the schema
            valid_data = cheeseSchema().basic().load(data)

            # if ok, lets set the data to the chesseService class
            self.amount = valid_data['amount']
            self.end = valid_data.get('end', 1080)

        except ValidationError as err: # if the data is not valid return the error messages
            return err.messages, 400
        

        # all code above supposed to run if the data is valid
        # Instantiate the chesseService class
        o = chesseService(self.amount, self.end) 
        self.result = o.calculate_chesse() # Calculate the amount of cheese
        
        # Create the response
        response = {
            'amount': self.amount,
            'end': self.end,
            'result': self.result
        }

        try:
            # Validate the response against the response schema
            cheeseSchema().response().load(response)

            # Instantiate the chesseService class

            chesse = chesseService(amount=response['amount'], end=response['end'])
            chesse.save_db() # Save the response to the database

            return response, 201 # Sucess
        
        except ValidationError as err:
            return err.messages, 400 # if the response is missing some information or is not valid return the error messages

class updateChesseAmount(MethodView):

    def post(self):
        data = request.get_json()

        try:
            valid_data = cheeseSchema().update().load(data)

            id = valid_data['id']

            operation = chesseService(valid_data['amount'], valid_data.get('end', 1080))

            v = operation.update_db(id)
            

        except ValidationError as err:
            return err.messages, 401
        
        return {'message': f'{v}, Updated'}, 201
        

class deleteCheeseAmount(MethodView):

    def post(self):
        data = request.get_json()

        try:
            valid_data = cheeseSchema().update().load(data)

            id = valid_data['id']

            chesse = chesseService(0, 0)

            chesse.delete_db(id)

        except ValidationError as err:
            return err.messages, 401