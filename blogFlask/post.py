from flask import Blueprint

bp= Blueprint('post', __name__, url_prefix = '/post')


@bp.route('/posts')
def posts():
    return "pagina de posts"


@bp.route('/create')
def create():
    return "pagina de create"

@bp.route('/update')
def update():
    return "pagina de update"