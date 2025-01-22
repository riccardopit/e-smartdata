'''
Implement a function called maximum() that returns the maximum of three numbers. Use conditional statement.
Example:
[IN]: maximum(4, 2, 1)
[OUT]: 4
[IN]: maximum(-3, 2, 5)
[OUT]: 5
Note! You only need to define the function.
'''


def maximum(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z


print(maximum(4, 2, 1))
print(maximum(-3, 2, 5))
