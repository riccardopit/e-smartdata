'''
An infinite geometric sequence is given with the following formula:
1, 1/2, 1/4, 1/8
Calculate the sum of this sequence. Print the result to the console as shown below.
Expected result:
The sum of the sequence: 2.0
'''

a = 1
b = 1 / 2
sum = a / (1 - b)
print(f"The sum of the sequence: {sum:.1f}")
