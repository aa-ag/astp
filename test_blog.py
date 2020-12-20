import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    def test_create_blog(self):
        new_blog = Blog('Test title', 'Test author')

        self.assertEqual('Test title', new_blog.title)
        self.assertEqual('Test author', new_blog.author)
        self.assertListEqual([], new_blog.posts)
        # self.assertEqual(0, len(new_blog.posts)) # alternative

    def test_repr(self):
        new_blog = Blog('Test title', 'Test author')
        newer_blog = Blog('Test title 2', 'Test author 2')

        self.assertEqual(new_blog.__repr__(),
                         'Test title by Test author (0 posts)')
        self.assertEqual(newer_blog.__repr__(),
                         'Test title 2 by Test author 2 (0 posts)')

    def test_repr_multiple_posts(self):
        new_blog = Blog('Test title', 'Test author')
        new_blog.posts = ['test']

        newer_blog = Blog('Test title2', 'Test author2')
        newer_blog.posts = ['test', 'test2']

        self.assertEqual(new_blog.__repr__(),
                         'Test title by Test author (1 post)')
        self.assertEqual(newer_blog.__repr__(),
                         'Test title2 by Test author2 (2 posts)')


if __name__ == '__main__':
    unittest.main()
