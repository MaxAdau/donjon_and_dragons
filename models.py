# coding: utf-8

from flask_sqlalchemy import SQLAlchemy

# Initialize a database object
# Could be moved to a model.py file
db = SQLAlchemy()

# Could me moved in a models.py file
# Should take arg from cli
