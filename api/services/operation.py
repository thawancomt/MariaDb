from ..app import db
from ..models.summation_model import summation_model
from ..models.division_model import division_model

class Operations():
    def __init__(self, sum1, sum2, result):
        self.result = result
        self.sum1 = sum1
        self.sum2 = sum2

    def save(self):
        summation_operation = summation_model(sum1=self.sum1, sum2=self.sum2, result=self.result)
        db.session.add(summation_operation)
        db.session.commit()

    def save_division(self):
        summation_operation = division_model(sum1=self.sum1, sum2=self.sum2, result=self.result)
        db.session.add(summation_operation)
        db.session.commit()