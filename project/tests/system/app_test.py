############------------ IMPORTS ------------############
from unittest import TestCase
from unittest.mock import patch
import app
from project.app import print_blogs
from project.blog import Blog

############------------ GLOBAL VARIABLE(S) ------------############


############------------ CLASS(ES) ------------############
class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
    
    def test_is_print_blogs_function_printed(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called(print_blogs)
    
    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('Test by Test Author (0 posts)')


    


############------------ DRIVER CODE ------------############
