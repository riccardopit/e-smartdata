'''
Implement a function called multi(), which accepts an iterable object (list, tuple) as an argument
and returns the product of all elements of this iterable object.
Example:
[IN]: multi((-4, 6, 2))
[OUT]: -48
[IN]: multi([4, 2, -5])
[OUT]: -40
Note! You only need to define the function.
'''


def multi(nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multi((-4, 6, 2)))
print(multi([4, 2, -5]))
