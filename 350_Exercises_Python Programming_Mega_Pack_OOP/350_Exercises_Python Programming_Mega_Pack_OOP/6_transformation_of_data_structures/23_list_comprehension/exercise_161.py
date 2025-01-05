'''
The contents of the file plw.txt were loaded as follows:
with open('plw.txt', 'r') as file:
    lines = file.read()
Tasks to perform:
1. Change uppercase letters to lowercase
2. Remove commas and periods
3. Split the text into tokens
4. Extract words with minimum 8 characters length
5. Sort the words alphabetically
Print the result to the console.
Expected result:
['addition', 'appstore', 'characterized', 'computer', 'cooperating', 'development',
'development', 'googleplay', 'produced', 'producer', 'publisher', 'simultaneously']
'''

import os.path

file_name = 'plw.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
with open(file_path, 'r') as file:
    lines = file.read()
lines = lines.lower().replace('.', '').replace(',', '')
words = lines.split()
words = sorted([word for word in words if len(word) >= 8])
print(words)
