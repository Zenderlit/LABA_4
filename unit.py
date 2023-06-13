import unittest
from unittest.mock import patch
from io import StringIO
from main import get_most_commonword, application


class TestGetMostCommonword(unittest.TestCase):
    def test_common_word(self):
        filename = 'testfile1.txt'
        with open(filename, 'w') as f:
            f.write('yes cat dog room man orange cat')
        self.assertEqual(get_most_commonword(filename), 'cat')

    def test_common_word_punctuation(self):
        filename = 'testfile2.txt'
        with open(filename, 'w') as f:
            f.write('yes, cat, room, eye, cat')
        self.assertEqual(get_most_commonword(filename), 'cat')

    def test_common_word_multiple(self):
        filename = 'testfile3.txt'
        with open(filename, 'w') as f:
            f.write('Dog yes quick brown fox jumped over the lazy dog.yes slept.')
        self.assertEqual(get_most_commonword(filename), 'dog')


class TestApplication(unittest.TestCase):
    @patch('builtins.open', return_value=StringIO('The quick brown fox jumped over the lazy dog.'))
    def test_response(self, mock_open):
        environ = {'PATH_INFO': '/test'}

        def start_response(status, headers):
            self.assertEqual(status, '200 OK')
            content_type = [header[1] for header in headers if header[0] == 'Content Type'][0]
            self.assertEqual(content_type, 'text/html')

        result = application(environ, start_response)
        self.assertIn(b'The most common word in text.txt is "the".', result)


if __name__ == '__main__':
    unittest.main()