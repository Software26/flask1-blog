from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 




# esto es para crear la instacia para cre
db = SQLAlchemy()

def create_app():
    
    app= Flask(__name__)
    
    app.config.from_object('config.Config')
    
     #inicializar la base de datos
    db.init_app(app) 
    
    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)
    
    import locale 
    locale.setlocale(locale.LC_ALL, 'es_ES')
    
    
    from blogFlask import home
    app.register_blueprint(home.bp)
    
    
    from blogFlask import auth
    app.register_blueprint(auth.bp)
    
    from blogFlask import post
    app.register_blueprint(post.bp)
     
    from .models import User, Post
     
    with app.app_context():
        db.create_all()
    return app
