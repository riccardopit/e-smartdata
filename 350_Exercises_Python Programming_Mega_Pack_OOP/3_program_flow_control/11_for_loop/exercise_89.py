'''
The following list is given:
items = [1, 5, 3, 2, 2, 4, 2, 4]
Write a program that removes duplicates from the list (the order must be kept) and print the list to the console.
Expected result:
[1, 5, 3, 2, 4]
'''

items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []
for item in items:
    if item not in result:
        result.append(item)
print(result)
