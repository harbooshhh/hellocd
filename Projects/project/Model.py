

from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50))
    fullname = db.Column(db.String(length=50))
    nickname = db.Column(db.String(length=50))
 
    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
                            self.name, self.fullname, self.nickname)

