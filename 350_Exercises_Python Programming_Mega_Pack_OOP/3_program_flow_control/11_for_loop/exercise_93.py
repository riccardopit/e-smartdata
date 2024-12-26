'''
Write a program that creates a histogram as a dictionary of the following values:
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
In response print histogram to the console.
Expected result:
{'x': 3, 'y': 4, 'z': 2}
'''

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
result = {}
for item in items:
    if item not in result:
        result[item] = 1
    else:
        result[item] += 1
print(result)
