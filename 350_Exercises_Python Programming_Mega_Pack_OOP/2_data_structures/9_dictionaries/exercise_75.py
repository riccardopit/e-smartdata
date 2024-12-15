'''
The following dictionary is given:
project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
Extract a list of unique values (sorted alphabetically) from the project_ids dictionary and print it to the console.
Expected result:
['completed', 'in progress', 'open']
'''

project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
project_values = sorted(set(project_ids.values()))
print(project_values)
