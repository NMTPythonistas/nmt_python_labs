# Testing
import pytest
from hypothesis import given
import hypothesis.strategies as st

# Communicate with external processes
from subprocess import Popen, PIPE, STDOUT


script_name = "adder_stdin_stdout.py"


@given(st.integers(), st.integers())
def test_adder_stdin_stdout(test_a, test_b):
    """Tests if the script accepts two newline separated integer inputs and returns their addition followed immediately by a newline.

    # idk if this syntax is right \_:D_/
    python3 script.py < echo "1\n2\n"
    output ends in OB"{test_a + test_b}\n"
    """
    p = Popen("python3 {}".format(script_name).split(), stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    script_stdout = p.communicate(input='{}\n{}\n'.format(test_a, test_b).encode())[0]
    script_stdout = script_stdout.decode()
    assert("{}\n".format(test_a + test_b) in script_stdout)

@given(st.integers(), st.integers())
def test_adder_library(test_a, test_b):
    import adder_library
    assert(test_a + test_b == adder_library.add(test_a, test_b))
