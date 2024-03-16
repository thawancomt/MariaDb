from api.models.cheese_model import chesseModel
from ..app import db
from flask import jsonify
import json


class chesseService():
    
    def __init__(self, amount, end):
        self.amount = amount
        self.end = end
        self.result = self.calculate_chesse()
        db.create_all()

    
    def update_db(self, id):

        old = chesseModel.query.filter_by(id=id).first()


        chesse = chesseModel.query.filter_by(id=id).update(
             {
                'amount': self.amount,
                'end': self.end,
                'result': self.result
             }
        )

        # Create the response
        response = {
             "old" : {
                "amount": old.amount,
                "end": old.end,
                "result": old.result
             },
                "new" : {
                    "amount": self.amount,
                    "end": self.end,
                    "result": self.result
                }
        }

        


        # we need to commit the changes
        db.session.commit()

        return json.loads(json.dumps(response, indent=4))

    def delete_db(self, id):
        chesse = chesseModel.query.filter_by(id=id).delete()
        db.session.commit()
    
    def save_db(self):
        chesse = chesseModel(amount=self.amount, end=self.end, result=self.result)
        db.session.add(chesse)
        db.session.commit()

    def calculate_chesse(self): # Function to calculate the amounnt of cheese in GRAMS
            return (self.amount * 4020) + 1080 if not self.end else (self.amount * 4020) - (self.end - 1080) 