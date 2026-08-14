'''
Question 3 of filter(): Filtering Even Numbers

In Python, the modulo operator % calculates the remainder of a division.

    To check if a number is even, we check if number % 2 == 0 
    (remainder is 0 when divided by 2).

    To check if a number is odd, we check if number % 2 != 0.

Your Task:
Given this list of numbers:
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Write a filter() expression using a lambda function to keep only the even numbers.

Save the result to a variable, print it as a list, and test your code in VS Code!

What is your code?

'''

number = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ))
print(number)
'''

Spot on! Your code runs cleanly and outputs [2, 4, 6, 8, 10].
What You Have Mastered

    You know how to use modulo % 2 == 0 inside a lambda to test for divisibility.

    You can filter numerical datasets based on arithmetic conditions.

    What You Have Mastered

    You know how to use modulo % 2 == 0 inside a lambda to test for divisibility.

    You can filter numerical datasets based on arithmetic conditions.
'''