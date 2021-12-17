############------------ IMPORTS ------------############
from unittest import TestCase
from app import app
from db import db


############------------ CLASS(ES) ------------############
class BaseTets(TestCase):
    def setUp(self):
        # to ensure a db exists,
        # it setUp creates one
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()

        # get test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        pass
