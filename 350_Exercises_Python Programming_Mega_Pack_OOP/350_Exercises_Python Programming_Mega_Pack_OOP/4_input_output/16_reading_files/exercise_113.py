'''
The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:
with open('playway.csv', 'r') as file:
    content = file.read().splitlines()
Find the highest volume for a given month and print the result to the console as shown below.
Expected result:
Max Vol: 100412
'''

import os.path

file_name = 'playway.csv'
file_path = os.path.join(os.path.dirname(__file__), file_name)
with open(file_path, 'r') as file:
    content = file.read().splitlines()
    volumes = [line.split(',')[-1] for line in content[1:]]
    volumes = [int(volume) for volume in volumes]
    max_volume = max(volumes)
print(f"Max Vol: {max_volume}")
