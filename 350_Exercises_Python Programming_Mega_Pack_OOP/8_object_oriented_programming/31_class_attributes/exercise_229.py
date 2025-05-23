'''
Implement a class named OnlineShop with the class attributes set appropriately:
sector to the value 'electronics'
sector_code to the value 'ELE'
is_public_company to the value False
Then, using dot notation, add a class attribute called country and set its value to 'USA'.
In response, print the user-defined OnlineShop class attribute names as shown below.
Expected result:
['sector', 'sector_code', 'is_public_company', 'country']
'''


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


OnlineShop.country = 'USA'
attrs = [attr for attr in OnlineShop.__dict__ if not attr.startswith('__')]
print(attrs)
