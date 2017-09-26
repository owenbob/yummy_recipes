# third party import
import unittest


# local import
from object_oriented.recipe import Recipe


class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        self.recipe_coffee = Recipe(title="africanCoffee", ingridient="water coffee", desc="pour water")

    def test_title(self):
        self.assertEqual(self.recipe_coffee.title, "africanCoffee", msg="we have africanCoffee")

    def test_ingridient(self):
        self.assertTrue(self.recipe_coffee.ingridient, "water coffee")

    def test_desc(self):
        self.assertEqual(self.recipe_coffee.desc, "pour water", msg="ae have description")