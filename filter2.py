

'''Question 2 of filter(): Filtering Strings

filter() works with strings too! You can use string methods inside your lambda condition.

For example, to keep words that start with the letter "a":
Python

lambda word: word.startswith("a")

Your Task:
Given this list of words:
words = ["cat", "elephant", "dog", "hippopotamus", "ant"]

Write a filter() expression using a lambda function to keep only words that have more
 than 4 letters (using len(word) > 4).

Save the result to a variable, print it as a list, and see which animals make the cut!

What is your code?

'''

word_list = list(filter(lambda word: len(word) > 4, ["cat", "elephant", "dog", "hippopotamus", "ant"]))

print(word_list)