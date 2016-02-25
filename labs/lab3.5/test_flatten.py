"""
CSE 107. Spring 2016. Testing script for flatten.py.

This test assumes your function are named as follows:
    flatten --- takes a list as an argument

This function should be in a file called "flatten.py".
You should make no changes to this file.
"""

import unittest

class TestFlatten(unittest.TestCase):
    test_cases = [([], set([])),
                  ([1,2,3], {1,2,3}),
                  ([1,2,3,[4]], {1,2,3,4}),
                  ([1,[4],2,3], {1,2,3,4}),
                  ([[1,2],[3,[[[[[[[4]]]]]]]], 5],
                    [1,2,3,4,5]),
                  ([[[[-7,[[[[-6,[[-5,-4,
                                   [-3,-2,-1,"zero",[[[1,2,3]]],4,5,6],True]],
                              8,9],10]]]]]]],
                   {-7,-6,-5,-4,-3,-2,-1,"zero",1,2,3,4,5,6,True,8,9,10})]

    def test_flatten(self):
        import flatten
        for test_list, elements in TestFlatten.test_cases:
            with self.subTest(i=test_list):
                self.assertEqual(set(flatten.flatten(test_list)), elements)

if __name__ == '__main__':
    unittest.main()
