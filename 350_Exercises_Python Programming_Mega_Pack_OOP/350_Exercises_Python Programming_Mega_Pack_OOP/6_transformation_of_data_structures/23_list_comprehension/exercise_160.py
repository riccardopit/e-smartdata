'''
The contents of the file plw.txt were loaded as follows:
with open('plw.txt', 'r') as file:
    lines = file.read().splitlines()
lines variable:
Tasks to perform:
1. Get rid of blank lines.
2. Split each line into tokens/words as shown below and print result to the console.
Expected result:
[
    ['PLAYWAY'],
    [
        'PlayWay',
        'is',
        'a',
        'producer',
        'and',
        'publisher',
        'of',
        'computer',
        'and',
        'mobile',
        'games.',
        'The',
        'company',
        'is',
        'characterized',
        'by',
        'a',
        'very',
        'large',
        'number',
        'of',
        'development',
        'teams',
        'and',
        'a',
        'large',
        'number',
        'of',
        'games',
        'produced',
        'simultaneously.'
    ],
    [
        'PlayWay',
        'sells,',
        'among',
        'others',
        'via',
        'the',
        'STEAM',
        'portal,',
        'AppStore',
        'and',
        'GooglePlay.',
        'The',
        'US',
        'and',
        'German',
        'markets',
        'are',
        'the',
        'two',
        'largest',
        'markets',
        'for',
        'the',
        "Group's",
        'sales.'
    ],
    [
        'In',
        'addition,',
        'the',
        'company',
        'has',
        'PlayWay',
        'Campus',
        '-',
        'a',
        'campus',
        'for',
        'cooperating',
        'development',
        'teams.'
    ]
]
'''

import os.path

file_name = 'plw.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)

with open(file_path, 'r') as file:
    lines = file.read().splitlines()
words = [line.split() for line in lines if len(line) > 0]
print(words)
