from blogFlask import db

######## Creando la tabla users ########
class User(db.Model):
    __tablename__ = "users" # cabiar el name de la table a users en minuscula
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))
    
####### constructor ########################
    def __init__(self, username, email, password,photo= None,id):
        self.username = username
        self.email = email
        self.password = password
        self.set_password(password)
        self.photo = photo
    
    def __repr__(self):
        return f"<User '{self.username}>'"
    
from datetime import datetime # creacion de tiempo de blog
class Post(db.Model):
    __table__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, db.models.ForeignKey("users.id"), nullable=False )  ##
    title= db.Column(db.String(100), nullable=False)
    contenido = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.titulo}')"