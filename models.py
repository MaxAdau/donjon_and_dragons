# coding: utf-8

from flask_sqlalchemy import SQLAlchemy

# Initialize a database object
# Could be moved to a model.py file
db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models

class YourModel(BaseModel):
    """model for one of your table"""
    __tablename__ = 'my_table'
    # define your model

