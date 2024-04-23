from flask import Blueprint

bp= Blueprint('home',__name__)

@bp.route('/')
def index():
    return "pagina de inicio"

@bp.route("/blog")
def blog():
    return "pagina de blog"
