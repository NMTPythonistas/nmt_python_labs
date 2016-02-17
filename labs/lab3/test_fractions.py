import unittest
import functools


class FractionsTests(unittest.TestCase):
    multiplications = [(((-29, -29), (-29, -29)), (841, 841)), (((-1, -29), (-29, -29)), (29, 841)), (((0, -29), (-29, -29)), (0, 841)), (((1, -29), (-29, -29)), (-29, 841)), (((499, -29), (-29, -29)), (-14471, 841)), (((-29, -1), (-29, -29)), (841, 29)), (((-1, -1), (-29, -29)), (29, 29)), (((0, -1), (-29, -29)), (0, 29)), (((1, -1), (-29, -29)), (-29, 29)), (((499, -1), (-29, -29)), (-14471, 29)), (((-29, 1), (-29, -29)), (841, -29)), (((-1, 1), (-29, -29)), (29, -29)), (((0, 1), (-29, -29)), (0, -29)), (((1, 1), (-29, -29)), (-29, -29)), (((499, 1), (-29, -29)), (-14471, -29)), (((-29, 499), (-29, -29)), (841, -14471)), (((-1, 499), (-29, -29)), (29, -14471)), (((0, 499), (-29, -29)), (0, -14471)), (((1, 499), (-29, -29)), (-29, -14471)), (((499, 499), (-29, -29)), (-14471, -14471)), (((-29, -29), (-1, -29)), (29, 841)), (((-1, -29), (-1, -29)), (1, 841)), (((0, -29), (-1, -29)), (0, 841)), (((1, -29), (-1, -29)), (-1, 841)), (((499, -29), (-1, -29)), (-499, 841)), (((-29, -1), (-1, -29)), (29, 29)), (((-1, -1), (-1, -29)), (1, 29)), (((0, -1), (-1, -29)), (0, 29)), (((1, -1), (-1, -29)), (-1, 29)), (((499, -1), (-1, -29)), (-499, 29)), (((-29, 1), (-1, -29)), (29, -29)), (((-1, 1), (-1, -29)), (1, -29)), (((0, 1), (-1, -29)), (0, -29)), (((1, 1), (-1, -29)), (-1, -29)), (((499, 1), (-1, -29)), (-499, -29)), (((-29, 499), (-1, -29)), (29, -14471)), (((-1, 499), (-1, -29)), (1, -14471)), (((0, 499), (-1, -29)), (0, -14471)), (((1, 499), (-1, -29)), (-1, -14471)), (((499, 499), (-1, -29)), (-499, -14471)), (((-29, -29), (0, -29)), (0, 841)), (((-1, -29), (0, -29)), (0, 841)), (((0, -29), (0, -29)), (0, 841)), (((1, -29), (0, -29)), (0, 841)), (((499, -29), (0, -29)), (0, 841)), (((-29, -1), (0, -29)), (0, 29)), (((-1, -1), (0, -29)), (0, 29)), (((0, -1), (0, -29)), (0, 29)), (((1, -1), (0, -29)), (0, 29)), (((499, -1), (0, -29)), (0, 29)), (((-29, 1), (0, -29)), (0, -29)), (((-1, 1), (0, -29)), (0, -29)), (((0, 1), (0, -29)), (0, -29)), (((1, 1), (0, -29)), (0, -29)), (((499, 1), (0, -29)), (0, -29)), (((-29, 499), (0, -29)), (0, -14471)), (((-1, 499), (0, -29)), (0, -14471)), (((0, 499), (0, -29)), (0, -14471)), (((1, 499), (0, -29)), (0, -14471)), (((499, 499), (0, -29)), (0, -14471)), (((-29, -29), (1, -29)), (-29, 841)), (((-1, -29), (1, -29)), (-1, 841)), (((0, -29), (1, -29)), (0, 841)), (((1, -29), (1, -29)), (1, 841)), (((499, -29), (1, -29)), (499, 841)), (((-29, -1), (1, -29)), (-29, 29)), (((-1, -1), (1, -29)), (-1, 29)), (((0, -1), (1, -29)), (0, 29)), (((1, -1), (1, -29)), (1, 29)), (((499, -1), (1, -29)), (499, 29)), (((-29, 1), (1, -29)), (-29, -29)), (((-1, 1), (1, -29)), (-1, -29)), (((0, 1), (1, -29)), (0, -29)), (((1, 1), (1, -29)), (1, -29)), (((499, 1), (1, -29)), (499, -29)), (((-29, 499), (1, -29)), (-29, -14471)), (((-1, 499), (1, -29)), (-1, -14471)), (((0, 499), (1, -29)), (0, -14471)), (((1, 499), (1, -29)), (1, -14471)), (((499, 499), (1, -29)), (499, -14471)), (((-29, -29), (499, -29)), (-14471, 841)), (((-1, -29), (499, -29)), (-499, 841)), (((0, -29), (499, -29)), (0, 841)), (((1, -29), (499, -29)), (499, 841)), (((499, -29), (499, -29)), (249001, 841)), (((-29, -1), (499, -29)), (-14471, 29)), (((-1, -1), (499, -29)), (-499, 29)), (((0, -1), (499, -29)), (0, 29)), (((1, -1), (499, -29)), (499, 29)), (((499, -1), (499, -29)), (249001, 29)), (((-29, 1), (499, -29)), (-14471, -29)), (((-1, 1), (499, -29)), (-499, -29)), (((0, 1), (499, -29)), (0, -29)), (((1, 1), (499, -29)), (499, -29)), (((499, 1), (499, -29)), (249001, -29)), (((-29, 499), (499, -29)), (-14471, -14471)), (((-1, 499), (499, -29)), (-499, -14471)), (((0, 499), (499, -29)), (0, -14471)), (((1, 499), (499, -29)), (499, -14471)), (((499, 499), (499, -29)), (249001, -14471)), (((-29, -29), (-29, -1)), (841, 29)), (((-1, -29), (-29, -1)), (29, 29)), (((0, -29), (-29, -1)), (0, 29)), (((1, -29), (-29, -1)), (-29, 29)), (((499, -29), (-29, -1)), (-14471, 29)), (((-29, -1), (-29, -1)), (841, 1)), (((-1, -1), (-29, -1)), (29, 1)), (((0, -1), (-29, -1)), (0, 1)), (((1, -1), (-29, -1)), (-29, 1)), (((499, -1), (-29, -1)), (-14471, 1)), (((-29, 1), (-29, -1)), (841, -1)), (((-1, 1), (-29, -1)), (29, -1)), (((0, 1), (-29, -1)), (0, -1)), (((1, 1), (-29, -1)), (-29, -1)), (((499, 1), (-29, -1)), (-14471, -1)), (((-29, 499), (-29, -1)), (841, -499)), (((-1, 499), (-29, -1)), (29, -499)), (((0, 499), (-29, -1)), (0, -499)), (((1, 499), (-29, -1)), (-29, -499)), (((499, 499), (-29, -1)), (-14471, -499)), (((-29, -29), (-1, -1)), (29, 29)), (((-1, -29), (-1, -1)), (1, 29)), (((0, -29), (-1, -1)), (0, 29)), (((1, -29), (-1, -1)), (-1, 29)), (((499, -29), (-1, -1)), (-499, 29)), (((-29, -1), (-1, -1)), (29, 1)), (((-1, -1), (-1, -1)), (1, 1)), (((0, -1), (-1, -1)), (0, 1)), (((1, -1), (-1, -1)), (-1, 1)), (((499, -1), (-1, -1)), (-499, 1)), (((-29, 1), (-1, -1)), (29, -1)), (((-1, 1), (-1, -1)), (1, -1)), (((0, 1), (-1, -1)), (0, -1)), (((1, 1), (-1, -1)), (-1, -1)), (((499, 1), (-1, -1)), (-499, -1)), (((-29, 499), (-1, -1)), (29, -499)), (((-1, 499), (-1, -1)), (1, -499)), (((0, 499), (-1, -1)), (0, -499)), (((1, 499), (-1, -1)), (-1, -499)), (((499, 499), (-1, -1)), (-499, -499)), (((-29, -29), (0, -1)), (0, 29)), (((-1, -29), (0, -1)), (0, 29)), (((0, -29), (0, -1)), (0, 29)), (((1, -29), (0, -1)), (0, 29)), (((499, -29), (0, -1)), (0, 29)), (((-29, -1), (0, -1)), (0, 1)), (((-1, -1), (0, -1)), (0, 1)), (((0, -1), (0, -1)), (0, 1)), (((1, -1), (0, -1)), (0, 1)), (((499, -1), (0, -1)), (0, 1)), (((-29, 1), (0, -1)), (0, -1)), (((-1, 1), (0, -1)), (0, -1)), (((0, 1), (0, -1)), (0, -1)), (((1, 1), (0, -1)), (0, -1)), (((499, 1), (0, -1)), (0, -1)), (((-29, 499), (0, -1)), (0, -499)), (((-1, 499), (0, -1)), (0, -499)), (((0, 499), (0, -1)), (0, -499)), (((1, 499), (0, -1)), (0, -499)), (((499, 499), (0, -1)), (0, -499)), (((-29, -29), (1, -1)), (-29, 29)), (((-1, -29), (1, -1)), (-1, 29)), (((0, -29), (1, -1)), (0, 29)), (((1, -29), (1, -1)), (1, 29)), (((499, -29), (1, -1)), (499, 29)), (((-29, -1), (1, -1)), (-29, 1)), (((-1, -1), (1, -1)), (-1, 1)), (((0, -1), (1, -1)), (0, 1)), (((1, -1), (1, -1)), (1, 1)), (((499, -1), (1, -1)), (499, 1)), (((-29, 1), (1, -1)), (-29, -1)), (((-1, 1), (1, -1)), (-1, -1)), (((0, 1), (1, -1)), (0, -1)), (((1, 1), (1, -1)), (1, -1)), (((499, 1), (1, -1)), (499, -1)), (((-29, 499), (1, -1)), (-29, -499)), (((-1, 499), (1, -1)), (-1, -499)), (((0, 499), (1, -1)), (0, -499)), (((1, 499), (1, -1)), (1, -499)), (((499, 499), (1, -1)), (499, -499)), (((-29, -29), (499, -1)), (-14471, 29)), (((-1, -29), (499, -1)), (-499, 29)), (((0, -29), (499, -1)), (0, 29)), (((1, -29), (499, -1)), (499, 29)), (((499, -29), (499, -1)), (249001, 29)), (((-29, -1), (499, -1)), (-14471, 1)), (((-1, -1), (499, -1)), (-499, 1)), (((0, -1), (499, -1)), (0, 1)), (((1, -1), (499, -1)), (499, 1)), (((499, -1), (499, -1)), (249001, 1)), (((-29, 1), (499, -1)), (-14471, -1)), (((-1, 1), (499, -1)), (-499, -1)), (((0, 1), (499, -1)), (0, -1)), (((1, 1), (499, -1)), (499, -1)), (((499, 1), (499, -1)), (249001, -1)), (((-29, 499), (499, -1)), (-14471, -499)), (((-1, 499), (499, -1)), (-499, -499)), (((0, 499), (499, -1)), (0, -499)), (((1, 499), (499, -1)), (499, -499)), (((499, 499), (499, -1)), (249001, -499)), (((-29, -29), (-29, 1)), (841, -29)), (((-1, -29), (-29, 1)), (29, -29)), (((0, -29), (-29, 1)), (0, -29)), (((1, -29), (-29, 1)), (-29, -29)), (((499, -29), (-29, 1)), (-14471, -29)), (((-29, -1), (-29, 1)), (841, -1)), (((-1, -1), (-29, 1)), (29, -1)), (((0, -1), (-29, 1)), (0, -1)), (((1, -1), (-29, 1)), (-29, -1)), (((499, -1), (-29, 1)), (-14471, -1)), (((-29, 1), (-29, 1)), (841, 1)), (((-1, 1), (-29, 1)), (29, 1)), (((0, 1), (-29, 1)), (0, 1)), (((1, 1), (-29, 1)), (-29, 1)), (((499, 1), (-29, 1)), (-14471, 1)), (((-29, 499), (-29, 1)), (841, 499)), (((-1, 499), (-29, 1)), (29, 499)), (((0, 499), (-29, 1)), (0, 499)), (((1, 499), (-29, 1)), (-29, 499)), (((499, 499), (-29, 1)), (-14471, 499)), (((-29, -29), (-1, 1)), (29, -29)), (((-1, -29), (-1, 1)), (1, -29)), (((0, -29), (-1, 1)), (0, -29)), (((1, -29), (-1, 1)), (-1, -29)), (((499, -29), (-1, 1)), (-499, -29)), (((-29, -1), (-1, 1)), (29, -1)), (((-1, -1), (-1, 1)), (1, -1)), (((0, -1), (-1, 1)), (0, -1)), (((1, -1), (-1, 1)), (-1, -1)), (((499, -1), (-1, 1)), (-499, -1)), (((-29, 1), (-1, 1)), (29, 1)), (((-1, 1), (-1, 1)), (1, 1)), (((0, 1), (-1, 1)), (0, 1)), (((1, 1), (-1, 1)), (-1, 1)), (((499, 1), (-1, 1)), (-499, 1)), (((-29, 499), (-1, 1)), (29, 499)), (((-1, 499), (-1, 1)), (1, 499)), (((0, 499), (-1, 1)), (0, 499)), (((1, 499), (-1, 1)), (-1, 499)), (((499, 499), (-1, 1)), (-499, 499)), (((-29, -29), (0, 1)), (0, -29)), (((-1, -29), (0, 1)), (0, -29)), (((0, -29), (0, 1)), (0, -29)), (((1, -29), (0, 1)), (0, -29)), (((499, -29), (0, 1)), (0, -29)), (((-29, -1), (0, 1)), (0, -1)), (((-1, -1), (0, 1)), (0, -1)), (((0, -1), (0, 1)), (0, -1)), (((1, -1), (0, 1)), (0, -1)), (((499, -1), (0, 1)), (0, -1)), (((-29, 1), (0, 1)), (0, 1)), (((-1, 1), (0, 1)), (0, 1)), (((0, 1), (0, 1)), (0, 1)), (((1, 1), (0, 1)), (0, 1)), (((499, 1), (0, 1)), (0, 1)), (((-29, 499), (0, 1)), (0, 499)), (((-1, 499), (0, 1)), (0, 499)), (((0, 499), (0, 1)), (0, 499)), (((1, 499), (0, 1)), (0, 499)), (((499, 499), (0, 1)), (0, 499)), (((-29, -29), (1, 1)), (-29, -29)), (((-1, -29), (1, 1)), (-1, -29)), (((0, -29), (1, 1)), (0, -29)), (((1, -29), (1, 1)), (1, -29)), (((499, -29), (1, 1)), (499, -29)), (((-29, -1), (1, 1)), (-29, -1)), (((-1, -1), (1, 1)), (-1, -1)), (((0, -1), (1, 1)), (0, -1)), (((1, -1), (1, 1)), (1, -1)), (((499, -1), (1, 1)), (499, -1)), (((-29, 1), (1, 1)), (-29, 1)), (((-1, 1), (1, 1)), (-1, 1)), (((0, 1), (1, 1)), (0, 1)), (((1, 1), (1, 1)), (1, 1)), (((499, 1), (1, 1)), (499, 1)), (((-29, 499), (1, 1)), (-29, 499)), (((-1, 499), (1, 1)), (-1, 499)), (((0, 499), (1, 1)), (0, 499)), (((1, 499), (1, 1)), (1, 499)), (((499, 499), (1, 1)), (499, 499)), (((-29, -29), (499, 1)), (-14471, -29)), (((-1, -29), (499, 1)), (-499, -29)), (((0, -29), (499, 1)), (0, -29)), (((1, -29), (499, 1)), (499, -29)), (((499, -29), (499, 1)), (249001, -29)), (((-29, -1), (499, 1)), (-14471, -1)), (((-1, -1), (499, 1)), (-499, -1)), (((0, -1), (499, 1)), (0, -1)), (((1, -1), (499, 1)), (499, -1)), (((499, -1), (499, 1)), (249001, -1)), (((-29, 1), (499, 1)), (-14471, 1)), (((-1, 1), (499, 1)), (-499, 1)), (((0, 1), (499, 1)), (0, 1)), (((1, 1), (499, 1)), (499, 1)), (((499, 1), (499, 1)), (249001, 1)), (((-29, 499), (499, 1)), (-14471, 499)), (((-1, 499), (499, 1)), (-499, 499)), (((0, 499), (499, 1)), (0, 499)), (((1, 499), (499, 1)), (499, 499)), (((499, 499), (499, 1)), (249001, 499)), (((-29, -29), (-29, 499)), (841, -14471)), (((-1, -29), (-29, 499)), (29, -14471)), (((0, -29), (-29, 499)), (0, -14471)), (((1, -29), (-29, 499)), (-29, -14471)), (((499, -29), (-29, 499)), (-14471, -14471)), (((-29, -1), (-29, 499)), (841, -499)), (((-1, -1), (-29, 499)), (29, -499)), (((0, -1), (-29, 499)), (0, -499)), (((1, -1), (-29, 499)), (-29, -499)), (((499, -1), (-29, 499)), (-14471, -499)), (((-29, 1), (-29, 499)), (841, 499)), (((-1, 1), (-29, 499)), (29, 499)), (((0, 1), (-29, 499)), (0, 499)), (((1, 1), (-29, 499)), (-29, 499)), (((499, 1), (-29, 499)), (-14471, 499)), (((-29, 499), (-29, 499)), (841, 249001)), (((-1, 499), (-29, 499)), (29, 249001)), (((0, 499), (-29, 499)), (0, 249001)), (((1, 499), (-29, 499)), (-29, 249001)), (((499, 499), (-29, 499)), (-14471, 249001)), (((-29, -29), (-1, 499)), (29, -14471)), (((-1, -29), (-1, 499)), (1, -14471)), (((0, -29), (-1, 499)), (0, -14471)), (((1, -29), (-1, 499)), (-1, -14471)), (((499, -29), (-1, 499)), (-499, -14471)), (((-29, -1), (-1, 499)), (29, -499)), (((-1, -1), (-1, 499)), (1, -499)), (((0, -1), (-1, 499)), (0, -499)), (((1, -1), (-1, 499)), (-1, -499)), (((499, -1), (-1, 499)), (-499, -499)), (((-29, 1), (-1, 499)), (29, 499)), (((-1, 1), (-1, 499)), (1, 499)), (((0, 1), (-1, 499)), (0, 499)), (((1, 1), (-1, 499)), (-1, 499)), (((499, 1), (-1, 499)), (-499, 499)), (((-29, 499), (-1, 499)), (29, 249001)), (((-1, 499), (-1, 499)), (1, 249001)), (((0, 499), (-1, 499)), (0, 249001)), (((1, 499), (-1, 499)), (-1, 249001)), (((499, 499), (-1, 499)), (-499, 249001)), (((-29, -29), (0, 499)), (0, -14471)), (((-1, -29), (0, 499)), (0, -14471)), (((0, -29), (0, 499)), (0, -14471)), (((1, -29), (0, 499)), (0, -14471)), (((499, -29), (0, 499)), (0, -14471)), (((-29, -1), (0, 499)), (0, -499)), (((-1, -1), (0, 499)), (0, -499)), (((0, -1), (0, 499)), (0, -499)), (((1, -1), (0, 499)), (0, -499)), (((499, -1), (0, 499)), (0, -499)), (((-29, 1), (0, 499)), (0, 499)), (((-1, 1), (0, 499)), (0, 499)), (((0, 1), (0, 499)), (0, 499)), (((1, 1), (0, 499)), (0, 499)), (((499, 1), (0, 499)), (0, 499)), (((-29, 499), (0, 499)), (0, 249001)), (((-1, 499), (0, 499)), (0, 249001)), (((0, 499), (0, 499)), (0, 249001)), (((1, 499), (0, 499)), (0, 249001)), (((499, 499), (0, 499)), (0, 249001)), (((-29, -29), (1, 499)), (-29, -14471)), (((-1, -29), (1, 499)), (-1, -14471)), (((0, -29), (1, 499)), (0, -14471)), (((1, -29), (1, 499)), (1, -14471)), (((499, -29), (1, 499)), (499, -14471)), (((-29, -1), (1, 499)), (-29, -499)), (((-1, -1), (1, 499)), (-1, -499)), (((0, -1), (1, 499)), (0, -499)), (((1, -1), (1, 499)), (1, -499)), (((499, -1), (1, 499)), (499, -499)), (((-29, 1), (1, 499)), (-29, 499)), (((-1, 1), (1, 499)), (-1, 499)), (((0, 1), (1, 499)), (0, 499)), (((1, 1), (1, 499)), (1, 499)), (((499, 1), (1, 499)), (499, 499)), (((-29, 499), (1, 499)), (-29, 249001)), (((-1, 499), (1, 499)), (-1, 249001)), (((0, 499), (1, 499)), (0, 249001)), (((1, 499), (1, 499)), (1, 249001)), (((499, 499), (1, 499)), (499, 249001)), (((-29, -29), (499, 499)), (-14471, -14471)), (((-1, -29), (499, 499)), (-499, -14471)), (((0, -29), (499, 499)), (0, -14471)), (((1, -29), (499, 499)), (499, -14471)), (((499, -29), (499, 499)), (249001, -14471)), (((-29, -1), (499, 499)), (-14471, -499)), (((-1, -1), (499, 499)), (-499, -499)), (((0, -1), (499, 499)), (0, -499)), (((1, -1), (499, 499)), (499, -499)), (((499, -1), (499, 499)), (249001, -499)), (((-29, 1), (499, 499)), (-14471, 499)), (((-1, 1), (499, 499)), (-499, 499)), (((0, 1), (499, 499)), (0, 499)), (((1, 1), (499, 499)), (499, 499)), (((499, 1), (499, 499)), (249001, 499)), (((-29, 499), (499, 499)), (-14471, 249001)), (((-1, 499), (499, 499)), (-499, 249001)), (((0, 499), (499, 499)), (0, 249001)), (((1, 499), (499, 499)), (499, 249001)), (((499, 499), (499, 499)), (249001, 249001))]

    divisions = [(((-29, -29), (-29, -29)), (841, 841)), (((-1, -29), (-29, -29)), (29, 841)), (((0, -29), (-29, -29)), (0, 841)), (((1, -29), (-29, -29)), (-29, 841)), (((499, -29), (-29, -29)), (-14471, 841)), (((-29, -1), (-29, -29)), (841, 29)), (((-1, -1), (-29, -29)), (29, 29)), (((0, -1), (-29, -29)), (0, 29)), (((1, -1), (-29, -29)), (-29, 29)), (((499, -1), (-29, -29)), (-14471, 29)), (((-29, 1), (-29, -29)), (841, -29)), (((-1, 1), (-29, -29)), (29, -29)), (((0, 1), (-29, -29)), (0, -29)), (((1, 1), (-29, -29)), (-29, -29)), (((499, 1), (-29, -29)), (-14471, -29)), (((-29, 499), (-29, -29)), (841, -14471)), (((-1, 499), (-29, -29)), (29, -14471)), (((0, 499), (-29, -29)), (0, -14471)), (((1, 499), (-29, -29)), (-29, -14471)), (((499, 499), (-29, -29)), (-14471, -14471)), (((-29, -29), (-1, -29)), (841, 29)), (((-1, -29), (-1, -29)), (29, 29)), (((0, -29), (-1, -29)), (0, 29)), (((1, -29), (-1, -29)), (-29, 29)), (((499, -29), (-1, -29)), (-14471, 29)), (((-29, -1), (-1, -29)), (841, 1)), (((-1, -1), (-1, -29)), (29, 1)), (((0, -1), (-1, -29)), (0, 1)), (((1, -1), (-1, -29)), (-29, 1)), (((499, -1), (-1, -29)), (-14471, 1)), (((-29, 1), (-1, -29)), (841, -1)), (((-1, 1), (-1, -29)), (29, -1)), (((0, 1), (-1, -29)), (0, -1)), (((1, 1), (-1, -29)), (-29, -1)), (((499, 1), (-1, -29)), (-14471, -1)), (((-29, 499), (-1, -29)), (841, -499)), (((-1, 499), (-1, -29)), (29, -499)), (((0, 499), (-1, -29)), (0, -499)), (((1, 499), (-1, -29)), (-29, -499)), (((499, 499), (-1, -29)), (-14471, -499)), (((-29, -29), (0, -29)), (841, 0)), (((-1, -29), (0, -29)), (29, 0)), (((0, -29), (0, -29)), (0, 0)), (((1, -29), (0, -29)), (-29, 0)), (((499, -29), (0, -29)), (-14471, 0)), (((-29, -1), (0, -29)), (841, 0)), (((-1, -1), (0, -29)), (29, 0)), (((0, -1), (0, -29)), (0, 0)), (((1, -1), (0, -29)), (-29, 0)), (((499, -1), (0, -29)), (-14471, 0)), (((-29, 1), (0, -29)), (841, 0)), (((-1, 1), (0, -29)), (29, 0)), (((0, 1), (0, -29)), (0, 0)), (((1, 1), (0, -29)), (-29, 0)), (((499, 1), (0, -29)), (-14471, 0)), (((-29, 499), (0, -29)), (841, 0)), (((-1, 499), (0, -29)), (29, 0)), (((0, 499), (0, -29)), (0, 0)), (((1, 499), (0, -29)), (-29, 0)), (((499, 499), (0, -29)), (-14471, 0)), (((-29, -29), (1, -29)), (841, -29)), (((-1, -29), (1, -29)), (29, -29)), (((0, -29), (1, -29)), (0, -29)), (((1, -29), (1, -29)), (-29, -29)), (((499, -29), (1, -29)), (-14471, -29)), (((-29, -1), (1, -29)), (841, -1)), (((-1, -1), (1, -29)), (29, -1)), (((0, -1), (1, -29)), (0, -1)), (((1, -1), (1, -29)), (-29, -1)), (((499, -1), (1, -29)), (-14471, -1)), (((-29, 1), (1, -29)), (841, 1)), (((-1, 1), (1, -29)), (29, 1)), (((0, 1), (1, -29)), (0, 1)), (((1, 1), (1, -29)), (-29, 1)), (((499, 1), (1, -29)), (-14471, 1)), (((-29, 499), (1, -29)), (841, 499)), (((-1, 499), (1, -29)), (29, 499)), (((0, 499), (1, -29)), (0, 499)), (((1, 499), (1, -29)), (-29, 499)), (((499, 499), (1, -29)), (-14471, 499)), (((-29, -29), (499, -29)), (841, -14471)), (((-1, -29), (499, -29)), (29, -14471)), (((0, -29), (499, -29)), (0, -14471)), (((1, -29), (499, -29)), (-29, -14471)), (((499, -29), (499, -29)), (-14471, -14471)), (((-29, -1), (499, -29)), (841, -499)), (((-1, -1), (499, -29)), (29, -499)), (((0, -1), (499, -29)), (0, -499)), (((1, -1), (499, -29)), (-29, -499)), (((499, -1), (499, -29)), (-14471, -499)), (((-29, 1), (499, -29)), (841, 499)), (((-1, 1), (499, -29)), (29, 499)), (((0, 1), (499, -29)), (0, 499)), (((1, 1), (499, -29)), (-29, 499)), (((499, 1), (499, -29)), (-14471, 499)), (((-29, 499), (499, -29)), (841, 249001)), (((-1, 499), (499, -29)), (29, 249001)), (((0, 499), (499, -29)), (0, 249001)), (((1, 499), (499, -29)), (-29, 249001)), (((499, 499), (499, -29)), (-14471, 249001)), (((-29, -29), (-29, -1)), (29, 841)), (((-1, -29), (-29, -1)), (1, 841)), (((0, -29), (-29, -1)), (0, 841)), (((1, -29), (-29, -1)), (-1, 841)), (((499, -29), (-29, -1)), (-499, 841)), (((-29, -1), (-29, -1)), (29, 29)), (((-1, -1), (-29, -1)), (1, 29)), (((0, -1), (-29, -1)), (0, 29)), (((1, -1), (-29, -1)), (-1, 29)), (((499, -1), (-29, -1)), (-499, 29)), (((-29, 1), (-29, -1)), (29, -29)), (((-1, 1), (-29, -1)), (1, -29)), (((0, 1), (-29, -1)), (0, -29)), (((1, 1), (-29, -1)), (-1, -29)), (((499, 1), (-29, -1)), (-499, -29)), (((-29, 499), (-29, -1)), (29, -14471)), (((-1, 499), (-29, -1)), (1, -14471)), (((0, 499), (-29, -1)), (0, -14471)), (((1, 499), (-29, -1)), (-1, -14471)), (((499, 499), (-29, -1)), (-499, -14471)), (((-29, -29), (-1, -1)), (29, 29)), (((-1, -29), (-1, -1)), (1, 29)), (((0, -29), (-1, -1)), (0, 29)), (((1, -29), (-1, -1)), (-1, 29)), (((499, -29), (-1, -1)), (-499, 29)), (((-29, -1), (-1, -1)), (29, 1)), (((-1, -1), (-1, -1)), (1, 1)), (((0, -1), (-1, -1)), (0, 1)), (((1, -1), (-1, -1)), (-1, 1)), (((499, -1), (-1, -1)), (-499, 1)), (((-29, 1), (-1, -1)), (29, -1)), (((-1, 1), (-1, -1)), (1, -1)), (((0, 1), (-1, -1)), (0, -1)), (((1, 1), (-1, -1)), (-1, -1)), (((499, 1), (-1, -1)), (-499, -1)), (((-29, 499), (-1, -1)), (29, -499)), (((-1, 499), (-1, -1)), (1, -499)), (((0, 499), (-1, -1)), (0, -499)), (((1, 499), (-1, -1)), (-1, -499)), (((499, 499), (-1, -1)), (-499, -499)), (((-29, -29), (0, -1)), (29, 0)), (((-1, -29), (0, -1)), (1, 0)), (((0, -29), (0, -1)), (0, 0)), (((1, -29), (0, -1)), (-1, 0)), (((499, -29), (0, -1)), (-499, 0)), (((-29, -1), (0, -1)), (29, 0)), (((-1, -1), (0, -1)), (1, 0)), (((0, -1), (0, -1)), (0, 0)), (((1, -1), (0, -1)), (-1, 0)), (((499, -1), (0, -1)), (-499, 0)), (((-29, 1), (0, -1)), (29, 0)), (((-1, 1), (0, -1)), (1, 0)), (((0, 1), (0, -1)), (0, 0)), (((1, 1), (0, -1)), (-1, 0)), (((499, 1), (0, -1)), (-499, 0)), (((-29, 499), (0, -1)), (29, 0)), (((-1, 499), (0, -1)), (1, 0)), (((0, 499), (0, -1)), (0, 0)), (((1, 499), (0, -1)), (-1, 0)), (((499, 499), (0, -1)), (-499, 0)), (((-29, -29), (1, -1)), (29, -29)), (((-1, -29), (1, -1)), (1, -29)), (((0, -29), (1, -1)), (0, -29)), (((1, -29), (1, -1)), (-1, -29)), (((499, -29), (1, -1)), (-499, -29)), (((-29, -1), (1, -1)), (29, -1)), (((-1, -1), (1, -1)), (1, -1)), (((0, -1), (1, -1)), (0, -1)), (((1, -1), (1, -1)), (-1, -1)), (((499, -1), (1, -1)), (-499, -1)), (((-29, 1), (1, -1)), (29, 1)), (((-1, 1), (1, -1)), (1, 1)), (((0, 1), (1, -1)), (0, 1)), (((1, 1), (1, -1)), (-1, 1)), (((499, 1), (1, -1)), (-499, 1)), (((-29, 499), (1, -1)), (29, 499)), (((-1, 499), (1, -1)), (1, 499)), (((0, 499), (1, -1)), (0, 499)), (((1, 499), (1, -1)), (-1, 499)), (((499, 499), (1, -1)), (-499, 499)), (((-29, -29), (499, -1)), (29, -14471)), (((-1, -29), (499, -1)), (1, -14471)), (((0, -29), (499, -1)), (0, -14471)), (((1, -29), (499, -1)), (-1, -14471)), (((499, -29), (499, -1)), (-499, -14471)), (((-29, -1), (499, -1)), (29, -499)), (((-1, -1), (499, -1)), (1, -499)), (((0, -1), (499, -1)), (0, -499)), (((1, -1), (499, -1)), (-1, -499)), (((499, -1), (499, -1)), (-499, -499)), (((-29, 1), (499, -1)), (29, 499)), (((-1, 1), (499, -1)), (1, 499)), (((0, 1), (499, -1)), (0, 499)), (((1, 1), (499, -1)), (-1, 499)), (((499, 1), (499, -1)), (-499, 499)), (((-29, 499), (499, -1)), (29, 249001)), (((-1, 499), (499, -1)), (1, 249001)), (((0, 499), (499, -1)), (0, 249001)), (((1, 499), (499, -1)), (-1, 249001)), (((499, 499), (499, -1)), (-499, 249001)), (((-29, -29), (-29, 1)), (-29, 841)), (((-1, -29), (-29, 1)), (-1, 841)), (((0, -29), (-29, 1)), (0, 841)), (((1, -29), (-29, 1)), (1, 841)), (((499, -29), (-29, 1)), (499, 841)), (((-29, -1), (-29, 1)), (-29, 29)), (((-1, -1), (-29, 1)), (-1, 29)), (((0, -1), (-29, 1)), (0, 29)), (((1, -1), (-29, 1)), (1, 29)), (((499, -1), (-29, 1)), (499, 29)), (((-29, 1), (-29, 1)), (-29, -29)), (((-1, 1), (-29, 1)), (-1, -29)), (((0, 1), (-29, 1)), (0, -29)), (((1, 1), (-29, 1)), (1, -29)), (((499, 1), (-29, 1)), (499, -29)), (((-29, 499), (-29, 1)), (-29, -14471)), (((-1, 499), (-29, 1)), (-1, -14471)), (((0, 499), (-29, 1)), (0, -14471)), (((1, 499), (-29, 1)), (1, -14471)), (((499, 499), (-29, 1)), (499, -14471)), (((-29, -29), (-1, 1)), (-29, 29)), (((-1, -29), (-1, 1)), (-1, 29)), (((0, -29), (-1, 1)), (0, 29)), (((1, -29), (-1, 1)), (1, 29)), (((499, -29), (-1, 1)), (499, 29)), (((-29, -1), (-1, 1)), (-29, 1)), (((-1, -1), (-1, 1)), (-1, 1)), (((0, -1), (-1, 1)), (0, 1)), (((1, -1), (-1, 1)), (1, 1)), (((499, -1), (-1, 1)), (499, 1)), (((-29, 1), (-1, 1)), (-29, -1)), (((-1, 1), (-1, 1)), (-1, -1)), (((0, 1), (-1, 1)), (0, -1)), (((1, 1), (-1, 1)), (1, -1)), (((499, 1), (-1, 1)), (499, -1)), (((-29, 499), (-1, 1)), (-29, -499)), (((-1, 499), (-1, 1)), (-1, -499)), (((0, 499), (-1, 1)), (0, -499)), (((1, 499), (-1, 1)), (1, -499)), (((499, 499), (-1, 1)), (499, -499)), (((-29, -29), (0, 1)), (-29, 0)), (((-1, -29), (0, 1)), (-1, 0)), (((0, -29), (0, 1)), (0, 0)), (((1, -29), (0, 1)), (1, 0)), (((499, -29), (0, 1)), (499, 0)), (((-29, -1), (0, 1)), (-29, 0)), (((-1, -1), (0, 1)), (-1, 0)), (((0, -1), (0, 1)), (0, 0)), (((1, -1), (0, 1)), (1, 0)), (((499, -1), (0, 1)), (499, 0)), (((-29, 1), (0, 1)), (-29, 0)), (((-1, 1), (0, 1)), (-1, 0)), (((0, 1), (0, 1)), (0, 0)), (((1, 1), (0, 1)), (1, 0)), (((499, 1), (0, 1)), (499, 0)), (((-29, 499), (0, 1)), (-29, 0)), (((-1, 499), (0, 1)), (-1, 0)), (((0, 499), (0, 1)), (0, 0)), (((1, 499), (0, 1)), (1, 0)), (((499, 499), (0, 1)), (499, 0)), (((-29, -29), (1, 1)), (-29, -29)), (((-1, -29), (1, 1)), (-1, -29)), (((0, -29), (1, 1)), (0, -29)), (((1, -29), (1, 1)), (1, -29)), (((499, -29), (1, 1)), (499, -29)), (((-29, -1), (1, 1)), (-29, -1)), (((-1, -1), (1, 1)), (-1, -1)), (((0, -1), (1, 1)), (0, -1)), (((1, -1), (1, 1)), (1, -1)), (((499, -1), (1, 1)), (499, -1)), (((-29, 1), (1, 1)), (-29, 1)), (((-1, 1), (1, 1)), (-1, 1)), (((0, 1), (1, 1)), (0, 1)), (((1, 1), (1, 1)), (1, 1)), (((499, 1), (1, 1)), (499, 1)), (((-29, 499), (1, 1)), (-29, 499)), (((-1, 499), (1, 1)), (-1, 499)), (((0, 499), (1, 1)), (0, 499)), (((1, 499), (1, 1)), (1, 499)), (((499, 499), (1, 1)), (499, 499)), (((-29, -29), (499, 1)), (-29, -14471)), (((-1, -29), (499, 1)), (-1, -14471)), (((0, -29), (499, 1)), (0, -14471)), (((1, -29), (499, 1)), (1, -14471)), (((499, -29), (499, 1)), (499, -14471)), (((-29, -1), (499, 1)), (-29, -499)), (((-1, -1), (499, 1)), (-1, -499)), (((0, -1), (499, 1)), (0, -499)), (((1, -1), (499, 1)), (1, -499)), (((499, -1), (499, 1)), (499, -499)), (((-29, 1), (499, 1)), (-29, 499)), (((-1, 1), (499, 1)), (-1, 499)), (((0, 1), (499, 1)), (0, 499)), (((1, 1), (499, 1)), (1, 499)), (((499, 1), (499, 1)), (499, 499)), (((-29, 499), (499, 1)), (-29, 249001)), (((-1, 499), (499, 1)), (-1, 249001)), (((0, 499), (499, 1)), (0, 249001)), (((1, 499), (499, 1)), (1, 249001)), (((499, 499), (499, 1)), (499, 249001)), (((-29, -29), (-29, 499)), (-14471, 841)), (((-1, -29), (-29, 499)), (-499, 841)), (((0, -29), (-29, 499)), (0, 841)), (((1, -29), (-29, 499)), (499, 841)), (((499, -29), (-29, 499)), (249001, 841)), (((-29, -1), (-29, 499)), (-14471, 29)), (((-1, -1), (-29, 499)), (-499, 29)), (((0, -1), (-29, 499)), (0, 29)), (((1, -1), (-29, 499)), (499, 29)), (((499, -1), (-29, 499)), (249001, 29)), (((-29, 1), (-29, 499)), (-14471, -29)), (((-1, 1), (-29, 499)), (-499, -29)), (((0, 1), (-29, 499)), (0, -29)), (((1, 1), (-29, 499)), (499, -29)), (((499, 1), (-29, 499)), (249001, -29)), (((-29, 499), (-29, 499)), (-14471, -14471)), (((-1, 499), (-29, 499)), (-499, -14471)), (((0, 499), (-29, 499)), (0, -14471)), (((1, 499), (-29, 499)), (499, -14471)), (((499, 499), (-29, 499)), (249001, -14471)), (((-29, -29), (-1, 499)), (-14471, 29)), (((-1, -29), (-1, 499)), (-499, 29)), (((0, -29), (-1, 499)), (0, 29)), (((1, -29), (-1, 499)), (499, 29)), (((499, -29), (-1, 499)), (249001, 29)), (((-29, -1), (-1, 499)), (-14471, 1)), (((-1, -1), (-1, 499)), (-499, 1)), (((0, -1), (-1, 499)), (0, 1)), (((1, -1), (-1, 499)), (499, 1)), (((499, -1), (-1, 499)), (249001, 1)), (((-29, 1), (-1, 499)), (-14471, -1)), (((-1, 1), (-1, 499)), (-499, -1)), (((0, 1), (-1, 499)), (0, -1)), (((1, 1), (-1, 499)), (499, -1)), (((499, 1), (-1, 499)), (249001, -1)), (((-29, 499), (-1, 499)), (-14471, -499)), (((-1, 499), (-1, 499)), (-499, -499)), (((0, 499), (-1, 499)), (0, -499)), (((1, 499), (-1, 499)), (499, -499)), (((499, 499), (-1, 499)), (249001, -499)), (((-29, -29), (0, 499)), (-14471, 0)), (((-1, -29), (0, 499)), (-499, 0)), (((0, -29), (0, 499)), (0, 0)), (((1, -29), (0, 499)), (499, 0)), (((499, -29), (0, 499)), (249001, 0)), (((-29, -1), (0, 499)), (-14471, 0)), (((-1, -1), (0, 499)), (-499, 0)), (((0, -1), (0, 499)), (0, 0)), (((1, -1), (0, 499)), (499, 0)), (((499, -1), (0, 499)), (249001, 0)), (((-29, 1), (0, 499)), (-14471, 0)), (((-1, 1), (0, 499)), (-499, 0)), (((0, 1), (0, 499)), (0, 0)), (((1, 1), (0, 499)), (499, 0)), (((499, 1), (0, 499)), (249001, 0)), (((-29, 499), (0, 499)), (-14471, 0)), (((-1, 499), (0, 499)), (-499, 0)), (((0, 499), (0, 499)), (0, 0)), (((1, 499), (0, 499)), (499, 0)), (((499, 499), (0, 499)), (249001, 0)), (((-29, -29), (1, 499)), (-14471, -29)), (((-1, -29), (1, 499)), (-499, -29)), (((0, -29), (1, 499)), (0, -29)), (((1, -29), (1, 499)), (499, -29)), (((499, -29), (1, 499)), (249001, -29)), (((-29, -1), (1, 499)), (-14471, -1)), (((-1, -1), (1, 499)), (-499, -1)), (((0, -1), (1, 499)), (0, -1)), (((1, -1), (1, 499)), (499, -1)), (((499, -1), (1, 499)), (249001, -1)), (((-29, 1), (1, 499)), (-14471, 1)), (((-1, 1), (1, 499)), (-499, 1)), (((0, 1), (1, 499)), (0, 1)), (((1, 1), (1, 499)), (499, 1)), (((499, 1), (1, 499)), (249001, 1)), (((-29, 499), (1, 499)), (-14471, 499)), (((-1, 499), (1, 499)), (-499, 499)), (((0, 499), (1, 499)), (0, 499)), (((1, 499), (1, 499)), (499, 499)), (((499, 499), (1, 499)), (249001, 499)), (((-29, -29), (499, 499)), (-14471, -14471)), (((-1, -29), (499, 499)), (-499, -14471)), (((0, -29), (499, 499)), (0, -14471)), (((1, -29), (499, 499)), (499, -14471)), (((499, -29), (499, 499)), (249001, -14471)), (((-29, -1), (499, 499)), (-14471, -499)), (((-1, -1), (499, 499)), (-499, -499)), (((0, -1), (499, 499)), (0, -499)), (((1, -1), (499, 499)), (499, -499)), (((499, -1), (499, 499)), (249001, -499)), (((-29, 1), (499, 499)), (-14471, 499)), (((-1, 1), (499, 499)), (-499, 499)), (((0, 1), (499, 499)), (0, 499)), (((1, 1), (499, 499)), (499, 499)), (((499, 1), (499, 499)), (249001, 499)), (((-29, 499), (499, 499)), (-14471, 249001)), (((-1, 499), (499, 499)), (-499, 249001)), (((0, 499), (499, 499)), (0, 249001)), (((1, 499), (499, 499)), (499, 249001)), (((499, 499), (499, 499)), (249001, 249001))]

    minimums = [([(0, 499), (1, 499), (499, -1), (499, 499), (499, 499), (0, -1), (-29, -29), (-29, -1)], (499, -1)), ([(-1, -29), (-29, -1), (-29, -29)], (-1, -29)), ([(499, 1), (499, -29), (499, 1), (0, 1), (-29, 1), (0, 1), (-1, -1), (0, -29)], (-29, 1)), ([(-29, 499), (-29, -29), (1, -1), (-29, -1), (-1, -1), (-29, 499), (1, 1), (-1, -1), (499, 1)], (1, -1)), ([(-1, 1), (-29, 1), (1, 499), (499, 1), (-29, 1), (499, 499), (-29, -1), (-1, -29), (-1, -29)], (-29, 1)), ([(499, 1), (1, -1), (0, 499), (0, 499), (0, -29), (1, 1), (0, -1), (-1, 1), (0, 499)], (-1, 1)), ([(1, 499), (1, 1), (-29, 1), (-29, 499), (0, -29)], (-29, 1)), ([(0, -1)], (0, -1)), ([(499, 1)], (499, 1)), ([(-29, 499), (499, 1), (1, 1), (-1, -1), (499, 499), (499, 1)], (-29, 499)), ([(1, 499), (-1, 499), (0, 499), (1, -29), (0, -29), (-29, 499), (499, -1), (-29, 499), (0, -1)], (499, -1)), ([(0, -29), (499, -29), (499, -29)], (499, -29)), ([(-1, 1), (499, -1), (-1, 499), (0, 1), (499, -29), (1, 499), (0, -29)], (499, -1)), ([(499, -29), (499, -29), (-29, 1)], (-29, 1)), ([(1, -29), (0, 499), (1, -1), (1, 1)], (1, -1)), ([(0, 499), (-1, 499), (499, -1), (-29, -29), (499, -1), (1, 499), (-1, 499)], (499, -1)), ([(1, -29), (499, 499), (-1, -29), (0, -1)], (1, -29)), ([(1, -29), (0, -29), (1, -29)], (1, -29)), ([(1, 1), (-29, -1)], (1, 1)), ([(-29, -29), (-1, 1), (-1, 499), (-1, 499), (-29, -1), (499, 499)], (-1, 1))]

    def test_multiplications(self):
        from fractions import multiply

        for input_fractions, expected_output in FractionsTests.multiplications:
            with self.subTest(i=input_fractions):
                output = multiply(input_fractions[0], input_fractions[1])
                self.assertEqual(output, expected_output)

    def test_divide(self):
        from fractions import divide

        for input_fractions, expected_output in FractionsTests.divisions:
            with self.subTest(i=input_fractions):
                output = divide(input_fractions[0], input_fractions[1])
                self.assertEqual(output, expected_output)

    def test_minimums(self):
        from fractions import find_minimum

        for input_fractions, expected_output in FractionsTests.minimums:
            with self.subTest(i=input_fractions):
                output = find_minimum(input_fractions)
                self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()