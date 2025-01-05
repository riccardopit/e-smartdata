'''
The following list is given:
indexes = ['WIG20', 'mWIG40', 'sWIG80']
Using dict comprehension, convert the above list into the following dictionary:
{0: 'WIG20', 1: 'mWIG40', 2: 'sWIG80'}
Print the result to the console.
'''

indexes = ['WIG20', 'mWIG40', 'sWIG80']
result = {i: index for i, index in enumerate(indexes)}
print(result)
