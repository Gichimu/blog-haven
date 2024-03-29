from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class commentForm(FlaskForm):
    name = TextField('Your name', validators=[Required()])
    comment = TextAreaField('Enter your comment...', validators=[Required()])
    submit = SubmitField('Submit')

class createBlog(FlaskForm):
    title = TextField('Title (255 characters maximum)', validators=[Required()])
    blog = TextAreaField('Enter your text here ...', render_kw={'class': 'form-control', 'rows': 10}, validators=[Required()])
    submit = SubmitField('Submit')

class updateBlogForm(FlaskForm):
    title = TextField('Title (255 characters maximum)', validators=[Required()])
    blog = TextAreaField('Enter your text here ...', render_kw={'class': 'form-control', 'rows': 10}, validators=[Required()])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    username = StringField('Enter your username', validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    password_confirm = PasswordField('Confirm passwords', validators=[Required()])
    submit = SubmitField('Sign up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email!')

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_user(cls):
        user = db.query.filter_by(username = cls.username).first()
        db.session.delete(user)

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken!')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')