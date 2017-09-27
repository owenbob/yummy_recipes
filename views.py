# views.py
#third party import
from flask import Blueprint, render_template, current_app, request, redirect, url_for


#local import
from recipe import Recipe

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

@main.route('/recipe/<int:recipe_id>')
def recipe_page(recipe_id):
    recipe = current_app.recipeCrud.get_recipe(recipe_id)
    return render_template('recipe.html', recipe=recipe)

@main.route('/recipes/add', methods=['GET', 'POST'])
def recipe_add_page():
    if request.method == 'GET':
        return render_template('recipe_edit.html')
    else:
        title = request.form['title']
        ingridient = request.form['ingridient']
        desc = request.form['desc']
        recipe = Recipe(title, ingridient, desc)
        current_app.recipeCrud.add_recipe(recipe)
        return redirect(url_for('main.recipe_page', movie_id=movie._id))
