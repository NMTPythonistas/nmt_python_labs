import unittest

# Used to communicate with external process
from subprocess import Popen, PIPE, STDOUT


class SumsTest(unittest.TestCase):
    timeout = 5  # seconds to run before sums.py is killed
    inputs = [[], [1], [1000], [1, 200, 32], list(range(0, 300, 44))]

    def test_sums(self):
        # check bad inputs are caught using an assertion
        for test_nums in SumsTest.inputs:
            with self.subTest(i=test_nums):
                test_sum = sum(test_nums)
                process = Popen("python3 sums.py".split(),
                                stdout=PIPE, stdin=PIPE)
                if len(test_nums) > 0:
                    test_input = '\n'.join(list(map(str, test_nums)))
                    test_input = test_input + '\nexit\n'
                else:
                    test_input = 'exit'

                process_stdout = process.communicate(
                    input=test_input.encode(), timeout=SumsTest.timeout)[0].decode()

                # is the last printed word an integer?
                last_word = process_stdout.split()[-1]
                process_sum = int(last_word)

                # is it the sum of the input numbers?
                self.assertEqual(process_sum, test_sum, msg='inputs {}: expected last word to be {}, received {}'.format(test_nums, test_sum, last_word))


if __name__ == '__main__':
    unittest.main()
