from flask_wtf import FlaskForm, 
from wtforms import TextAreaField, TextField, SubmitField
from wtforms.validators import Required


class commentForm(FlaskForm):
    comment = TextAreaField('Enter your comment...', validators=[Required()])
    name = TextField('Your name...', validators=[Required()])
    email = TextField('Your email...', validators=[Required()])
    submit = SubmitField('Submit')