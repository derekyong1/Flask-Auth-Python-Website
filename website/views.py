# This file is the blueprint of our application
# It contains routes/URLs for our app
from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


