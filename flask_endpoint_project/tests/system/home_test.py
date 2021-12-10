############------------ IMPORTS ------------############
from tests.system.tests_base import BaseTest
import json


############------------ FUNCTION(S) ------------############
class TestHome(BaseTest):
    def test_home(self):
        # initialize a context manager
        with app.test_client() as c:
            # makes a get request to test
            # endpoint works as expected
            response = c.get('/')

            # check that http response is ok
            # success_http_responses = [200, 201]

            # self.assertIn(
            #     response.status_code, 
            #     success_http_responses
            # )

            # alternatively, check that http response
            # is not a particular number
            fail_http_responses = [500, 429]

            self.assertNotIn(
                response.status_code,
                fail_http_responses
            )
            
            expected = {'message': 'Hello, Wolrd!'}

            self.assertEqual(
                json.loads(response.get_data()),
                expected
            )
