# third party import
import unittest

# local import
from object_oriented.recipeCrud import RecipeCrud


class RecipeCrudTestCase(unittest.TestCase):
    def setUp(self):
        self.recipe = RecipeCrud()

    def test_recipeCrud_initialization(self):
        self.assertEqual(self.recipe.last_recipe_id, 0, msg="initial value of last inserted id not correct")
        self.assertIsInstance(self.recipe.recipes, dict, msg="recipes is not a dictionary")

    def test_add_recipe(self):
        self.recipe.add_recipe("coffee")
        self.assertEqual(self.recipe.last_recipe_id, 1, msg="recipe id not correct")

    def test_delete_recipe(self):
        self.recipe.add_recipe("coffee")
        self.recipe.delete_recipe(1)
        self.assertEqual(self.recipe.last_recipe_id, 1, msg="recipe not deleted")

    def test_get_recipe(self):
        self.recipe.add_recipe("french fries")
        self.recipe.get_recipe(1)
        self.assertEqual(self.recipe.last_recipe_id, 1, msg="recipe got successfully")

    def test_get_recipes(self):
        self.recipe.add_recipe('germany sandwich')
        self.recipe.add_recipe('swedish beef')
        self.recipe.get_recipes()
        self.assertEqual(self.recipe.recipes, {1:"germany sandwich", 2:"swedish beef"}, msg='we got sandwich')
        

