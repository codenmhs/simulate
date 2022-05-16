import vector
from vector import Vector
import unittest


class KnownOutput(unittest.TestCase):
    known_differences = (
        ([0, 0, 0], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [0, 0, 0], [-1, -2, -3])
    )

    known_lengths = (
        ([3, 4, 0], 5.0),
        ([0, 3, 4], 5.0),
        ([3, 0, 4], 5.0),
    )

    known_additions = (
        ([1, 2, 3], [3, 2, 1], [4, 4, 4]),
        ([1, 2, 3], [-1, -2, -3], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3], [2, 4, 6]),
    )

    known_mults = (
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2, 3], -1, [-1, -2, -3]),
        ([1, 2, 3], 2, [2, 4, 6]),
    )

    known_unit_vects = (
        ([1, 2, 3], [0.2672612419124244, 0.5345224838248488, 0.8017837257372732]),
        ([1, 0], [1, 0]),
        ([0, 0, 0, -1], [0, 0, 0, -1])
    )

    def test_known_differences(self):
        for (vec1, vec2, answer) in self.known_differences:
            output = Vector(vec1).difference(Vector(vec2))
            self.assertEqual(output.position, answer)

    def test_known_lengths(self):
        for (vec, answer) in self.known_lengths:
            output = Vector(vec).get_length()
            self.assertEqual(output, answer)

    def test_known_additions(self):
        for (vec1, vec2, answer) in self.known_additions:
            output = Vector(vec1) + Vector(vec2)
            self.assertEqual(output.position, answer)

    def test_known_mults(self):
        for (vec1, scalar, answer) in self.known_mults:
            output = Vector(vec1).mult(scalar)
            self.assertEqual(output.position, answer)

    def test_mismatch_add(self):
        vec1, vec2 = Vector([1, 2, 3]), Vector([1, 2])
        with self.assertRaises(ValueError):
            vec1 + vec2

    def test_mismatch_difference(self):
        vec1, vec2 = Vector([1, 2, 3]), Vector([1, 2])
        with self.assertRaises(ValueError):
            vec1.difference(vec2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
