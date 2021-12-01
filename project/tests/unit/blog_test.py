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
        b3 = Blog("this is a title", "aLberT eInStEiN")

        self.assertEqual(b1.__repr__(), "Test by Test Author (0 posts).")
        self.assertEqual(b2.__repr__(), "Another Test by Another Author (0 posts).")
        self.assertEqual(b3.__repr__(), "this is a title by aLberT eInStEiN (0 posts).")

    def test_repr_multiple_posts(self):
        b1 = Blog("Blog title", "Blog author")
        b1.posts = ["this is a post", "this is another post", "this is a third post"]

        b2 = Blog("Another blog title", "Another blog author")
        b2.posts = []

        self.assertEqual(b1.__repr__(), "Blog title by Blog author (3 posts).")
        self.assertEqual(b2.__repr__(), "Another blog title by Another blog author (0 posts).")

    def jsonify_function(self):
        b = blog.Blog("sample Title", "sample Author", ["a blog post", "another blog post"])
        expected = {
            "title": "sample Tile",
            "author": "sample Author",
            "posts": ["a blog post", "another blog post"],
        }
        self.assertDictEqual(expected, b.json_function())

    def test_create_post_in_post(self):
        b = blog.Blog("sample Title", "sample Title", ["a blog post", "another blog post"])
        b.create_post("Test Post", "Test Content")

        self.assertEqual(len(b.posts), 1)
        
    