'''
The Person class is implemented. Add a special method __str__()
to return an informal representation of an instance of the Person class.
Example:
[IN]: person = Person('Mike', 'Smith')
[IN]: print(person)
First name: Mike
Last name: Smith
Then create an instance named person with the following values:
fname = 'John'
lname = 'Doe'
In response, print the person instance to the console.
Expected result:
First name: John
Last name: Doe
'''


class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"{self.__class__.__name__}(fname='{self.fname}', lname='{self.lname}')"

    def __str__(self):
        return f"First name: {self.fname}\nLast name: {self.lname}"


person = Person('John', 'Doe')
print(person)
