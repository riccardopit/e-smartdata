'''
The following classes are implemented:
Vehicle
LandVehicle
AirVehicle
Define a __repr__() special method in the Vehicle class
that returns a formal representation of the objects of the classes Vehicle, LandVehicle, and AirVehicle.
Example: The code below:
instances = [Vehicle(), LandVehicle(), AirVehicle()]
for instance in instances:
    print(instance)
returns:
Vehicle(category='land vehicle')
LandVehicle(category='land vehicle')
AirVehicle(category='air vehicle')
Run the code below in response:
instances = [Vehicle(), LandVehicle(), AirVehicle()]
for instance in instances:
    print(instance)
Expected result:
Vehicle(category='land vehicle')
LandVehicle(category='land vehicle')
AirVehicle(category='air vehicle')
'''


class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'

    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):

    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


instances = [Vehicle(), LandVehicle(), AirVehicle()]

for instance in instances:
    print(instance)
