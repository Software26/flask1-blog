from flask import Flask

def create_app():
    
    app= Flask(__name__)
    
    app.config.from_object('config.Config')
    
    from blogFlask import home
    app.register_blueprint(home.bp)
    
    
    from blogFlask import auth
    app.register_blueprint(auth.bp)
    
    from blogFlask import post
    app.register_blueprint(post.bp)
    
    return app
