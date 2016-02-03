# Testing
import pytest
from hypothesis import given
import hypothesis.strategies as st

# Communicate with external processes
from subprocess import Popen, PIPE, STDOUT


# For demonstration purposes only.
want_failure = False


# Run test using many combinations of automatically generated input.
# If a failure is detected, the hypothesis library will try to produce a
# minimal input. For example, it would find the shortest string or smallest
# integer.

# See
# https://docs.python.org/3/library/subprocess.html
# https://hypothesis.readthedocs.org/en/latest/
@given(st.integers(), st.integers())
def test_adder_stdin_stdout(test_a, test_b):
    """Tests if the script accepts two newline separated integer inputs a, b
    and if it returns a + b followed immediately by a newline.

    Given input "{test_a}\n{test_b}\n",
    the output must contain line which ends in "{test_a + test_b}\n"
    """

    script_name = "adder_stdin_stdout.py"

    # run script
    p = Popen("python3 {}".format(script_name).split(),
              # use Popen.communicate for stdin and stdout
              stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    # feed input
    test_input = '{}\n{}\n'.format(test_a, test_b).encode()

    # retrieve and verify output
    script_stdout = p.communicate(input=test_input)[0].decode()
    assert("{}\n".format(test_a + test_b) in script_stdout)


@given(st.integers(), st.integers())
def test_adder_library(test_a, test_b):
    """Checks if module can be imported and if adder_library.add works as
    expected."""

    # this test fails if import fails
    import adder_library

    if want_failure:
        adder_library.winning = False

    # test against known output
    oracle_output = test_a + test_b
    output = adder_library.add(test_a, test_b)
    assert(oracle_output == output)


#### Test using list of known input-output pairs
weierstrass_samples = [
    (0.0, 0.0),
    (0.1, 0.18565188043473438),
    (0.2, 0.19819595995165212),
    (0.3, 0.25625088651699685),
    (0.4, 0.2137918664233767),
    (0.5, 0.39269749014820104),
    (0.6, 0.320687799634669),
    (0.7, 0.3223162065019885),
    (0.8, 0.13213063996728286),
    (0.9, 0.07875594722286147)
]

# See
# http://pytest.org/latest/parametrize.html
@pytest.mark.parametrize("input_,near", weierstrass_samples)
def test_weierstrass(input_, near):
    """Checks if user's module outputs accurate enough values of the
    Weierstrass function.
    """

    import weierstrass
    epsilon = 0.01
    output = weierstrass.evaluate_at(input_)
    if want_failure:
        output = weierstrass.evaluate_at(input_, max_k=10)
    assert(abs(near - output) <= epsilon)
