import unittest
from unittest.mock import patch
import app
from blog import Blog


class AppTest(unittest.TestCase):
    def test_menu(self):
        with unittest.mock.patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_print_blogs(self):
        with unittest.mock.patch('app.print_blogs') as mocked_print_blogs:
            with unittest.mock.patch('builtins.input'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test title', 'Test author')

        app.blogs = {
            'Test': blog
        }

        with unittest.mock.patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(
                '- Test title by Test author (0 posts)')


if __name__ == '__main__':
    unittest.main()
