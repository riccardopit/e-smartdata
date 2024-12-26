'''
Write a program that returns a list of values above the given threshold = 0.5 from the following list:
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
Expected result:
[0.91, 0.55, 0.76]
'''

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
threshold = 0.5
result = []
for probabilitie in probabilities:
    if probabilitie > threshold:
        result.append(probabilitie)
print(result)
