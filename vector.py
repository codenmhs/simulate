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
            output.position[i] = self.position[i] * scalar * 2
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