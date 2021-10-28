# This file is the blueprint of our application
# It contains authentication routes/URLs for our app
from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form.get()
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return 

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    return render_template("signup.html")