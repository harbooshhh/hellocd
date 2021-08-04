
from flask import Flask
from Model import User

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from Model import db
    db.init_app(app)
    jwk_user = User(name='jesper', fullname='Jesper Wisborg Krogh', nickname='🐬')
    db.session.add(jwk_user)
    db.session.commit()

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
