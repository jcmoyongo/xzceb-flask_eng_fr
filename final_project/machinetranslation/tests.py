import unittest

from translator import french_to_english, english_to_french, API_KEY, URL

class TestTranslator(unittest.TestCase): 
    def testFrenchToEnglish(self): 
        self.assertEqual(french_to_english(None, API_KEY, URL),"No text.") 
        self.assertEqual(french_to_english('Bonjour', API_KEY, URL), 'Hello')  
 
    def testEnglisthToFrench(self): 
        self.assertEqual(english_to_french(None, API_KEY, URL),"No text.") 
        self.assertEqual(english_to_french('Hello', API_KEY, URL), 'Bonjour') 

unittest.main()