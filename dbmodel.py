
from sqlalchemy import Column, Integer, String,LargeBinary,DATETIME,Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import base64

Base=declarative_base()

class info(Base):
        __tablename__ = 'info'
        id=Column(Integer,autoincrement=True,primary_key=True)
        name=Column(String(200))
        desc1=Column(String(500))
        Image=Column(LargeBinary)

        def __init__(self,name=None,desc1=None,img=None):
                self.name=name
                self.desc1=desc1
                self.Image=img

        @hybrid_property
        def EncImg(self):
                return base64.b64encode(self.Image)

        @hybrid_property
        def GetName(self):
                return self.name


class HS_LOG(Base):
        __tablename__ = 'HS_LOG'
        id=Column(Integer,autoincrement=True,primary_key=True)
        R_PERSON=Column(String(100))
        HS_CAMERA=Column(Integer)
        HS_CONFIDENCE=Column (Numeric(4, 2))
        HS_TIME=Column(DATETIME)
        Image=Column(LargeBinary)

        # id INTEGER NOT NULL, 
        # "R_PERSON" VARCHAR(100), 
        # "HS_CAMERA" INTEGER, 
        # "HS_CONFIDENCE" NUMERIC(4, 2), 
        # "HS_TIME" DATETIME, 
        # "Image" BLOB, 
        # PRIMARY KEY (id)


        def __init__(self,R_PERSON=None,HS_CAMERA=None,HS_CONFIDENCE=None,HS_TIME=None,Image=None):
                self.R_PERSON=R_PERSON
                self.HS_CAMERA=HS_CAMERA
                self.HS_CONFIDENCE=HS_CONFIDENCE
                self.HS_TIME=HS_TIME
                self.Image=Image

        @hybrid_property
        def EncHSImg(self):
                if self.Image != None:
                        return base64.b64encode(self.Image);

        @hybrid_property
        def EncHS_CONFIDENCE(self):
                return str(self.HS_CONFIDENCE)

        @hybrid_property
        def GetName(self):
                return self.name


        # def __repr__(self):
        #         return '<info %r>' % self.name




