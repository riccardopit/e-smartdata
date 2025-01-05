'''
Read the currencies.txt file. Each line has a different currency pair.
Create a list with the names of currency pairs containing the 'USD' symbol.
Expected result:
['ARSUSD', 'AUDUSD']
'''

import os.path

file_name = 'currencies.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
with open(file_path, 'r') as file:
    lines = file.read().splitlines()
    result = [line for line in lines if 'USD' in line]
print(result)
