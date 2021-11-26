from unittest import TestCase
import blog


class BlogTest(TestCase):
    def test_blog_creation(self):
        b = blog.Blog("sample Title", "sample Author")
        self.assertEqual("sample Title", b.title)
        self.assertEqual("sample Author", b.author)
        self.assertListEqual([], b.posts)

    def __repr__(self):
        pass

    def create_post(self, title, content):
        pass

    def jsonify_function(self):
        pass