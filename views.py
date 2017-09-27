# views.py
#third party import
from flask import Blueprint, render_template, current_app, request, redirect, url_for


#local import
from recipe import Recipe
from validator import validate_recipe_data

main = Blueprint('main', __name__)


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
    if request.method == 'GET':
        form = {'title':'', 'ingridient':'', 'desc': ''}
        
    else:
        valid = validate_recipe_data(request.form)
        if valid:
            title = request.form['title']
            ingridient = request.form['ingridient']
            desc = request.form['desc']
            recipe = Recipe(title, ingridient, desc)
            current_app.recipeCrud.add_recipe(recipe)
            return redirect(url_for('main.recipe_page', recipe_id=recipe._id))
        form = request.form
    return render_template('recipe_edit.html', form=form)

@main.route('/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
def recipe_edit_page(recipe_id):
    recipe = current_app.recipeCrud.get_recipe(recipe_id)
    if request.method == 'GET':
        form = {'title':recipe.title,
                'ingridient': recipe.ingridient,
                'desc': recipe.desc
        }

    else:
        valid = validate_recipe_data(request.form)
        if valid:
            recipe.title = request.form['title']
            recipe.ingridient = request.form['ingridient']
            recipe.desc = request.form['desc']
            current_app.recipeCrud.update_recipe(recipe)
            return redirect(url_for('main.recipe_page', recipe_id=recipe._id))
        form = request.form
    return render_template('recipe_edt.html', form=form)