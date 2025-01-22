'''
Calculate the distance of two points A = (3, 2), B = (- 1, -1) and print result to the console as shown below.
Expected result:
The distance between points A and B: 5.0
'''

A = (3, 2)
B = (-1, -1)
distance = ((B[0] - A[0])**2 + (B[1] - A[1])**2)**0.5
print(f"The distance between points A and B: {distance}")
