'''
A class named OnlineShop was defined with the class attributes set accordingly:
sector to the value 'electronics'
sector_code to the value 'ELE'
is_public_company to the value False
Outside of the class, implement a function called describe_attrs()
that displays the names of all user-defined class attributes and their values as shown below.
In response, call the describe_attrs() function.
Expected result:
sector -> electronics
sector_code -> ELE
is_public_company -> False
'''


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


def describe_attrs(object):
    for k, v in object.__dict__.items():
        if not k.startswith('__'):
            print(f"{k} -> {v}")


describe_attrs(OnlineShop)
