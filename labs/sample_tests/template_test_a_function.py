"""
This test assumes your function is named .
This function must take and return .
"""

import unittest

class Test(unittest.TestCase):
    test_cases = [("input", "output")]

    def test_validate(self):
        from test_file import test_function
        for test_input, test_output in Test.test_cases:
            with self.subTest(i=test_input):
                self.assertEqual(test_function(test_input), test_output)

if __name__ == '__main__':
    unittest.main()
