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
    def __init__(self, username, email, password,photo= None):
        self.username = username
        self.email = email
        self.password = password
        self.set_password(password)
        self.photo = photo
    
    def __repr__(self):
        return f"User: '{self.username}'"
    
from datetime import datetime # creacion de tiempo de blog
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False )  ##
    url = db.Column(db.String(100), unique = True, nullable=False)
    title= db.Column(db.String(100), nullable=False)
    info = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    ####constructor####
    def __init__(self,author, url, title, info, content,) -> None:
        self.author = author
        self.url = url
        self.title = title
        self.info = info
        self.content = content
        
    def __repr__(self):
        return f"Post: ('{self.title}') by {self.author})"