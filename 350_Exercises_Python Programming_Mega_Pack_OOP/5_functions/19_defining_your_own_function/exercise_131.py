'''
Implement a function count_str(),
which returns the number of str objects in an iterable object (list, tuple, set).
Example:
[IN]: count_str(['p', 2, 4.3, None])
[OUT]: 1
[IN]: count_str({'p', 2, 4.3, True, 'True', None})
[OUT]: 2
Note! You only need to define the function.
'''


def count_str(items):
    count = 0
    for item in items:
        if isinstance(item, str):
            count += 1
    return count


print(count_str(['p', 2, 4.3, None]))
print(count_str({'p', 2, 4.3, True, 'True', None}))
