'''
Question 2 of 5: Combining Strings with Multiple Arguments

Write a lambda function that takes two inputs: first_name and last_name.

It should return a single full name string formatted as "First Last" (with a space in between).

Assign it to a variable named full_name, call it with your first name and last name, and print() the result.

What is your code?
'''
full_name = lambda  first_name, last_name : first_name  + " " + last_name
print(full_name("Joy",  "Isah"))