#coding: utf-8

from flask_sqlalchemy import SQLAlchemy

# Initialize a database object
# Could be moved to a model.py file
db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super(BaseModel, self).__init__(*args)
