
# from sqlalchemy import Column, Integer, String,LargeBinary,DATETIME,Numeric
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import base64

#engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:smhh2112@localhost:3306/sqlalchemy',echo=True)


db = sqlalchemy()
ma = Marshmallow()


class User(db.Model):
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50))
    fullname = db.Column(db.String(length=50))
    nickname = db.Column(db.String(length=50))
 
    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
                            self.name, self.fullname, self.nickname)

"""

#        @hybrid_property
#       def EncHSImg(self):
#                if self.Image != None:
                        return base64.b64encode(self.Image);

#        @hybrid_property
#        def EncHS_CONFIDENCE(self):
#                return str(self.HS_CONFIDENCE)

#        @hybrid_property
#        def GetName(self):
#                return self.name


        # def __repr__(self):
        #         return '<info %r>' % self.name

"""


