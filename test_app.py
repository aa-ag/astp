import unittest
from unittest.mock import patch
import app
from blog import Blog


class AppTest(unittest.TestCase):
    def test_print_blogs(self):
        blog = Blog('Test title', 'Test author')

        app.blogs = {
            'Test': blog
        }

        with unittest.mock.patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(
                '- Test title by Test author (0 posts)')

    def test_menu(self):
        with unittest.mock.patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)


if __name__ == '__main__':
    unittest.main()
