'''
Question 4 of filter(): Filtering Dictionaries / Key-Value Pairs

filter() isn't limited to basic numbers or plain strings—you can also filter through complex structures like a list of dictionaries!

For example, suppose you have a list of user profiles:
Python

users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True}
]

To filter for only active users, your lambda inspects the key inside each dictionary element (x["active"] == True):
Python

active_users = list(filter(lambda x: x["active"] == True, users))

Your Task:
Given this list of products with their prices:
Python

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200},
    {"name": "Keyboard", "price": 50}
]

Write a filter() expression using a lambda function to keep only products that
 cost less than 100 (x["price"] < 100).

Save the result to a variable, print it as a list, and see which items match!

What is your code?
'''

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200},
    {"name": "Keyboard", "price": 50}
]

result = list(filter(lambda x : x["price"] < (100), products) )

print(result)

'''
What You Need to Know

    When items in a list are dictionaries, access specific values using x["key_name"].

    Lists use square brackets [...].
'''