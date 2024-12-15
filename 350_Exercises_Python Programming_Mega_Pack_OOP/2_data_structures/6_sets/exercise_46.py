'''
The following text is given:
text = 'Programming in python.'
Follow the next steps:
1. Change all letters to lowercase.
2. Delete spaces and period.
3. Create a set consisting of all letters in the text and assign to letters variable
4. Using the appropriate method for sets, remove all vowels from letters set:
    vowels = {'a', 'e', 'i', 'o', 'u'}
5. Print the number of items in the letters set as shown below.
Expected result:
Number of items: 8
'''

text = "Programming in python."
vowels = {'a', 'e', 'i', 'o', 'u'}
text = text.lower()
text = text.replace(' ', '').replace('.', '')
text = set(text)
text1 = text - vowels
text2 = text.difference(vowels)
print(f"Number of items: {len(text1)}")
