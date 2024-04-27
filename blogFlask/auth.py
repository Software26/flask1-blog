from flask import Flask ,Blueprint, render_template, url_for, request, redirect, flash, session, g 
from werkzeug.security import generate_password_hash,check_password_hash

from .models import User
from blogFlask import db # llamada de la base de datos


bp = Blueprint('auth', __name__, url_prefix='/auth')


#----------------------------------------------------------------
@bp.route('/register', methods = ("GET", "POST"))
def register():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get("password")
        email = request.form.get("email")
        
        user = User(username, email, generate_password_hash(password))
        
        error = None
        
        
        #comparando el nombre existente
        user_email = User.query.filter_by(email = email).first()
        if user_email == error: 
            db.session.add(user)
            db.session.commit()
            flash('Registro exitoso. Por favor, inicia sesión.', 'success')
            return redirect(url_for('auth.login'))
        else:
            error = f'El correo electrónico {email} ya está registrado.'
        
        flash(error,'error')
            
    return render_template("auth/register.html")
#----------------------------------------------------------------
# login method
@bp.route('/login', methods = ('GET', 'POST'))
def login():
    
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        error = None
        #
        user = User.query.filter_by(email = email).first()
        
        #Condicion de seguridad
        if user == None or not check_password_hash(user.password, password): 
            error = "Correo o la contrasena es incorrecto"
        
           #Log in
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('post.posts'))
             
        flash(error)
    
    return render_template("auth/login.html")
 
 
 # mantener un usuario logiodao
@bp.before_app_request
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
#------------------------------------------------------------------------------

#---Editar perfil----


#------subir photos-----
from werkzeug.utils import secure_filename

def get_photo(id):
    user = User.query.get_or_404(id)
    photo = None
    if photo != None:
        photo = user.photo
    return photo


#-------------------------


#Edit profile
@bp.route('/profile/<int:id>', methods=("GET","POST"))
@login_required
def profile(id):
    user= User.query.get_or_404(id)
    photo = get_photo(id)
    
    if request.method == "POST":
        user.username = request.form.get("username")
        password = request.form.get("password")
        
        error = None
        if len(password) !=0:
            user.password = generate_password_hash(password)
        elif len(password) > 0 and len(password) < 6:
            error = "Contraseña demasiado corta debe de tener mas 5 caracteres"
    
    #Edit photo
        if request.files['photo']:
            photo = request.files['photo']  
            photo.save(f'blogFlask/static/media/{secure_filename(photo.filename)}')
            user.photo = f'media/{secure_filename(photo.filename)}'
            
            
        if error is not None:
            flash(error)
        else:
            db.session.commit()
            flash("Perfil actualizado exitosamente.", "success")
            return redirect(url_for('auth.profile', id=user.id))
        
        flash(error)
    
    
    return render_template("auth/profile.html", user=user, photo = photo)