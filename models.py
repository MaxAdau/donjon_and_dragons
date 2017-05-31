# coding: utf-8

from flask_sqlalchemy import SQLAlchemy
import datetime

# Initialize a database object
# Could be moved to a model.py file
db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


# TODO move it to another file
class Character(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'chars'

    # incremental ID
    id = db.Column(db.Integer, primary_key=True)

    # About the character
    player_name = db.Column(db.String)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    level = db.Column(db.Integer)

    # TODO change it to custom type
    race = db.Column(db.String)
    klass = db.Column(db.String)

    # Character carac
    # TODO put it in a custom type
    str = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    wis = db.Column(db.Integer)
    cha = db.Column(db.Integer)

    # Base attack Bonus
    BAB = db.Column(db.Integer)

    # Armor Class
    AC_natural = db.Column(db.Integer)
    magic_resist = db.Column(db.Integer)
    # TODO calculate it instead of hard code it
    AC = db.Column(db.Integer)
    AC_flatfooted = db.Column(db.Integer)
    AC_touch = db.Column(db.Integer)

    # Size and speed
    size = db.Column(db.Integer)
    initiative = db.Column(db.Integer)

    # TODO Should be calculated
    speed = db.Column(db.Integer)

    # Saving throw
    SAVE_ref = db.Column(db.Integer)
    SAVE_for = db.Column(db.Integer)
    SAVE_will = db.Column(db.Integer)

    # Weapons # TODO Change type to weapon type
    right_hand = db.Column(db.String)
    left_hand = db.Column(db.String)

    # Armor # TODO Change type armor/shield type
    armor = db.Column(db.String)
    shield = db.Column(db.String)

    # Stuff # TODO change it to list os equipement type
    head_protection = db.Column(db.String)
    hand_protection = db.Column(db.String)
    foot_protection = db.Column(db.String)
    head_protection = db.Column(db.String)










