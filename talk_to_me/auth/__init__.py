from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, logout_user, login_user, login_required

from talk_to_me.models import User
from talk_to_me import db, lm

auth_bp = Blueprint('auth_bp', __name__, static_folder='static', static_url_path='/auth_bp/static/', template_folder='templates')

@auth_bp.route('/signup/', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
        newUser = User(username=request.form['username'])
        db.session.add(newUser)
        db.session.commit()

    return render_template('auth/signup.html')


@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()

        if user:
            login_user(user)

            return redirect(url_for('chat_bp.home'))

    return render_template('auth/login.html')


@auth_bp.route('/logout/', methods=['GET'])
def logout():
    return 'LOGOUT'