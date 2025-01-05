'''
The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:
with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
Transform the content of the file to get a dictionary containing two keys: 'Date' and 'Close'.
The values for these keys will be, respectively, lists consisting of all dates and closing prices.
Convert closing prices to float type and print this dictionary to the console as shown below.
Expected result:
{
    'Date': [
        '2020-03-02',
        '2020-03-03',
        '2020-03-04',
        '2020-03-05',
        '2020-03-06',
        '2020-03-09',
        '2020-03-10',
        '2020-03-11',
        '2020-03-12',
        '2020-03-13',
        '2020-03-16',
        '2020-03-17',
        '2020-03-18',
        '2020-03-19',
        '2020-03-20',
        '2020-03-23',
        '2020-03-24',
        '2020-03-25',
        '2020-03-26',
        '2020-03-27',
        '2020-03-30',
        '2020-03-31'
    ],
    'Close': [
        310.0,
        340.5,
        330.0,
        315.0,
        305.0,
        258.0,
        264.0,
        245.0,
        197.0,
        211.0,
        240.5,
        264.0,
        270.0,
        279.5,
        280.5,
        285.0,
        309.0,
        304.0,
        300.0,
        296.0,
        300.0,
        306.5
    ],
}
'''

import csv
import os.path

file_name = 'playway.csv'
file_path = os.path.join(os.path.dirname(__file__), file_name)

with open(file_path, 'r') as file:
    content = file.read().splitlines()
    date = [line.split(',')[0] for line in content]
    close = [line.split(',')[4] for line in content]
    date_key = date[0]
    date_values = date[1:]
    close_key = close[0]
    close_values = [float(value) for value in close[1:]]
    result = {date_key: date_values, close_key: close_values}
print(result)

with open(file_path, 'r') as csvfile:
    date = []
    close = []
    result = {}
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    for row in csv_reader:
        date.append(row['Date'])
        close.append(float(row['Close']))
    result['Date'] = date
    result['Close'] = close
print(result)
