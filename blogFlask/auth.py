from flask import Blueprint

bp= Blueprint('auth',__name__,url_prefix = '/auth')


@bp.route('/register')
def register():
    return "pagina de register"


@bp.route('/login')
def login():
    return "pagina de Login"

@bp.route('/profile')
def profile():
    return "pagina de profile"