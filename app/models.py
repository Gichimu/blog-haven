from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    '''
    Class that defines the default template for the quote object
    '''

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote


class User(UserMixin, db.Model):
    '''
    Class that defines the user object template
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True, index=True)
    blogposts = db.relationship('Blogpost', backref='users', lazy='dynamic')
    password_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute!')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Comment(db.Model):
    '''
    Class that defines the default template for the comment object
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogposts.id'))
    comment = db.Column(db.String())
    name = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'Comment {self.comment}'


class Blogpost(db.Model):
    '''
    Class that defines the default template for the blog object
    '''

    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255))
    photo_uri = db.Column(db.String(255))
    blog_text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='blogpost', lazy='dynamic')

    @classmethod
    def get_all_posts(cls):
        posts = cls.query.all()
        return posts



    def __repr__(self):
        return f'Blogpost {self.id}'


class Vote(db.Model):

    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'Votes {self.upvotes}'

    



