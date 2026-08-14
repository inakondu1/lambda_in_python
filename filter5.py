

'''
Question 5 of filter(): Final Challenge!

Let's do one last filter() challenge before moving to map()!

Given this list of numbers:
data = [-5, 10, -3, 0, 8, -1, 12]

Write a filter() expression using a lambda to keep only positive numbers 
(numbers greater than 0: x > 0).

Convert it to a list, save it to a variable, and print() the result.

What is your code?

'''
data = list(filter(lambda x: x > 0, [-5, 10, -3, 0, 8, -1, 12] ))

print(data)