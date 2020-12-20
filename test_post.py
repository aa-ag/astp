import unittest
from post import Post


class PostTest(unittest.TestCase):
    def test_create_post(self):
        new_post = Post('Test Title', 'Test Content')

        self.assertEqual('Test Title', new_post.title)
        self.assertEqual('Test Content', new_post.content)

    def test_jsonify(self):
        p = Post('Test title', 'Test content')
        expected = {'title': 'Test title', 'content': 'Test content'}
        self.assertDictEqual(expected, p.jsonify())


if __name__ == '__main__':
    unittest.main()
