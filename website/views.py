# This file is the blueprint of our application
# It contains routes/URLs for our app
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        data = request.form.get('note')

        if len(data) < 1:
            flash("Note is too short", category='error')
        else:
            new_note = Note(data=data, person_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note is successfully saved", category='success')


    return render_template("home.html", user=current_user)

# As the note is not in a form, so we cannot fetch it with request.method
# We need to use JSON to fetch it
@views.route('/delete-note', methods=['POST'])
def delete_note():

    # note is loaded as a json so a python dictionary
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        # checking if the note belongs to the current user logged in
        if note.person_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


