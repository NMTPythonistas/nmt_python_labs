import unittest
# Used to communicate with external process
from subprocess import Popen, PIPE, STDOUT


def get_process_output(command, test_input, timeout=5):
    process = Popen(command.split(), stdout=PIPE, stdin=PIPE)
    process_stdout = process.communicate(
        input=test_input.encode(),
        timeout=timeout)[0].decode()
    return process_stdout


def get_last_line(string):
    # get last non empty line
    return list(filter(lambda x: x != '', string.split('\n')))[-1]


class PrimesTest(unittest.TestCase):
    # prime numbers up to 101
    true_inputs = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53}
    large_inputs = {59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
        103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
        449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009}

    # all other numbers between -50 and the max
    false_inputs = set(
        range(max(true_inputs) + 1)) - true_inputs
    false_inputs = false_inputs.union(set(range(-5, 1)))

    def test_primes(self):
        # check bad inputs are caught using an assertion
        for f in PrimesTest.false_inputs:
            with self.subTest(i=f):
                print("test input:", f)
                last_line = get_last_line(get_process_output("python3 primes.py", str(f)))
                self.assertTrue(last_line.endswith("not prime"), msg="non-prime number misclassified {}, expected 'not prime' received {}".format(f, last_line))

        # check for expected output given positive integers
        for t in PrimesTest.true_inputs:
            with self.subTest(i=t):
                print("test input:", t)
                last_line = get_last_line(get_process_output("python3 primes.py", str(t)))
                last_line_prime = last_line.endswith("prime") and not last_line.endswith("not prime")
                self.assertTrue(last_line_prime, msg="prime number misclassified {}, expected 'prime' received {}".format(t, last_line))


if __name__ == '__main__':
    unittest.main()
