"""
This test assumes your functions are named as follows:
    validate: Take in a credit card number as a string and return True if valid, False if no.

You should make no other changes to this file.
"""

import unittest

class TestLuhns(unittest.TestCase):
    test_cases = [("38520000023237", True),
                  ("49927398716", True),
                  ("49927398717", False),
                  ("1234567812345678", False),
                  ("1234567812345670", True)]

    def test_validate(self):
        import luhns
        for ccnum, valid in TestLuhns.test_cases:
            with self.subTest(i=ccnum):
                self.assertEqual(luhns.validate(ccnum), valid)

if __name__ == '__main__':
    unittest.main()
