'''
The following text is given:
text = 'python is a popular programming language.'
Use the appropriate method to replace the first letter of the text with uppercase. Print the result to the console.
Expected result:
Python is a popular programming language.
'''

text = "python is a popular programming language."
text = text.replace('p', 'P', 1)
print(text)
print(text.capitalize())
