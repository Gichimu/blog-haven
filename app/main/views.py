from flask import render_template, redirect,url_for, flash, request
from ..request import get_quote
from .. import db
from . import main
from datetime import datetime
from sqlalchemy import desc
from flask_login import login_user, logout_user, login_required
from ..models import User, Blogpost, Comment, Vote
from ..email import mail_message
from .forms import commentForm, LoginForm, RegistrationForm, createBlog, updateBlogForm


@main.route('/', methods=['GET', 'POST'])
def home():
    '''
    Homepage route
    '''
    form = LoginForm()
    quote = get_quote()
    posts = Blogpost.query.limit(4).all()
    blogposts = Blogpost.query.order_by(desc(Blogpost.id)).all()
    user = None
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or Password')

    
    return render_template('index.html', quote=quote, form=form, posts=posts, blogposts=blogposts)


@main.route('/create/<int:user_id>', methods=['GET','POST'])
def create(user_id):

    user = User.query.filter_by(id=user_id).first()
    form = createBlog()
    if form.validate_on_submit():
        blog = Blogpost(user_id=user_id, title=form.title.data, blog_text=form.blog.data, timestamp=datetime.now())
        db.session.add(blog)
        db.session.commit()

        flash('Your blog has been created')
        return redirect(url_for('main.home'))
    title = 'Create a blog'
    return render_template('blog/create_blog.html', form=form, title=title)

@main.route('/blogpost/<int:id>')
def blog(id):
    '''
    The route for a blogpost
    '''
    like_count = None
    likes = Vote.query.filter_by(blog_id=id).first()
    if likes is not None:
        like_count = likes.upvotes - likes.downvotes
    comments = Comment.query.filter_by(blog_id=id).all()
    blog = Blogpost.query.filter_by(id=id).first()
    return render_template('blog.html', blog=blog, comments=comments, like_count=like_count)


@main.route('/register', methods=['GET', 'POST'])
def register():
    '''
    The default route to register
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password= form.password.data)

        db.session.add(user)
        db.session.commit()

        mail_message('Welcome to Blog Haven', 'email/welcome', user.email, user=user)
        flash('Your account has been created. Proceed to sign in')
        return redirect(url_for('main.home'))
    title = 'Create a new Account'
    return render_template('auth/register.html', form=form, title=title)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/blogpost/<int:id>/comment', methods=['GET', 'POST'])
def comment(id):

    form = commentForm()

    if form.validate_on_submit():
        comment = Comment(blog_id=id, comment=form.comment.data, name=form.name.data, timestamp=datetime.now())
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.blog', id=id))
    title = 'Write a comment'
    return render_template('blog/create_comment.html', form=form)

@main.route('/blogpost/<int:id>/upvote')
def upvote(id):

    vote = None
    votes = Vote.query.filter_by(blog_id=id).all()
    if votes is not None:
        vote = Vote(blog_id=id, upvote=votes.upvotes+1)

    db.session.add(vote)
    db.session.commit()

    return redirect(url_for('main.blog', id=id))


@main.route('/blogpost/<int:id>/delete')
@login_required
def delete(id):

    post = Blogpost.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('main.home'))


@main.route('/blogpost/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):

    form = updateBlogForm()
    post = Blogpost.query.filter_by(id=id).first()
    if form.validate_on_submit():
        new_post = Blogpost.query.filter_by(id=id).update({"title": form.title.data, "blog_text": form.blog.data})
        db.session.commit()
        return redirect(url_for('main.blog', id=id))
    return render_template('blog/update_blog.html', form=form)


@main.route('/blogpost/<int:id>/delete_comment')
@login_required
def delete_comment(id):

    comment = Comment.query.filter_by(blog_id=id).first()
    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for('main.blog', id=id))




