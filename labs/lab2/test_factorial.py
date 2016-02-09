import unittest


class FactorialTest(unittest.TestCase):
    bad_inputs = map(lambda x: x / 5, list(range(-20, 1)))
    inputs = [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120),
              (6, 720), (7, 5040), (8, 40320), (9, 362880),
              (10, 3628800), (11, 39916800), (12, 479001600),
              (13, 6227020800), (14, 87178291200),
              (15, 1307674368000), (16, 20922789888000),
              (17, 355687428096000), (18, 6402373705728000),
              (19, 121645100408832000), (20, 2432902008176640000)]

    def test_factorial(self):
        import factorial

        # check bad inputs are caught using an assertion
        for bad in FactorialTest.bad_inputs:
            with self.subTest(i=bad):
                with self.assertRaises(AssertionError, msg="input={}".format(bad)):
                    factorial.factorial(bad)

        # check for expected output given positive integers
        for in_, out_ in FactorialTest.inputs:
            with self.subTest(i=in_):
                test_out = factorial.factorial(in_)
                self.assertEqual(test_out, out_, msg="input={}, expected output {}, received {}".format(in_, out_, test_out))


if __name__ == '__main__':
    unittest.main()
