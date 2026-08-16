'''
Question 4 of map(): Extracting Values from Dictionaries

map() is also great for extracting specific pieces of information from a list of dictionaries!

For example, if you have a list of user profiles and want to extract just their names:
Python

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# Extracting only the name from each dictionary:
names = list(map(lambda person: person["name"], users))
print(names)  # Outputs: ['Alice', 'Bob']

Your Task:
Given this list of products:
Python

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200}
]

Write a map() expression using a lambda function to extract just the price of each product
 (product["price"]).

Convert the result to a list, save it to a variable, and print() it.

What is your code?
'''
