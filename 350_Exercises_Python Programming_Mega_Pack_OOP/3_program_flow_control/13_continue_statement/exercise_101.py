'''
The list of companies from the WIG.GAMES index is given with the closing price and currency:
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
Using the continue statement, create a for loop that will change the closing price from USD to PLN in this dictionary.
Take USDPLN = 4.0.
In response, print the gaming dictionary to the console.
Expected result:
{'11B': [362.5, 'PLN'], 'CDR': [297.0, 'PLN'], 'CIG': [0.85, 'PLN'], 'PLW': [318.0, 'PLN'], 'TEN': [300.0, 'PLN']}
'''

gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}
USDPLN = 4.0
for v in gaming.values():
    if v[1] == 'PLN':
        continue
    v[0] = v[0] * USDPLN
    v[1] = 'PLN'
print(gaming)
