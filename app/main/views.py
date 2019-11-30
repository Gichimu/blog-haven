from flask import render_template
from ..request import get_quote
from . import main
from .forms import commentForm


@main.route('/')
def home():
    '''
    Homepage route
    '''
    quote = get_quote()
    return render_template('index.html', quote=quote)


@main.route('/blogpost')
def blog():
    '''
    The route for a blogpost
    '''
    return render_template('blog.html')

@main.route('/blogpost/<id>/comment', methods=['GET', 'POST'])
def comment(id):

    form = commentForm()

    if form.validate_on_submit():
        

