############------------ IMPORTS ------------############
from unittest import TestCase
from unittest import mock
from unittest.mock import patch
import app
from project.blog import Blog
from project.post import Post

############------------ GLOBAL VARIABLE(S) ------------############


############------------ CLASS(ES) ------------############
class AppTest(TestCase):
    # def test_menu_prints_prompt(self):
    #     with patch('builtins.input') as mocked_input:
    #         app.menu()
    #         mocked_input.assert_called_with(app.MENU_PROMPT)
    

    def test_menu_calls_print_blogs(self):
        with patch('app.list_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()
    

    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.list_blogs()
            mocked_print.assert_called_with("Test by Test Author (0 posts).")


    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('This is a fake Title', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs['This is a fake Title'])


    def test_ask_read_blog(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(b)


    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test Post','Test Content')
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])


    def test_print_post(self):
        post = Post('Post Title', 'Post content')
        expected_print = 'Post Title... Post content'

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)


    def test_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')



############------------ DRIVER CODE ------------############
