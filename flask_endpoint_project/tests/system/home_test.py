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

            possible_http_responses = [200, 201]

            self.assertIn(
                response.status_code, 
                possible_http_responses
            )
            
            expected = {'message': 'Hello, Wolrd!'}

            self.assertEqual(
                json.loads(response.get_data()),
                expected
            )
