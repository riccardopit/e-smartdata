'''
Implement a class called Car that sets the following instance attributes when creating an instance:
brand
model
price
type_of_car, by default 'sedan'
Then create an instance named car with the given values:
brand = 'Opel'
model = 'Insignia'
price = 115000
In response, print the value of the __dict__ attribute of the car instance.
Expected result:
{'brand': 'Opel', 'model': 'Insignia', 'price': 115000, 'type_of_car': 'sedan'}
'''


class Car:

    def __init__(self, brand, model, price, type_of_car=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car if type_of_car else 'sedan'


car = Car('BMW', 'X3', 200000, 'SUV')
print(car.__dict__)
