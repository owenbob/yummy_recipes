# views.py
#third party import
from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/recipes')
def movies_page():
    return render_template('recipes.html')