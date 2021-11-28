from unittest import TestCase
import blog
from project.blog import Blog


class BlogTest(TestCase):
    def test_blog_creation(self):
        b = blog.Blog("sample Title", "sample Author")
        self.assertEqual("sample Title", b.title)
        self.assertEqual("sample Author", b.author)
        self.assertListEqual([], b.posts)

    def test__repr__(self):
        b1 = Blog("Test","Test Author")
        b2 = Blog("Another Test", "Another Author")
        self.assertEqual(b1.__repr__(), "Test by Test Author (0 posts).")
        self.assertEqual(b2.__repr__(), "Another Test by Another Author (0 posts).")

    def create_post(self):
        pass

    def jsonify_function(self):
        b = blog.Blog("sample Title", "sample Author", ["a blog post", "another blog post"])
        expected = {
            "title": "sample Tile",
            "author": "sample Author",
            "posts": ["a blog post", "another blog post"],
        }
        self.assertDictEqual(expected, b.json_function())
    