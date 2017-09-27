# manage.py 
# third party import
from flask import Flask


#local import
from views import main
from recipe import Recipe
from recipeCrud import RecipeCrud

# Define an Application factory
def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(main)

    app.recipeCrud = RecipeCrud()
    #app.recipeCrud.add_recipe(Recipe('Chicken Stew', 'water, chicken, tomatoes', 'you put three'))
    #app.recipeCrud.add_recipe(Recipe('African yams', 'water, yams','peel the yams and boil in water'))

    return app


def main_point():
    app = create_app()
    debug = app.config['DEBUG']
    app.run(debug=True)


if __name__ == '__main__':
    main_point()