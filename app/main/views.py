from flask import render_template
from ..request import get_quote
from . import main


@main.route('/')
def home():
    '''
    Homepage route
    '''
    quote = get_quote()
    return render_template('index.html', quote=quote)