# views.py
#third party import
from flask import Blueprint, render_template, current_app


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/addrecipe')
def addrecipe():
    return render_template('addrecipe.html')


@main.route('/recipes')
def recipes_page():
    recipes = current_app.recipeCrud.get_recipes()
    return render_template('recipes.html', recipes=sorted(recipes.items()))