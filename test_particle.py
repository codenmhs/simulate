from vector import Vector, Particle
import unittest
import numpy as np


class KnownOutput(unittest.TestCase):
    part1 = Particle([1, 2, 3], [3, 2, 1], 3, 'red')
    part2 = Particle([0, 0, 0], [2, 3, 1], 10, 'purple')

    # Known velocity vectors after part1.apply_forces(part2, 2)
    known_velocities = {
        'part1': Vector([2.618198225839394, 1.2363964516787875, -0.1454053224818188]),
        'part2': Vector([2.114540532248182, 3.2290810644963637, 1.3436215967445457])
    }
    # Known positions after doing above apply_forces then incrementing part1 and part2 with step_size 10
    known_positions = {
        'part1': Vector([27.181982258393937, 14.363964516787876, 1.545946775181812]),
        'part2': Vector([21.145405322481817, 32.290810644963635, 13.436215967445458])
    }

    def test_apply_forces(self):
        self.part1.apply_forces(self.part2, 2)

        self.assertTrue(self.part1.velocity == self.known_velocities['part1'])
        self.assertTrue(self.part2.velocity == self.known_velocities['part2'])

    def test_increment(self):
        self.part1.increment(10)
        self.part2.increment(10)

        self.assertTrue(self.part1 == self.known_positions['part1'])
        self.assertTrue(self.part2 == self.known_positions['part2'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
