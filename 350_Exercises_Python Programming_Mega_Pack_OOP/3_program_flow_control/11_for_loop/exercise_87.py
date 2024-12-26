'''
Write a program that finds all two-digit numbers divisible by 11 and indivisible by 3 (use a for loop).
Print the result to the console as comma-separated values as shown below.
Expected result:
11,22,44,55,77,88
'''

nums = []
for x in range(11, 100, 11):
    if x % 3 != 0:
        nums.append(str(x))
print(','.join(nums))
