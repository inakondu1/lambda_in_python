'''
Question 4 of 5: Working with Lists

A lambda can also take a list as its input parameter!

Python has a built-in function sum() that adds up all numbers in a list
 (for example, sum([1, 2, 3]) gives 6).

Your Task:
Write a lambda function named total_sum that takes one input parameter
 (a list of numbers called num_list).

Inside the lambda, use sum(num_list) to calculate and return the total.

Test it by passing the list [10, 20, 30] into total_sum, and print() the result!

What is your code?

'''
#total_sum = lambda sum1, sum2, sum3: sum1 + sum2 + sum3
#print(total_sum(10, 20, 30))

total_sum = lambda num_list: sum(num_list)
print(total_sum(10, 20, 30))
