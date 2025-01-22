'''
Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console as shown below.
Expected result:
Geometric average of the given numbers: 4.05
'''

nums = [4, 3, 4.5, 5]
mean = 1
for n in nums:
    mean *= n
mean = mean**(1 / len(nums))
print(f"Geometric average of the given numbers: {mean:.2f}")
