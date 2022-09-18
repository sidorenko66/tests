import unittest
from unittest.mock import patch

from task1 import get_doc_owner_name, get_doc_shelf, delete_doc, add_new_shelf

class MyTestCase(unittest.TestCase):
    def test_get_doc_owner_name(self):
        with patch('builtins.input', return_value='10006'):
            self.assertEqual('Аристарх Павлов', get_doc_owner_name())

    def test_get_doc_shelf(self):
        with patch('builtins.input', return_value='10006'):
            self.assertEqual('2', get_doc_shelf())

    def test_delete_doc(self):
        with patch('builtins.input', return_value='11-2'):
            self.assertEqual(('11-2', True), delete_doc())

    def test_add_new_shelf(self):
        with patch('builtins.input', return_value='12345'):
            self.assertEqual(('12345', True), add_new_shelf())

if __name__ == '__main__':
    unittest.main()
