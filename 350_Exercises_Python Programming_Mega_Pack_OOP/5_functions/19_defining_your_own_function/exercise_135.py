'''
The following function is defined:
def function(idx, vals=[]):
    for i in range(idx):
        vals.append(i ** 3)
    print(vals)
Call the function three times as follows:
function(3)
function(5, ['a', 'b', 'c'])
function(6)
Analyze the results!
Expected result:
[0, 1, 8]
['a', 'b', 'c', 0, 1, 8, 27, 64]
[0, 1, 8, 0, 1, 8, 27, 64, 125]
'''


def function(idx, vals=[]):
    for i in range(idx):
        vals.append(i ** 3)
    print(vals)


function(3)
function(5, ['a', 'b', 'c'])
function(6)
