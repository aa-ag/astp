from unittest import TestCase
import blog
from project.blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_post(self):
        b = blog.Blog("sample Title", "sample Title")
        b.create_post("Test Post", "Test Content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test Content")

    def test_json(self):
        pass
    