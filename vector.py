import math


class Vector():
    def __init__(self, position: list):
        self.position = position

    def __add__(self, other):
        if len(self.position) != len(other.position):
            raise ValueError('The two vectors have different dimensions.')
        output = [0] * len(self.position)
        for index, item in enumerate(self.position):
            output[index] = item + other.position[index]
        return Vector(output)

    def mult(self, scalar):
        output = Vector([0] * len(self.position))
        for i in range(len(output.position)):
            output.position[i] = self.position[i] * scalar
        return output

    def difference(self, other):
        if len(self.position) != len(other.position):
            raise ValueError('The two vectors have different dimensions.')
        output = [0] * len(self.position)
        for index, item in enumerate(self.position):
            output[index] = other.position[index] - item
        return Vector(output)

    def get_length(self):
        total = 0
        for item in self.position:
            total += item ** 2
        return total ** (1 / 2)

    def get_unit(self):
        if self.get_length() != 0:
            return self.mult(1 / self.get_length())
        return Vector([0] * len(self.position))

    def reverse(self):
        return self.mult(-1)

    def __eq__(self, other):
        error = 0.0001
        if self.difference(other).get_lenth() < error:
            return True
        return False


class Particle(Vector):
    def __init__(self, position: list, velocity: list, mass: float, color: str):
        super().__init__(position)
        self.velocity = Vector(velocity)
        self.mass = float(mass)
        self.color = color
        self.display_size = math.log(self.mass, 1.3)

    def apply_forces(self, other, grav_const):
        '''
            Calculate the mutual gravitation of two particles. 
            Apply the resulting acceleration to their velocities.
        '''
        # Find direction from this particle to the other; normalize it; and then assign magnitude
        # given by the product of their masses and the gravitational constant, divided by the distance squared.
        # Ie, implement F_G1,2 = (G * m1 * m2 / d ** 2) * uv_1,2
        denom = self.difference(other).get_length() ** 2
        if denom == 0.0:
            # If the positions are identical, avoid a divide by 0 and assign 0 mutual force.
            force_on_self = Vector([0] * len(self.position))
        else:
            force_on_self = self.difference(other).get_unit().mult(
                grav_const * self.mass * other.mass / denom)
        accel_on_self = force_on_self.mult(1 / self.mass)
        accel_on_other = force_on_self.mult(-1 / other.mass)
        self.velocity += accel_on_self
        other.velocity += accel_on_other

    def increment(self, step_size):
        '''
            Apply velocities resulting from get_forces to particle positions.
        '''
        self.position = self.__add__(self.velocity.mult(step_size)).position


if __name__ == '__main__':
    part1 = Particle([1, 2, 3], [3, 2, 1], 3)
    part2 = Particle([0, 0, 0], [2, 3, 1], 10)
    part1.increment(part2, 10, 10)
