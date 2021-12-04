############------------ IMPORTS ------------############
from unittest import TestCase
from unittest.mock import patch
import app
from project.blog import Blog

############------------ GLOBAL VARIABLE(S) ------------############


############------------ CLASS(ES) ------------############
class AppTest(TestCase):
    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('Test by Test Author (0 posts)')


############------------ DRIVER CODE ------------############
