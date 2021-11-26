from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_blog_creation(self):
        b = Blog("sample Title", "sample Author")
        self.assertEqual("sample Title", b.title)
        self.assertEqual("sample Author", b.author)
        self.assertListEqual([], b.posts)