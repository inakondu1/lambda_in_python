'''Step 2: Multiple Arguments (Inputs)

Now that you've got single inputs down, let's look at how to give a lambda more than one input.

In a regular function, you separate inputs with a comma inside parentheses:
Python
'''
def add_numbers(a, b):
    return a + b

'''With lambda, you do the exact same thing, just without parentheses before the colon:
'''
add_numbers = lambda a, b : a + b

'''practice Question 2

Write a lambda function named subtract that takes two inputs (x and y) 
and returns x - y.

Call it with 10 and 4, and use print() so you can see the result!
'''
subtract = lambda x, y : x - y

print(subtract(10, 4))