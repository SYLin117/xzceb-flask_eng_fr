import unittest
from machinetranslation import translator


class Testing(unittest.TestCase):
    def test_englishToFrench(self):
        a = 'Hello'
        result = translator.english_to_french(a)
        b = 'Bonjour'
        self.assertEqual(result, b)

    def test_frenchToEnglish(self):
        a = 'Bonjour'
        result = translator.french_to_english(a)
        b = 'Hello'
        self.assertEqual(result, b)


if __name__ == '__main__':
    unittest.main()
