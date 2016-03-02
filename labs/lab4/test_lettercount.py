"""
This test assumes your function is named `count_letters`.
This function must take a string and return a dictionary.
"""

import unittest

class TestCountLetters(unittest.TestCase):
    test_cases = [("", dict()),
                  ("abc", {'a': 1, 'c': 1, 'b': 1}),
                  ("ABC abc", {'a': 2, 'c': 2, 'b': 2}),
                  ("The cat in the hat",
                   {'h': 3, 'i': 1, 'c': 1, 't': 4, 'n': 1, 'a': 2, 'e': 2}),
                  ("A partial solar eclipse will occur on August Third",
                   {'h': 1, 'c': 3, 'o': 3, 'w': 1, 'n': 1, 't': 3, 'd': 1,
                    'l': 5, 'i': 4, 'p': 2, 'g': 1, 'r': 4, 'a': 5, 's': 3,
                    'u': 3, 'e': 2}
                  )]

    def test_validate(self):
        import lettercount

        for test_input, test_output in TestCountLetters.test_cases:
            with self.subTest(i=test_input):
                print("given", "'{}'".format(test_input), "should output", test_output)
                self.assertEqual(lettercount.count_letters(test_input),
                                 test_output)

if __name__ == '__main__':
    unittest.main()
