
from marshmallow import Schema, fields, ValidationError

class OperationSchema(Schema):
    sum1 = fields.Float(required=True, error_messages={'required': 'sum1 is required'})
    sum2 = fields.Float(required=True, error_messages={'validator_failed': 'sum2 is ddmissing'})


    result = fields.Float(dump_only=True)