from flask import render_template,request,redirect,url_for,abort
from ..models import User
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db
from app.models import Blog,Comment
from ..requests import get_quotes

@main.route('/')
def index():
    quotes = get_quotes()
    print(quotes)
    my_blogs = Blog.query.all()
    print(my_blogs)
    return render_template ('index.html',quotes=quotes,my_blogs=my_blogs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html",user=user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/blog',methods=['GET','POST'])
@login_required
def write_blog():
    form1 = BlogForm()
    if form1.validate_on_submit():
        user_id = current_user._get_current_object().id
        blog = Blog(blog =form1.blog.data,user_id=user_id,author= form1.author.data)
        blog.save_blog() 
        return redirect(url_for('main.index'))
    return render_template('blog.html',form1=form1)

@main.route('/comment/<int:blog_id>',methods=['GET','POST']) 
@login_required
def blog_comment(blog_id):
    form2 = CommentForm() 
    comment = Comment.query.filter_by(blog_id=blog_id).all() 
    if form2.validate_on_submit():
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        comment = Comment(comment=form2.comment.data,user_id=user_id,blog_id=blog_id) 
        comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('comment.html',form2=form2,comment=comment)
