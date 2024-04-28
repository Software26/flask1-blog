from flask import Blueprint, render_template, flash, redirect ,g, url_for, request

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
    if request.method == "POST":
        url = request.form.get('url')
        url = url.replace(' ','-')
        title = request.form.get('title')
        info = request.form.get('info')
        content = request.form.get('ckeditor')
        
        
        post = Post(g.user.id, url, title, info, content)
        
        error = None
        
        #comprarando url de post con los existentes
        post_url = Post.query.filter_by(url = url).first()
        if post_url == None:
            db.session.add(post)
            db.session.commit()
            flash(f"El blog {post.title} se registro correctamente")
            return redirect(url_for('post.posts'))
        else:
           error = f"El url '{url}' ya esta registrado"
        flash(error)
    return render_template("admin/create.html")

#Editar 

# button delete


@bp.route('/update/<int:id>', methods = ('GET', 'POST'))
@login_required
def update(id):
    post = Post.query.get_or_404(id)
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.info = request.form.get('info')
        post.content = request.form['ckeditor']
        db.session.commit()
        
        flash(f'El blog {post.title} se actualizo correctamente')   
        return redirect(url_for('post.posts'))
        
    return render_template("admin/update.html", post = post)

# Delete register
@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash(f'¡La blog {post.title} se a eliminado correctamente')
    return redirect(url_for('post.posts'))