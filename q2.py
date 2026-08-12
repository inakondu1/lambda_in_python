'''
Question 2 of 5: Combining Strings with Multiple Arguments

Write a lambda function that takes two inputs: first_name and last_name.

It should return a single full name string formatted as "First Last" (with a space in between).

Assign it to a variable named full_name, call it with your first name and last name, and print() the result.

What is your code?
'''


full_name = lambda  first_name, last_name : first_name  + " " + last_name
print(full_name("Joy",  "Isah"))



'''

In Python, the plus sign + when used with text (strings) acts as a joiner (or concatenation operator).

The part + " " + does two specific jobs:

    " " (a string containing a single space): This inserts a blank space between the two names.

    + (the plus signs): These glue the three pieces together into one single string.

What happens with vs. without + " " +

If you wrote:
Python

first_name + last_name

With first_name = "Ina" and last_name = "Isah", Python would smash them directly together:
👉 "InaIsah" (No space in between!)

By adding + " " +:
Python

first_name + " " + last_name

Python connects three distinct pieces:

    first_name ("Ina")

    + (glue)

    " " (a space)

    + (glue)

    last_name ("Isah")

👉 "Ina Isah" (Properly formatted with a space!)

'''