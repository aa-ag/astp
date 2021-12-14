############------------ IMPORTS ------------############
from unittest import TestCase
from models.item import ItemModel


############------------ GLOBAL VARIABLE(S) ------------############
class ModelTest(TestCase):
    def test_model_name(self):
        expected = 'items'
        self.assertEqual(ItemModel.__tablename__, expected)


############------------ FUNCTION(S) ------------############


############------------ DRIVER CODE ------------############
