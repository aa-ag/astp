from unittest import TestCase
from blog.post import Post
from post import Post as post_class

class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Example title", "Lorem ipsum... (example content).")
        self.assertEqual("Example title", p.title)

