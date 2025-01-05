'''
The following list of indexes is given:
indeks = ['WIG20', 'mWIG40', 'sWIG80']
and a list of properties for each index:
properties = ['number of companies', 'companies', 'cap']
Using dict comprehension, create a following dictionary.
Set the default value of each property to None and print the result to the console.
Expected result:
{'WIG20': {'cap': None, 'companies': None, 'number of companies': None},
 'mWIG40': {'cap': None, 'companies': None, 'number of companies': None},
 'sWIG80': {'cap': None, 'companies': None, 'number of companies': None}}
'''

indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['number of companies', 'companies', 'cap']
result = {indek: {propertie: None for propertie in properties} for indek in indeks}
print(result)
