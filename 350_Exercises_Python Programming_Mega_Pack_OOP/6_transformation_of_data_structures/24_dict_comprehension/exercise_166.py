'''
The following dictionary is given:
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}
Using dict comprehension, extract a key: value pair from the dictionary with a value greater than 100
and print the result to the console.
Expected result:
{'CD Projekt': 295, 'Playway': 350}
'''

stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 3}
result = {k: v for k, v in stocks.items() if v > 100}
print(result)
