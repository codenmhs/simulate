from vector import Particle
import unittest


class KnownOutput(unittest.TestCase):
    part1 = Particle([1, 2, 3], [3, 2, 1], 3, 'red')
    part2 = Particle([0, 0, 0], [2, 3, 1], 10, 'purple')

    # Known velocity vectors after apply_forces(part1, part2, 2)
    known_velocities = (
        [-0.054414193284849866, -4.1088283865697, -8.16324257985455], 
        [2.916324257985455, 4.83264851597091, 3.7489727739563654]
    )
    # Known positions after doing above apply_forces then incrementing part1 and part2 with step_size 2
    known_positions = (
        [0.7823432268606005, -14.435313546278799, -29.652970319418202],
        [11.66529703194182, 19.33059406388364, 14.995891095825462]
    )

    def test_apply_forces(self):
        self.part1.apply_forces(self.part2, 2)
        self.assertEqual(
            (self.part1.velocity.position, self.part2.velocity.position),
            self.known_velocities
        )

    def test_increment(self):
        self.part1.increment(2)
        self.part2.increment(2)
        self.assertEqual(
            (self.part1.position, self.part2.position),
            self.known_positions
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)