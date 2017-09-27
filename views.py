# views.py
#third party import
from flask import Blueprint, render_template, current_app, request, redirect, url_for

main = Blueprint('main', __name__)


#local import
from recipe import Recipe
from forms import RecipeEditForm
#from initial import main


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/recipes', methods=['GET', 'POST'])
def recipes_page():
    if request.method == 'GET':
        recipes = current_app.recipeCrud.get_recipes()
        return render_template('recipes.html', recipes=sorted(recipes.items()))
    else:
        recipe_ids = request.form.getlist('recipe_ids')
        for recipe_id in recipe_ids:
            current_app.recipeCrud.delete_recipe(int(recipe_id))
        return redirect(url_for('main.recipes_page'))

@main.route('/recipe/<int:recipe_id>')
def recipe_page(recipe_id):
    recipe = current_app.recipeCrud.get_recipe(recipe_id)
    return render_template('recipe.html', recipe=recipe)

@main.route('/recipes/add', methods=['GET', 'POST'])
def recipe_add_page():
    form = RecipeEditForm()
    if form.validate_on_submit():
        title = form.data['title']
        ingridient = form.data['ingridient']
        desc = form.data['desc']

        recipe = Recipe(title, ingridient, desc)

        current_app.recipeCrud.add_recipe(recipe)
        return redirect(url_for('main.recipe_page', recipe_id=recipe._id))
    return render_template('recipe_edit.html', form=form)

@main.route('/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
def recipe_edit_page(recipe_id):
    recipe = current_app.recipeCrud.get_recipe(recipe_id)
    form = RecipeEditForm()
    if form.validate_on_submit():
        recipe.title = form.data['title']
        recipe.ingridient = form.data['ingridient']
        recipe.desc = form.data['desc']

        current_app.recipeCrud.update_recipe(recipe)
        return redirect(url_for('main.recipe_page', recipe_id=recipe._id))
    form.title.data = recipe.title
    form.ingridient.data = recipe.ingridient
    form.desc.data = recipe.desc
    return render_template('recipe_edit.html', form=form)