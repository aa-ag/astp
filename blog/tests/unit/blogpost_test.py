from unittest import TestCase
import post


class PostTest(TestCase):
    def test_create_post(self):
        '''
         creates an object and compares that properties match
        '''
        p = post.Post("Example title", "Lorem ipsum... (example content).")
        self.assertEqual("testing wrong title", p.title)
        self.assertEqual("Lorem ipsum... (example content).", p.content)