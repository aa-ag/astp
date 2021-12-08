############------------ IMPORTS ------------############
from unittest import TestCase
import post


############------------ CLASS(ES) ------------############
class PostTest(TestCase):
    def test_create_post(self):
        '''
         creates an object and compares that properties match
        '''
        p = post.Post("Example title", "Lorem ipsum... (example content).")
        self.assertEqual("Example title", p.title)
        self.assertEqual("Lorem ipsum... (example content).", p.content)

    def test_json_function(self):
        '''
         creates and object and compares with an expected json function
         testing both creation, components & type
        '''
        p = post.Post("Example title", "Lorem ipsum... (example content).")
        expected = {"title": "Example title", "content": "Lorem ipsum... (example content)."}
        self.assertDictEqual(expected, p.json_function())


############------------ DRIVER CODE ------------############