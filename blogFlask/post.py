from flask import Blueprint, render_template

bp= Blueprint('post', __name__, url_prefix = '/post')


@bp.route('/posts')
def posts():
    return render_template("admin/posts.html")


@bp.route('/create')
def create():
    return render_template("admin/create.html")

@bp.route('/update')
def update():
    return render_template("admin/update.html")