''' 
Question 3 of map(): Converting Data Types

map() is super handy for converting data types across an entire list.

A common task in real-world Python programming (like reading input from a file or user form) is converting a list of string numbers into actual integers:
Python

# Convert text "10" into number 10 using int()
lambda x: int(x)

Your Task:
Given this list of numbers stored as strings:
str_numbers = ["10", "20", "30", "40"]

Write a map() expression using a lambda function to convert each
 string into an integer using int(x).

Save the result to a variable, print it as a list, and test your code in VS Code!

What is your code?
'''
num = ("10", "20", "30", "40")
number = map(lambda x: int(x), num)
print(list(number))

#str_numbers = ["10", "20", "30", "40"]

#result = map(lambda x: int(x), str_numbers)

#print(list(result))
