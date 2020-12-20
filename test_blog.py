import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    def test_create_blog(self):
        new_blog = Blog('Test title', 'Test author')

        self.assertEqual('Test title', new_blog.title)
        self.assertEqual('Test author', new_blog.author)
        self.assertListEqual([], new_blog.posts)
        # self.assertEqual(0, len(new_blog.posts)) # alternative
