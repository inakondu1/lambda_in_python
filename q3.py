'''
Question 3 of 5: Finding the Larger Number

Write a lambda function that takes two numbers (a and b).

Use a one-line if/else inside the lambda to return whichever number is larger:

    If a > b, return a.

    Otherwise, return b.

Assign it to a variable named get_max, call it with 15 and 25, and print() the result.

What is your code?

'''

get_max = lambda a, b : a if a > b else b
print(get_max(15, 25))