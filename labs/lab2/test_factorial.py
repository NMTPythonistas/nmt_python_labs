import unittest
# Used to communicate with external process
from subprocess import Popen, PIPE, STDOUT


class FactorialTest(unittest.TestCase):
    timeout = 5
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
                # is it the sum of the input numbers?
                process_output = get_process_output("python3 factorial.py", "{}\n".format(in_))
                self.assertEqual(last_word, expected_output,
                         msg='input {}: expected output {}, received {}'\
                         .format(in_, "Not a positive integer",
                                 process_output))

        # check for expected output given positive integers
        for in_, out_ in FactorialTest.inputs:
            with self.subTest(i=in_):
                last_word = get_last_word(get_process_output("python3 factorial.py", "{}\n".format(in_)))

                # make sure it is an integer
                test_out = int(last_word)
                self.assertEqual(test_out, out_,
                                 msg="input={}, expected output {}, received {}".format(in_, out_, test_out))

    def get_process_output(command, test_input, timeout=5):
        process = Popen(command.split(),
                        stdout=PIPE, stdin=PIPE)
        process_stdout = process.communicate(
            input=test_input.encode(),
            timeout=timeout)[0].decode()
        return process_stdout

    def get_last_word(string):
        return string.split()[-1]


if __name__ == '__main__':
    unittest.main()
