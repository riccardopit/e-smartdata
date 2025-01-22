'''
Implement a function called factorial() that calculates the factorial for a given number.
Example:
[IN]: factorial(6)
[OUT]: 720
[IN]: factorial(10)
[OUT]: 3628800
Note! You only need to define the function.
'''


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

print(factorial(6))
print(factorial(10))
