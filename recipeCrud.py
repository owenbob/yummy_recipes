"""
    This anonymous class contains methods to perform CRUD
    on the recipe
"""


class RecipeCrud:
    def __init__(self):
        self.recipes = {}
        self.last_recipe_id = 0

    def add_recipe(self, recipe):
        self.last_recipe_id += 1
        self.recipes[self.last_recipe_id] = recipe
        recipe._id = self.last_recipe_id

    def update_recipe(self, recipe):
        self.recipes[recipe._id] = recipe

    def delete_recipe(self, recipe_id):
        del self.recipes[recipe_id]

    def get_recipe(self, recipe_id):
        return self.recipes[recipe_id]

    def get_recipes(self):
        return self.recipes