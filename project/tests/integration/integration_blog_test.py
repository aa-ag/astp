from unittest import TestCase
import blog
from project.blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        '''
         tests creating a post in a blog
        '''
        b = blog.Blog("sample Title", "sample Author")
        b.create_post("Test Post", "Test Content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test Content")

    def test_json_without_posts(self):
        '''
         tests json_function from blog.py's Blog class,
         with no posts
        '''
        b = blog.Blog("sample Title", "sample Author")
        expected = {
            'title': "sample Title",
            'author': "sample Author",
            'posts': list(),
        }

        self.assertEqual(expected, b.json_function())

    def test_json(self):
        b = blog.Blog("sample Title", "sample Author")
        b.create_post("Test Post", "Test Content")

        expected = {
            'title': "sample Title",
            'author': "sample Author",
            'posts': [{"title": "Test Post", "content": "Test Content"}],
        }

        self.assertEqual(expected, b.json_function())