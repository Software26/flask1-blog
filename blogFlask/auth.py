from flask import Flask ,Blueprint, render_template, url_for, request, redirect, flash, session, g 
from werkzeug.security import generate_password_hash,check_password_hash

from .models import User
from blogFlask import db # llamada de la base de datos


bp = Blueprint('auth', __name__, url_prefix='/auth')
###############################################################################################
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
            flash('Registro exitoso. Por favor, inicia sesión.', 'success')
            return redirect(url_for('auth.login'))
        else:
            error = f'El correo electrónico {email} ya está registrado.'
        
        flash(error, 'error')
            
    return render_template("auth/register.html")
#############################################################################################################

@bp.route('/login', methods = ('GET', 'POST'))
def login():
    
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        error = None
        #
        user = User.query.filter_by(email = email).first()
        
        #Condicion de seguridad
        if user is None or not check_password_hash(user.password, password): 
            error = "Correo o la contrasena es incorrecto"
        
           #Log in
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('post.posts'))
             
        flash(error)
    
    return render_template("auth/login.html")
 
 
 # mantener un usuario logiodao
bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
     
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)
        
        
#Exit session
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))


#requerir iniciar session

import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@bp.route('/profile')
def profile():
    return render_template("auth/profile.html")