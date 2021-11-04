# This file is the blueprint of our application
# It contains authentication routes/URLs for our app
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Person
from werkzeug.security import generate_password_hash, check_password_hash # These hash makes it that it is never storing the password in plain text

from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Validating if the email is in the database
        user = Person.query.filter_by(email=email).first()
        if user:
            # Comparing the database password with the password entered in the form
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            # If user does not exist:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Checking to see if the email exists
        user = Person.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')


        # Checking if the login credentials are valid
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            new_user = Person(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
        
    return render_template("signup.html", user=current_user)