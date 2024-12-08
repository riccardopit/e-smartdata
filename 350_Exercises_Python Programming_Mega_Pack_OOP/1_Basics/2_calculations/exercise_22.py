'''
Calculate the standard deviation of the following set of data: 10, 11, 9.
Print the result to the console as shown below.
Expected result:
The standard deviation: 0.82
'''

nums = [10, 11, 9]
avg = sum(nums) / len(nums)
var = sum([(n - avg)**2 for n in nums]) / len(nums)
std = var**0.5
print(f"The standard deviation: {std:.2f}")
