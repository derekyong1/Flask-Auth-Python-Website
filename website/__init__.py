from flask import Flask
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

def create_app():
    app = Flask(__name__)

    # Creating secret key for app to encrypt and secure the cookies.
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    return app