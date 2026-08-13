'''
Question 5 of 5: Final lambda Challenge!

Write a lambda function named get_first_item that takes one input (a list called items).

Return the first element of that list using indexing (items[0]).

Call your function with the list ["apple", "banana", "cherry"] 
(remember to wrap the items in square brackets [...] when passing them!) and print() the result.

What is your code?
'''
get_first_item = lambda list: list[0]
print(get_first_item(["apple", "banana", "cherry"]))