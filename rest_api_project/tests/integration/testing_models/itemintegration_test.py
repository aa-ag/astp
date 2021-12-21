############------------ IMPORTS ------------############
from tests.base_test import BaseTest
from models.item import ItemModel


############------------ TEST(S) ------------############
class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('Test', 9.99)

            self.assertIsNone(ItemModel.find_by_name('Test'))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Test'))
