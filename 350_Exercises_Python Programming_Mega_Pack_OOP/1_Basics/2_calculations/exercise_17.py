'''
Calculate the midpoint of the segment with ends at the points: A = (2, 4), B = (-4, 6)
and print result to the console as shown below.
Expected result:
The middle point: (-1.0, 5.0)
'''

A = (2, 4)
B = (-4, 6)
midpoint = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
print(f"The middle point: {midpoint}")
