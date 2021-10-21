# This file is the blueprint of our application
# It contains authentication routes/URLs for our app
from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 

@auth.route('/logout')
def logout():
    return 

@auth.route('/signup')
def signup():
    return 