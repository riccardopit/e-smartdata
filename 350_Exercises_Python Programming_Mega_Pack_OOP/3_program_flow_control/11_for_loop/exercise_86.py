'''
Write a program that finds all two-digit numbers divisible by 11 (use a for loop).
Print the result to the console as comma-separated values as shown below.
Expected result:
11,22,33,44,55,66,77,88,99
'''

nums = []
for x in range(11, 100, 11):
    nums.append(str(x))
print(','.join(nums))
