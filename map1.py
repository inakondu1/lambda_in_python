'''
Question 2 of map(): Working with Strings

Just like filter(), map() works seamlessly on strings! You can use string methods inside the lambda to transform text.

For example, to convert every word in a list to uppercase:
Python

lambda word: word.upper()

Your Task:
Given this list of lowercase names:
names = ["ina", "alice", "bob"]

Write a map() expression using a lambda function to capitalize the first letter of each name using the .capitalize() method (or .upper() if you prefer all caps!).

Save the result to a variable, print it as a list, and see how it transforms the text!

What is your code?

'''

names = ["ina", "alice", "bob"]

name = list(map(lambda name: name[:-1] + name[-1:].upper(), names))
print(name)
#capitalized_last = list(map(lambda name: name[:-1] + name[-1:].upper(), names))
#print(capitalized_last)
# Output: ['inA', 'alicE', 'boB']
