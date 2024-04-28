from flask import Blueprint, render_template, flash, redirect ,g, url_for

from .auth import login_required
from .models import Post
from blogFlask import db


bp= Blueprint('post', __name__, url_prefix = '/post')

@bp.route('/posts')
@login_required
def posts():
    posts = Post.query.all()#list posts
    return render_template("admin/posts.html",posts = posts)


@bp.route('/create', methods=("GET","POST"))
@login_required
def create():
    return render_template("admin/create.html")

@bp.route('/update')
@login_required
def update():
    return render_template("admin/update.html")