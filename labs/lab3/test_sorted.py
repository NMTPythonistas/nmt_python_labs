import unittest
import ast
# Used to communicate with external process
from subprocess import Popen, PIPE, STDOUT
import functools


def get_process_output(command, test_input, timeout=5):
    process = Popen(command.split(), stdout=PIPE, stdin=PIPE)
    process_stdout = process.communicate(
        input=test_input.encode(),
        timeout=timeout)[0].decode()
    return process_stdout


def get_last_line(string):
    # get last non empty line
    return list(filter(lambda x: x != '', string.split('\n')))[-1]


class SortedTest(unittest.TestCase):

    test_lists = map(lambda l: sorted(l), [[2.267605633802817, 2.9624413145539905, 4.615023474178404], [1.6056338028169015, 4.178403755868545, 1.8779342723004695, 0.5117370892018779, 3.727699530516432, 3.967136150234742, 2.92018779342723, 4.023474178403756], [0.046948356807511735, 1.9812206572769953, 1.7652582159624413, 0.863849765258216, 1.4225352112676057], [0.11737089201877934, 1.272300469483568, 3.788732394366197, 1.7417840375586855, 3.727699530516432, 4.39906103286385, 1.7699530516431925], [1.4976525821596245, 0.7981220657276995, 4.47887323943662, 0.9671361502347418, 2.464788732394366, 1.6854460093896713, 2.732394366197183], [3.15962441314554, 1.7887323943661972, 3.244131455399061, 2.9859154929577465], [0.9859154929577465, 0.7089201877934272], [0.09389671361502347, 0.36619718309859156], [1.2816901408450705, 0.16901408450704225], [2.779342723004695, 1.84037558685446, 0.7370892018779343, 3.3051643192488265, 4.314553990610329, 2.1502347417840375]])

    def test_sorted(self):
        for test_list in SortedTest.test_lists:
            with self.subTest(l=test_list):
                input_str = "\n".join(map(lambda l: str(l), test_list)) + "\nstop"
                last_line = get_last_line(get_process_output("python3 sorted.py", input_str))
                # try to find a list within the last line
                maybe_output_list = last_line[last_line.find("["):]
                self.assertEqual(ast.literal_eval(maybe_output_list), test_list)

if __name__ == "__main__":
    unittest.main()
