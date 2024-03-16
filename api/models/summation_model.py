from ..app import db
from flask_sqlalchemy import SQLAlchemy

class summation_model(db.Model):

    # Define the table name
    __tablename__ = 'summation'

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # autoincrement=True is used to autoincrement the id
    sum1 = db.Column(db.Integer, nullable=False)
    sum2 = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)