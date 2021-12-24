from models.store import StoreModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test')
        expected = 'test'
        self.assertEqual(
                store.name, 
                expected,
                'Error: name of store after creation does not match expected value'
            )