'''
An implementation of the Vector class is given. Create the following instances of this class:
v1 = Vector(4, 2)
v2 = Vector(-1, 3)
Then try to add these instances, i.e. perform the operation v1 + v2.
If there is an error, print the error message to the console. Use a try ... except ... clause in your solution.
Expected result:
unsupported operand type(s) for +: 'Vector' and 'Vector'
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


v1 = Vector(4, 2)
v2 = Vector(-1, 3)
try:
    v1 + v2
except Exception as e:
    print(e)
