from app import app, db, allowed_file
from flask import url_for, redirect, render_template, request, jsonify, session, flash
from methods import login_user, user_logged
from form import LoginForm, RegistrationForm, ComplaintForm
from werkzeug.utils import secure_filename
import os


@app.route('/')
def home_page():
    return render_template("index.html")




# db.session.query(Complaint).delete()
# db.session.commit()
db.create_all()
