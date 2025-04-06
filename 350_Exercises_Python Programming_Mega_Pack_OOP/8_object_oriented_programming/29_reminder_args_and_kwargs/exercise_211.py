'''
Implement a function called display_info() which prints the name of the company (as shown below)
and if the user also passes an argument named price, it prints the price (as shown below).
Example I:
[IN]: display_info(company='Apple')
Company name: Apple
Example II:
[IN]: display_info(company='Apple', price=114)
Company name: Apple
Price: $ 114
In response, call display_info() as shown below:
display_info(company='CD Projekt', price=100)
Expected result:
Company name: CD Projekt
Price: $ 100
'''


def display_info(**kwargs):
    if 'company' in kwargs:
        print(f"Company name: {kwargs['company']}")
    if 'price' in kwargs:
        print(f"Price: $ {kwargs['price']}")


display_info(company='CD Projekt', price=100)
