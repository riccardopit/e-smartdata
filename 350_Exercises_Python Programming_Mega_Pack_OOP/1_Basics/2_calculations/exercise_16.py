'''
The quadratic equation is given with the following formula:
x² + 5x + 4 = 0
Using Vieta's formulas calculate the sum and product of the roots of this quadratic equation.
Print the result to the console as shown below.
Expected result:
x1 + x2 = -5.0
x1x2 = 4.0
'''

a = 1
b = 5
c = 4
sum_roots = -b / a
product_roots = c / a
print(f"x1 + x2 = {sum_roots:.1f}")
print(f"x1x2 = {product_roots:.1f}")
