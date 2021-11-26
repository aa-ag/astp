from unittest import TestCase
import blog


class BlogTest(TestCase):
    def test_blog_creation(self):
        b = blog.Blog("sample Title", "sample Author")
        self.assertEqual("sample Title", b.title)
        self.assertEqual("sample Author", b.author)
        self.assertListEqual([], b.posts)

    def __repr__(self):
        return f"Blog {self.title} with articles by {self.author}, created."

    