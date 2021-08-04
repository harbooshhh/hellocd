

from datetime import datetime
from config import db, ma

class Person(db.Model):
    __tablename__ = 'Persons'
    ThingId = db.Column(db.String(64), primary_key=True)
    Name = db.Column(db.String(50), index=True,nullable=False)
    Gender = db.Column(db.String(350), nullable=False)
    Nationality = db.Column(db.String(50))
    ContactId = db.Column(db.String(50))
    Address = db.Column(db.String(50))
    EMPTY = db.Column(db.String(50))

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqla_session = db.session


