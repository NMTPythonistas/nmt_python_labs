"""
This test assumes your function is named `is_anagram`.
This function must take a string and return True or False.
"""

import unittest

class TestAnagrams(unittest.TestCase):
    test_cases = [("ab", "ba", True),
                  ("a", "a", True),
                  ("abc", "abc", True),
                  ("abc", "cba", True),
                  ("williamshakespeare", "iamaweakishspeller", True),
                  ("madamcurie", "radiumcame", True),
                  ("MadamCurie", "radiuMCame", True),
                  ("ab", "bc", False),
                  ("An", "anagram is a type of word play", False),
                  ("William Shakespeare", "I am a weakish speller", False),
                  ("The creation of anagrams assumes an alphabet",
                   " the symbols which are to be permuted.", False),
    ]

    def test_validate(self):
        import anagrams
        for test_input1, test_input2, test_output in TestAnagrams.test_cases:
            with self.subTest(i=(test_input1, test_input2)):
                self.assertEqual(anagrams.is_anagram(test_input1, test_input2),
                                 test_output)
                self.assertEqual(anagrams.is_anagram(test_input2, test_input1),
                                 test_output)

if __name__ == '__main__':
    unittest.main()
