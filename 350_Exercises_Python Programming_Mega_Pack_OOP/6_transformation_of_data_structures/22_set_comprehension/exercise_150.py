'''
Consider the two-roll of the dice. Create the probability space (omega)
and count the probability of getting a sum of points higher than 10. Use set comprehension.
Expected result:
Probability: 0.08
'''

omega = {(x, y) for x in range(1, 7) for y in range(1, 7)}
selection = {(x, y) for x, y in omega if x + y > 10}
prob = round(len(selection) / len(omega), 2)
print(f'Probability: {prob}')
