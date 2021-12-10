############------------ IMPORTS ------------############
from unittest import TestCase
from app import app

############------------ GLOBAL VARIABLE(S) ------------############
class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client

############------------ FUNCTION(S) ------------############


############------------ DRIVER CODE ------------############
