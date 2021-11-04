from flask import Flask
import os
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv



load_dotenv(find_dotenv())

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    # Creating secret key for app to encrypt and secure the cookies.
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Setting SQLAchemy database location 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Taking the database and telling the app that we are using this database
    db.init_app(app)

    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Person, Note

    create_database(app)

    # Defining a login manager for the app
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Person.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)