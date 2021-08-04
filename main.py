
from flask import Flask, render_template,jsonify
from dbmodel_Hajj import db, User
from flask_sqlalchemy import SQLAlchemy
import base64
import json
from flask_marshmallow import Marshmallow


app = Flask(__name__)
#db = SQLAlchemy(app)

ma=Marshmallow(app)
"""
# @app.template_filter()

# def b64encode(s):
#    return base64.b64encode(s)

# app.jinja_env.filters['b64encode'] = b64encode



# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:smhh2112@localhost:3306/sqlalchemy',echo=True)

#Base.metadata.create_all(engine)
 """

# Create a session
#Session = SQLAlchemy.orm.sessionmaker()
session=db.session.configure(bind=engine)
#session = Session()
 
# Add a user
jwk_user = User(name='jesper', fullname='Jesper Wisborg Krogh', nickname='test11')
session.add(jwk_user)
session.commit()

 
# Query the user
our_user = db.session.query(User).filter_by(name='jesper').first()
print('\nOur User:')
print(our_user)
print('Nick name in hex: {0}'.format(our_user.nickname.encode('utf-8')))

