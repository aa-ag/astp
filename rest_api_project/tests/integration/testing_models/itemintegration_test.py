############------------ IMPORTS ------------############
from tests.base_test import BaseTest
from models.item import ItemModel


############------------ TEST(S) ------------############
class ItemTest(BaseTest):
    def test_crud(self):
        # generate context / all reqs
        with self.app_context():
            # create a test item in doc/db
            item = ItemModel('Test', 9.99)

            # make sure it doesn't already exist
            self.assertIsNone(ItemModel.find_by_name('Test'))

            # save it to the db if it doesn't
            item.save_to_db()

            # assert that it does exist in the db after creating it
            self.assertIsNotNone(ItemModel.find_by_name('Test'))
