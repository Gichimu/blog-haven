from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User
from ..request import get_quote


@auth.route('/login')
def login():
    '''
    Default route for the login page
    '''
    form = LoginForm()
    quote = get_quote()
    if form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or Password')
    
    return redirect(url_for('main.home', quote=quote, form = form))