# coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
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
    """Model for the character table"""
    __tablename__ = 'chars'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # About the character
    player_name = Column(String)
    name = Column(String)
    age = Column(Integer)
    level = Column(Integer)
    description = Column(String)

    # TODO change it to custom type
    # http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html
    race_id = Column(Integer, ForeignKey("races.id"))
    race = db.relationship("Address", foreign_keys=[race_id])
    klass = Column(String)

    # Character carac
    # TODO put it in a custom type
    str = Column(Integer)
    dex = Column(Integer)
    con = Column(Integer)
    int = Column(Integer)
    wis = Column(Integer)
    cha = Column(Integer)

    # Base attack Bonus
    BAB = Column(Integer)

    # Armor Class
    AC_natural = Column(Integer)
    magic_resist = Column(Integer)
    # TODO calculate it instead of hard code it
    AC = Column(Integer)
    AC_flatfooted = Column(Integer)
    AC_touch = Column(Integer)

    # Size and speed
    size = Column(Integer)
    initiative = Column(Integer)

    # TODO Should be calculated
    speed = Column(Integer)

    # Saving throw
    SAVE_ref = Column(Integer)
    SAVE_for = Column(Integer)
    SAVE_will = Column(Integer)

    # Weapons # TODO Change type to weapon type
    right_hand = Column(String)
    left_hand = Column(String)

    # Armor # TODO Change type armor/shield type
    armor = Column(String)
    shield = Column(String)

    # Stuff # TODO change it to list os equipement type
    head_protection = Column(String)
    hand_protection = Column(String)
    foot_protection = Column(String)
    ring_1 = Column(String)


class Race(BaseModel, db.Model):
    """Model for the race table"""
    __tablename__ = 'races'

    # incremental ID
    id = Column(Integer, primary_key=True)

    # About the race
    name = Column(String)
    description = Column(String)

    # TODO move it to an ENUM type
    size = Column(String)








