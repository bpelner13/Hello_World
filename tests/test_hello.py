"""Test module for the Hello module"""

import unittest

from sample import hello


class TestLetterPrint(unittest.TestCase):
    """"Will test the letter_print method"""
    def setUp(self):
        """Set up the test"""
        pass
    def tearDown(self):
        """Close the test"""
        pass
    def test_happy_path(self):
        """Let's pretend our user is smart enough to enter a string and only one
        string..."""
        self.assertTrue(hello.letter_print('Hello there'))
    def test_sad_path(self):
        """Let's pretend our user is not very smart and wants to give the
        letter_print method a list instead..."""
        sadness = ['Hello there', ' General Kenobi']
        self.assertFalse(hello.letter_print(sadness))

if __name__ == '__main__':
    unittest.main()
