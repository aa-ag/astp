############------------ IMPORTS ------------############
from unittest import TestCase
from models.item import ItemModel


############------------ GLOBAL VARIABLE(S) ------------############
class ModelTest(TestCase):
    def test_model_name(self):
        expected = 'items'
        self.assertEqual(ItemModel.__tablename__, expected)

    def test_input_types(self):
        dummy_item = ItemModel('Test Item', 1.00)
        self.assertEqual(type(dummy_item.name), str)
        self.assertEqual(type(dummy_item.price), float)

    def test_price_precision(self):
        dummy_item = ItemModel('Test Item', 1.33)
        expected_precision = round(dummy_item.price, 2)
        self.assertEqual(dummy_item.price, expected_precision)

    def test_jsonmethod(self):
        dummy_item = ItemModel('Test Item', 1.99)
        expected_json = {'name': 'Test Item', 'price': 1.99}
        self.assertEqual(dummy_item.generate_json(), expected_json)


'''
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

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
