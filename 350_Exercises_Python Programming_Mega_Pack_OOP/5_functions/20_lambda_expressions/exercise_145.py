'''
The following list is given:
items = ['P-1', 'R-2', 'D-4', 'F-6']
Using the map() function and the lambda expression, get rid of the '-' (dash) from each element
and print items list on the console.
Expected result:
['P1', 'R2', 'D4', 'F6']
'''


items = ['P-1', 'R-2', 'D-4', 'F-6']
items_clean = list(map(lambda stock: stock.replace('-', ''), items))
print(items_clean)
