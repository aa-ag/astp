############------------ IMPORTS ------------############
from unittest import TestCase
from app import app
import json


############------------ FUNCTION(S) ------------############
class TestHome(TestCase):
    def test_home(self):
        # initialize a context manager
        with app.test_client() as c:
            # makes a get request to test
            # endpoint works as expected
            response = c.get('/')

            self.assertEqual(response.status_code, 200)
            
            expected = {'message': 'Hello, Wolrd!'}

            self.assertEqual(
                json.loads(response.get_data()),
                expected
            )
