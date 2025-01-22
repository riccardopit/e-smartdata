'''
The geometric sequence is given with the following formula:
aₙ = 8 * 2ⁿ⁻¹
Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.
Expected result:
The sum of the first 6 elements of the sequence is: 504.0
'''

n = 6
sum = 0
for n in range(1, n + 1):
    sum += 8 * 2**(n - 1)
print(f"The sum of the first {n} elements of the sequence is: {sum:.1f}")
