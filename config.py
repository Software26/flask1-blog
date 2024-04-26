
SQLITE = 'sqlite:///blogflask.db'
POSTGREESQL = 'postgresql+psycopg2://postgres:123456@localhost:5432/blogpost_db'
POSTGREESQL1 = 'postgresql://scott:tiger@localhost/project'
class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = POSTGREESQL