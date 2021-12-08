############------------ IMPORTS ------------############
from unittest import TestCase
from unittest import mock
from unittest.mock import patch
import app
from project.blog import Blog
from project.post import Post

### wherever docstring isn't provided is from class


############------------ CLASS(ES) ------------############
class AppTest(TestCase):
    # def test_menu_prints_prompt(self):
    #     with patch('builtins.input') as mocked_input:
    #         app.menu()
    #         mocked_input.assert_called_with(app.MENU_PROMPT)
    def setUp(self):
        blog = Blog('Test Blog Title', 'Test Blog Author')
        app.blogs = {'Test Blog Title': blog}

    def test_c(self):
        '''
         mocks input to menu, then mocks input of `b`,
         blog title, blog's author and then `q` to quit;
         tests if `ask_create_blog` is called when user inputs `b`
        '''
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_c:
                mocked_input.side_effect = (
                    'b', 
                    'Test Blog Title', 
                    'Test Blog Author', 
                    'q'
                )

                app.menu()

                mocked_c.assert_called()

    def test_l(self):
        '''
         mocks input to menu, then mocks input of `l` and then `q` to quit;
         tests if `list_blogs` is called when user inputs `l`
        '''
        with patch('builtins.input') as mocked_input:
            with patch('app.list_blogs') as mocked_l:
                mocked_input.side_effect = ('l', 'q')

                app.menu()

                mocked_l.assert_called()
                

    def test_r(self):
        '''
         mocks input to menu, then mocks input of `r` and then `q` to quit;
         tests if `ask_read_blog` is called when user inputs `r`
        '''
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_r:
                mocked_input.side_effect = ('r', 'q')

                app.menu()

                mocked_r.assert_called()

    def test_p(self):
        '''
         mocks input to menu, then mocks input of `p` and then `q` to quit;
         tests if `ask_create_post` is called when user inputs `p`
        '''
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_p:
                mocked_input.side_effect = ('p', 'q')

                app.menu()

                mocked_p.assert_called()
    

    def test_menu_calls_print_blogs(self):
        with patch('app.list_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()
    

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.list_blogs()
            mocked_print.assert_called_with("Test Blog Title by Test Blog Author (0 posts).")


    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Blog Title', 'Test Blog Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs['Test Blog Title'])


    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test Blog Title'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test Blog Title'])


    def test_print_posts(self):
        blog = app.blogs['Test Blog Title']
        blog.create_post('Test Post Title','Test Post Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])


    def test_print_post(self):
        post = Post('Test Post Title', 'Test Post Content')
        expected_print = 'Test Post Title... Test Post Content'

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)


    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Blog Title', 'Test Post Title', 'Test Post Content')

            app.ask_create_post()

            self.assertEqual(app.blogs['Test Blog Title'].posts[0].title, 'Test Post Title')
            self.assertEqual(app.blogs['Test Blog Title'].posts[0].content, 'Test Post Content')



############------------ DRIVER CODE ------------############
