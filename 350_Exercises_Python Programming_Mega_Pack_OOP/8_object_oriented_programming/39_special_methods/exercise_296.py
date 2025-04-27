'''
An implementation of the Vector class is given.
Implement the __sub__() special method that subtracts Vector instances (by coordinates).
For simplicity, assume that the user subtracts vectors of the same length. Then create two instances of this class:
v1 = Vector(4, 2)
v2 = Vector(-1, 3)
and perform the subtraction of these vectors. Print the result to the console.
Expected result:
(5, -1)
'''


class Vector:

    def __init__(self, *args):
        self.components = args

    def __repr__(self):
        return f"{self.__class__.__name__}{self.components}"

    def __str__(self):
        return f"{self.components}"

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        return tuple(x + y for x, y in zip(self.components, other.components))

    def __sub__(self, other):
        return tuple(x - y for x, y in zip(self.components, other.components))


v1 = Vector(4, 2)
v2 = Vector(-1, 3)
print(v1 - v2)
