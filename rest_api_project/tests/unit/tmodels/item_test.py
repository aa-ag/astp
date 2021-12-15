############------------ IMPORTS ------------############
from unittest import TestCase
from models.item import ItemModel


############------------ GLOBAL VARIABLE(S) ------------############
class ModelTest(TestCase):
    def test_create_item(self):
        test_item = ItemModel('Test Item', 9.99)
        self.assertEqual(
            test_item.name, 
            'Test Item',
            'Item\'s name not equal to constructor argument.'
        )
        self.assertEqual(
            test_item.price, 
            9.99,
            'Item\'s price not equal to constructor argument.'
        )


    def test_model_name(self):
        '''
         tests that ItemModel's table name is what's expected
        '''
        expected = 'items'
        self.assertEqual(ItemModel.__tablename__, expected)


    def test_input_types(self):
        '''
         ItemModel takes two inputs: name & price.
         this test tests that ItemModel's inputs are in the
         expected type: string for name and float for price
        '''
        dummy_item = ItemModel('Test Item', 1.00)
        self.assertEqual(type(dummy_item.name), str)
        self.assertEqual(type(dummy_item.price), float)


    def test_price_decimals(self):
        '''
         ItemModel's price input expects a floating point value with two places
        '''
        dummy_item = ItemModel('Test Item', 1.33)
        expected_precision = round(dummy_item.price, 2)
        self.assertEqual(dummy_item.price, expected_precision)


    def test_generate_json(self):
        '''
         tests ItemModel's generate_json method
        '''
        dummy_item = ItemModel('Test Item', 1.99)
        expected_json = {'name': 'Test Item', 'price': 1.99}
        self.assertEqual(dummy_item.generate_json(), expected_json)


'''
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
'''
