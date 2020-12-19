from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        new_post = Post('Test Title', 'Test Content')

        self.assertEqual('Test Title', new_post.title)
        self.assertEqual('Test Content', new_post.content)
