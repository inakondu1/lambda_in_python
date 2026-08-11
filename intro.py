'''Step 1: def vs. lambda

In Python, you normally create a function using def:
Python
'''
def add_five(x):
    return x + 5

'''A lambda is just a shortcut to write a simple function on one line without using def or return.

The return is automatic! Whatever math or operation you write after the colon : is automatically sent back.

Here is the exact same function written as a lambda:
'''
add_five = lambda x: x + 5
''' in this code, nothing will be printed because we dnt add the print to the code 


Here is our clear, step-by-step roadmap for lambda:

    Step 1: What is a lambda and how does it compare to a regular function?

    Step 2: Single argument (parameter) functions.

    Step 3: Multiple arguments (parameters).

    Step 4: Using logic (if / else) inside a lambda.

    Step 5: String operations with lambda.
    '''