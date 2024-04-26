from flask import Flask ,Blueprint, render_template, url_for, request, redirect, flash, session, g 
from werkzeug.security import generate_password_hash,check_password_hash

from .models import User
from blogFlask import db # llamada de la base de datos


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods = ("GET", "POST"))
def register():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get("password")
        email = request.form.get("email")
        
        user = User(username = username, email = email, password = generate_password_hash(password))
        
        error = None
        
        #comparando el nombre existente
        user_email = User.query.filter_by(email = email).first()
        if user_email is error: 
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
            
    return render_template("auth/register.html")

@bp.route('/login')
def login():
    return render_template("auth/login.html")

@bp.route('/profile')
def profile():
    return render_template("auth/profile.html")