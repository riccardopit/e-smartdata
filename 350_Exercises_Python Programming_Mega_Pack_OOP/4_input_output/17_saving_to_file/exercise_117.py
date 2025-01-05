'''
Two following lists are given:
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]
Save the above data to the users.csv file (file in csv format - comma-separated values) as shown below.
File users.csv after saving:
user_id,amount
001,1400
004,1300
007,900
'''

import csv
import os.path

file_name = 'users.csv'
file_path = os.path.join(os.path.dirname(__file__), file_name)
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open(file_path, 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(headers)
    write.writerows(users)

with open(file_path, 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')
