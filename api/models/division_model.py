from flask_sqlalchemy import SQLAlchemy

from ..app import db

class division_model(db.Model):

    # Define the table name
    __tablename__ = 'division'

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # autoincrement=True is used to autoincrement the id
    sum1 = db.Column(db.Integer, nullable=False)
    sum2 = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)