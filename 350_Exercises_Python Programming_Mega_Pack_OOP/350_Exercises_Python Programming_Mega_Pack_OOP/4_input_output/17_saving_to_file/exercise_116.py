'''
The following dictionary:
stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}
save to stocks.json using the json package. Set the indent to 4.
File stocks.json after saving:
{
    "PLW": [
        "Playway",
        350
    ],
    "BBT": [
        "Boombit",
        22
    ]
}
'''

import json
import os.path

file_name = 'stocks.json'
file_path = os.path.join(os.path.dirname(__file__), file_name)
stocks = {
    'PLW': ['Playway', 350],
    'BBT': ['Boombit', 22]
}
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(stocks, file, indent=4)
