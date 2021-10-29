# From the current package import the database
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # func gets the current date
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))



class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # Primary Key
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')