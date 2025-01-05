'''
Generate all even numbers from 2 to 18 inclusive. Then write each number on a separate line to the file called num.txt.
File num.txt after saving:
2
4
6
8
10
12
14
16
18

'''

import os.path

file_name = 'num.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)

even_nums = [str(num) for num in range(2, 19) if num % 2 == 0]
with open(file_path, 'w') as file:
    for num in even_nums:
        file.write(num + '\n')

even_nums = [str(num) + '\n' for num in range(2, 19) if num % 2 == 0]
with open(file_path, 'w') as file:
    file.writelines(even_nums)
