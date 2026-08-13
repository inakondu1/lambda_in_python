

'''
filter() is a built-in Python function that takes a collection of items (like a list) 
and keeps only the items that satisfy a specific condition.

It takes two arguments:
Python

filter(function, list)

    function: A function (usually a lambda) that returns either True or False for each item.

    list: The collection of items you want to filter through.

How filter() works step-by-step

Let's say we have a list of numbers: [1, 2, 3, 4, 5, 6] and we want to keep only 
the numbers greater than 3.

Step A: Write a lambda that returns True or False
Python

lambda x: x > 3

    If x = 1, 1 > 3 is False ❌ (Dropped)

    If x = 4, 4 > 3 is True ✅ (Kept)

Step B: Pass it into filter()
Python

filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6])

Step C: Convert to a list()
In Python, filter() creates a "filter object" (a stream of data). To view it as a regular list, we wrap the whole thing inside list():
Python

result = list(filter(lambda x: x > 3, [1, 2, 3, 4, 5, 6]))
print(result)  # Outputs: [4, 5, 6]

Question 1 of filter()
'''

#Given this list of numbers:
#numbers = [10, 15, 20, 25, 30]

#Write a filter() expression using a lambda function to keep only numbers greater than 18.

#Convert the result to a list, save it to a variable named filtered_numbers, and print() it.

result = list(filter(lambda number: number > 18, [10, 15, 20, 25, 30]
 ))
print(result)