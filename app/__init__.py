from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    login_manager.init_app(app)

    from app.routes import bp, office_bp
    app.register_blueprint(bp)
    app.register_blueprint(office_bp)

    return app
