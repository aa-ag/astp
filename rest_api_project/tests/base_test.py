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
        pass

    def tearDown(self):
        pass
