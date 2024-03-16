from flask_sqlalchemy import SQLAlchemy

from api.app import db

class chesseModel(db.Model):

    # Define the table name
    __tablename__ = 'chesse'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    end = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)