from flask import render_template
from . import main


@main.route('/')
def home():
    '''
    Homepage route
    '''

    return render_template('index.html')