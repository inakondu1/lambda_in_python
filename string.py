'''Step 3: Performing Operations on Strings

lambda functions aren't just for math—you can use them on text (strings) as well!

For example, if you want a lambda that converts a word to uppercase:
Python

# Regular function:
def make_upper(word):
    return word.upper()

# Lambda shortcut:
make_upper = lambda word : word.upper()

print(make_upper("hello"))  # Prints: HELLO

Notice how it follows the exact same pattern:

    word is the input parameter.

    word.upper() is the operation after the colon :.

Practice Question 3

Write a lambda function named greet that takes one input (a person's name) and returns
 a friendly greeting string combining "Hello, " with their name.

Hint: You can join strings together using the + operator, like "Hello, " + name.

Call your function with your name (or any name you like), wrap it in print(), and run it.

What is your code'''

greet = lambda name : "hello " + name

print(greet("Ina"))