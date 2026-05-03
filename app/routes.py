from flask import Blueprint, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError

from . import db
from .models import Note

bp = Blueprint("note", __name__, url_prefix="/note")


@bp.route("/")
def index():

    notes = Note.query.all()
    return render_template("note/index.html", notes=notes)


@bp.route("/add", methods=("POST", "GET"))
def add_post():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required!"
        elif not body:
            error = "Body is require!"
        if error is None:
            try:
                new_note = Note(title=title, body=body)
                db.session.add(new_note)
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                error = "Note is alread there"
            else:
                return redirect(url_for("note.index"))
        flash(error)
    return render_template("note/add.html")

@bp.route("/update/<int:id>", methods=("GET", "POST"))
def update_note(id):
    
    note = Note.query.get_or_404(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required!"
        elif not body:
            error = "Body is require!"
        if error is None:
            note.title = title 
            note.body = body
            db.session.commit()
            return redirect(url_for("note.index"))
        flash(error)
    return render_template("note/update.html", note=note)



@bp.route("/delete/<int:id>", methods=("POST",))
def delete(id):
    note = Note.query.get_or_404(id)
    
    db.session.delete(note)
    
    db.session.commit()
    
    return redirect(url_for("note.index"))
