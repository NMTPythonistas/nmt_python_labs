import unittest

'''
This test assumes your function is named as follows:
    piglatin: Take in a single word and convert that single word to piglatin.
'''

class PigLatinTest(unittest.TestCase):
    def test_piglatin(self):
        import piglatin
        test_cases = [('glove', 'oveglay'),
                      ('egg', 'eggway'),
                      ('happy', 'appyhay'),
                      ('inbox', 'inboxway')]

        for inword, outword in test_cases:
            with self.subTest(i=inword):
                self.assertEqual(piglatin.piglatin(inword),
                    outword)

if __name__ == '__main__':
    unittest.main()
