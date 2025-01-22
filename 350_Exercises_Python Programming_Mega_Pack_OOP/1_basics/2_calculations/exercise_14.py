'''
The arithmetic sequence is given with the following formula:
aₙ = 10 + 4n
Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.
Expected result:
The sum of the first 10 elements in a sequence: 320.0
'''

n = 10
sum = 0
for n in range(1, n + 1):
    sum += 10 + 4 * n
print(f"The sum of the first {n} elements in a sequence: {sum:.1f}")
