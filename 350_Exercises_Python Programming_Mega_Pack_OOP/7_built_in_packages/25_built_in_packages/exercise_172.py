'''
Using the datetime built-in module, calculate the difference for dates (date 2 - date 1):
date 1: 2020-06-01
date 2: 2020-07-18
Print the result to the console as shown below.
Expected result:
47 days, 0:00:00
'''

from datetime import datetime

date_1 = '2020-06-01'
date_2 = '2020-07-18'
print(datetime.strptime(date_2, "%Y-%m-%d") - datetime.strptime(date_1, "%Y-%m-%d"))
