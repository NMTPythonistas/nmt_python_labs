import unittest
import functools


class BezierTest(unittest.TestCase):
    test_points = [((0,0), (200,400), (200,0), (50, 200), 2, [(0, 0), (50, 200)]),
                   ((0,0), (200,400), (200,0), (50, 200), 5, [(0.0, 0.0), (113.28125, 171.875), (156.25, 175.0), (133.59375, 140.625), (50.0, 200.0)]),
                   ((0, 0), (50, 180), (100, 100), (100, 200), 3, [(0.0, 0.0), (68.75, 130.0), (100.0, 200.0)]),
                   ((0, 0), (50, 180), (100, 100), (100, 200), 10, [(0.0, 0.0), (16.598079561042525, 50.97393689986283), (32.78463648834019, 86.31001371742113), (48.14814814814815, 109.62962962962965), (62.27709190672154, 124.55418381344307), (74.75994513031551, 134.7050754458162), (85.18518518518519, 143.7037037037037), (93.14128943758573, 155.17146776406037), (98.21673525377228, 172.72976680384087), (100.0, 200.0)])]

    def test_bezier(self):
        from bezier import cubic_bezier

        for p1, p2, p3, p4, point_count, expected_output in BezierTest.test_points:
            with self.subTest(i=(p1, p2, p3, p4, point_count)):
                point_count = len(expected_output)
                output = cubic_bezier(p1, p2, p3, p4, point_count)
                close_enough = 0.01
                output_close_to_expected_output = functools.reduce(
                    lambda t, b: t and b,
                    map(lambda o, eo:
                        abs(o[0] - eo[0]) + abs(o[1] - eo[1]) < close_enough,
                        output, expected_output))
                self.assertTrue(output_close_to_expected_output, msg="output and expected output differ too much: \noutput: {}\nexpected: {}".format(output, expected_output))


if __name__ == '__main__':
    unittest.main()
