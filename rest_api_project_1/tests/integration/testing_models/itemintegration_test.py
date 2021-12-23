############------------ IMPORTS ------------############
from models.item import ItemModel
from tests.base_test import BaseTest


############------------ TEST(S) ------------############
class ItemTest(BaseTest):
    def test_crud(self):
        # generate context / all reqs
        with self.app_context():
            # create a test item in doc/db
            item = ItemModel('Test', 9.99)

            # make sure it doesn't already exist
            self.assertIsNone(
                    ItemModel.find_by_name('Test'),
                    f"Error: did find an item \"{item.name}\""
                )

            # save it to the db if it doesn't
            try:
                item.save_to_db()
            except:
                print("something went wrong; could not save item to the db")

            # assert that it does exist in the db after creating it
            self.assertIsNotNone(
                    ItemModel.find_by_name('Test'),
                    f"Error: found item \"{item.name}\" in the database"
                )

            # delete the test item we just created
            try:
                item.delete_from_db()
            except:
                print("something went wrong; could not delete item to the db")

            # check that item was deleted
            self.assertIsNone(
                    ItemModel.find_by_name('Test'),
                    f"Error: did find an item \"{item.name}\""
                )
