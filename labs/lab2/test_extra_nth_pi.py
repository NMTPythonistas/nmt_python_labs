import unittest


class PiTest(unittest.TestCase):
    inputs = [(0, '243F6A8885'), (1, '43F6A8885A'), (2, '3F6A8885A3'), (3, 'F6A8885A30'), (4, '6A8885A308'), (5, 'A8885A308D'), (6, '8885A308D3'), (7, '885A308D31'), (8, '85A308D313'), (9, '5A308D3131'), (10, 'A308D31319'), (11, '308D313198'), (12, '08D313198A'), (13, '8D313198A2'), (14, 'D313198A2E'), (15, '313198A2E0'), (16, '13198A2E03'), (17, '3198A2E037'), (18, '198A2E0370'), (19, '98A2E03707'), (20, '8A2E037073'), (100, '29B7C97C50'), (1000, '49F1C09B07')]
    large_inputs = [(10000, '8AC8FCFB80'), (50000, '940C214001'), (1000000, '6C65E52CB4')]

    def test_extra_nth_pi(self):
        import extra_nth_pi

        # check bad inputs are caught using an assertion
        for in_, expected_output_ in PiTest.inputs:
            with self.subTest(i=in_):
                actual_output = extra_nth_pi.digits(in_)
                self.assertTrue(len(test_out) > 0, msg="Output of length 0")
                self.assertTrue(expected_output.startswith(test_out.upper()), msg="input={}, expected output: '{}', received '{}'".format(in_, out_, test_out))


if __name__ == '__main__':
    unittest.main()
