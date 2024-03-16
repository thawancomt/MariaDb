
from typing import Any
from marshmallow import Schema, fields, ValidationError

class cheeseSchema():

    """
    basic: Schema for the request
    response: Schema for the response
    update: Schema for the update
    """

    @staticmethod
    def basic() -> Schema:
        class cheeseSchema(Schema):
            amount = fields.Integer(required=True, error_messages={'required': 'amount is required'})
            end = fields.Integer(required=False)
            result = fields.Integer(required=False, dump_only=True)
        return cheeseSchema()
    
    @staticmethod
    def response() -> Schema:
        class cheeseResponseSchema(Schema):
                amount = fields.Integer(required=True, error_messages={'required': 'amount is required'})
                end = fields.Integer(required=False)
                result = fields.Integer(required=True, error_messages={'required': 'result is required'})
        return cheeseResponseSchema()
    
    @staticmethod
    def update() -> Schema:
        class updateChesseAmountSchema(Schema):
            amount = fields.Integer(required=True, error_messages={'required': 'amount is required'})
            end = fields.Integer(required=False)
            result = fields.Integer(required=False, dump_only=True)
            id = fields.Integer(required=True, error_messages={'required': 'id is required'})
        return updateChesseAmountSchema()