############------------ IMPORTS ------------############
from unittest import TestCase
from unittest.mock import patch
import app

############------------ GLOBAL VARIABLE(S) ------------############


############------------ CLASS(ES) ------------############
class AppTest(TestCase):
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('Test Blog')


############------------ DRIVER CODE ------------############
