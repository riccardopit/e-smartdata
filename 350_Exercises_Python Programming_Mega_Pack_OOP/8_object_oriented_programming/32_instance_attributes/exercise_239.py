'''
The Book class is defined. A list books_data is also given.
books_data = [
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {
        'author': 'Dan Brown',
        'title': 'The Da Vinci Code',
        'year_of_publishment': 2003,
    },
]
Based on this data, create two instances of the Book class, where the instance attributes
will be the keys from the given dictionaries (books_data list) with their corresponding values.
In response, print the __dict__ attributes of the objects to the console as shown below.
Expected result:
{'author': 'Dan Brown', 'title': 'Inferno'}
{'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}
'''


class Book:
    language = 'ENG'
    is_ebook = True


books_data = [
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {
        'author': 'Dan Brown',
        'title': 'The Da Vinci Code',
        'year_of_publishment': 2003,
    },
]

for book_data in books_data:
    book = Book()
    for k, v in book_data.items():
        setattr(book, k, v)
    print(book.__dict__)
