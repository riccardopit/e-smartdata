'''
We roll the symmetrical dice three times. Calculate the probability of the following:
- odd number of points in each roll
Use set comprehension. Round the result to three decimal places and print to the console as shown below.
Expected result:
Probability: 0.125
'''

omega = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
selection = {(x, y, z) for x, y, z in omega if x % 2 and y % 2 and z % 2 == 0}
prob = round(len(selection) / len(omega), 3)
print(f'Probability: {prob}')
