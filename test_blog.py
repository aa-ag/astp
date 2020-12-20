import unittest
from blog import Blog


# UNITTESTS

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

# INTEGREATION TESTS
    def test_create_post_in_blog(self):
        b = Blog('Test title', 'Test author')
        b.create_post('Test post', 'Test content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test post')
        self.assertEqual(b.posts[0].content, 'Test content')

    def test_json(self):
        b = Blog('Test', 'Test author')
        b.create_post('Test post', 'Test content')

        expected = {
            'title': 'Test',
            'author': 'Test author',
            'posts': [{
                'title': 'Test post',
                'content': 'Test content'
            }]
        }

        self.assertDictEqual(expected, b.json())


if __name__ == '__main__':
    unittest.main()
