from flask import flash
from flask import Blueprint, render_template, redirect, request, url_for
from .website import db
from .website.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                login_user(user, remember=True)
                
                return render_template("home.html")
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Username is incorrect.', category='error')
            
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        username_exists = User.query.filter_by(username=username).first()
        if username_exists:
            flash('Email is already in use.', category='error')
        elif len(password) < 4:
            flash('Password too short', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))
    
    return render_template("register.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))