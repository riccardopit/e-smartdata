'''
A class named Circle is given. Add a property to the class called perimeter (read-only)
that calculates the length of circle with a given radius.
This property should be computed only at the first reading or after modifying the radius attribute.
To do this, also modify the way of setting the value of the radius attribute in the __init __() method.
Make sure that the value of the perimeter attribute is recalculated when the radius attribute is changed.
Then create an instance named circle with radius=3.
In response, display the value of the perimeter attribute to the console (round the result to four decimal places).
Expected result:
18.8496
'''

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius ** 2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = math.pi * self._radius * 2
        return self._perimeter


circle = Circle(3)
print(round(circle.perimeter, 4))
