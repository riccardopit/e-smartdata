'''
A class called Laptop was implemented.
Add validation of the price attribute also at the stage of creating the instance (in __init__() method).
Then try to create an instance of the Laptop class with a price of -3499.
If an error is raised, print the error message to the console. Use a try ... except ... clause in your solution.
Expected result:
The price attribute must be a positive int or float value.
'''


class Laptop:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if not (isinstance(price, (int, float))):
            raise TypeError("The price attribute must be an int or float type.")
        if price <= 0:
            raise ValueError("The price attribute must be a positive int or float value.")
        self._price = price


laptop = Laptop(3499)
try:
    laptop.set_price(-3000)
except (TypeError, ValueError) as e:
    print(e)
