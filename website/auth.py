# This file is the blueprint of our application
# It contains authentication routes/URLs for our app
from flask import Blueprint, render_template, request, flash

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
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Checking if the login credentials are valid
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            flash('Account created!', category='success')
            pass
        
    return render_template("signup.html")