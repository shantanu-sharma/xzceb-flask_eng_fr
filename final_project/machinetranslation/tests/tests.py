import unittest
from translator import french_to_english, english_to_french

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english(' '),' ')
        #self.assertEqual(french_to_english(' adkfj'),'sdkjf ')

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french(' '),' ')
        #self.assertEqual(english_to_french('abc'),'def')

unittest.main()          