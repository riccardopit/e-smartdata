'''
Implement a function called filter_ge_6() that takes a list of words
and returns list of words with the length greater than or equal to 6 characters.
Example:
[IN]: filter_ge_6(['programming', 'python', 'java', 'sql'])
[OUT]: ['programming', 'python']
[IN]: filter_ge_6(['java', 'sql'])
[OUT]: []
Note! You only need to define the function.
'''


def filter_ge_6(words):
    return [word for word in words if len(word) >= 6]


print(filter_ge_6(['programming', 'python', 'java', 'sql']))
print(filter_ge_6(['java', 'sql']))
