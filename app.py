rom models import Base, info,HS_LOG
from flask_sqlalchemy import SQLAlchemy
import base64
import json
from flask_marshmallow import Marshmallow


app = Flask(__name__)
db = SQLAlchemy(app)

ma=Marshmallow(app)
@app.template_filter()
def b64encode(s):
    return base64.b64encode(s)

app.jinja_env.filters['b64encode'] = b64encode



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


