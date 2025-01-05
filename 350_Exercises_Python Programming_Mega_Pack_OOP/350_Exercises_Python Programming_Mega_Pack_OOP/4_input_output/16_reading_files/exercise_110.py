'''
Write a program that reads playway.txt file containing Playway stock data,
and then calculates the average closing price (3-day average).
Print the result to the console as shown below.
Expected result:
3-day average closing price: 313.67
'''

import csv
import os.path

file_name = 'playway.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
with open(file_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    close_sum = 0
    for count, row in enumerate(csv_reader, start=1):
        close_sum += int(row['Close'])
    close_avg = close_sum / count
print(f"3-day average closing price: {close_avg:.2f}")
