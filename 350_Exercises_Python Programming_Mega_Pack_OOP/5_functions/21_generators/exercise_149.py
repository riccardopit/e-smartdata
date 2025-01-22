'''
Implement a generator named dayname() that accepts the index of the element from the following list:
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
and allows us to iterate over 3 days (previous day, present day, next day).
Example:
[IN]:
for pair in dayname(0):
    print(pair)
[OUT]:
Sun
Mon
Tue
Note! All you have to do is define a generator.
'''


def dayname(index):
    index = index % 7
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    yield days[index - 1]
    yield days[index]
    yield days[index + 1]


for pair in dayname(-3):
    print(pair)
