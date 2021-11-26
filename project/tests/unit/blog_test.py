from unittest import TestCase
import blog

print(blog.Blog)
class BlogTest(TestCase):
    def test_blog_creation(self):
        b = blog.Blog("sample Title", "sample Author")
        self.assertEqual("sample Title", b.title)
        self.assertEqual("sample Author", b.author)
        self.assertListEqual([], b.posts)