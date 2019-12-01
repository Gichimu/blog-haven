from flask import render_template
from ..request import get_quote
from . import main
from ..models import User
from .forms import commentForm, LoginForm, RegistrationForm


@main.route('/')
def home():
    '''
    Homepage route
    '''
    form = LoginForm()
    quote = get_quote()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            
            return redirect(request.args.get('next') or url_for('home'))
        flash('Invalid username or Password')
    return render_template('index.html', quote=quote, form=form)


@main.route('/blogpost')
def blog():
    '''
    The route for a blogpost
    '''
    return render_template('blog.html')

@main.route('/register')
def register():
    '''
    The default route to register
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data, password= form.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home'))
    title = 'Create a new Account'
    return render_template('auth/register.html', form=form, title=title)

# @main.route('/blogpost/<id>/comment', methods=['GET', 'POST'])
# def comment(id):

#     form = commentForm()

#     if form.validate_on_submit():


