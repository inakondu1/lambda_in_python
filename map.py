'''
filter() acts as a sieve or gateway—it decides which items get to stay based on 
a True/False condition.map() acts as a transformer—it takes every item that made
 it through and changes or converts it.
 How They Work Side-By-SideFeaturefilter()map()PurposeSelects / keeps
   specific itemsTransforms / modifies every itemOutput sizeUsually smaller
than the original listSame size as the original listLambda expectationMust 
 return True or FalseReturns the new modified valueUsing Them Hand-in-Hand 
 (Chaining)Because both take a list and output an iterable, you can nest them
 together!For example, imagine you want to take a list of numbers,
 keep only the even ones, and then double those even
numbers:Pythonnumbers = [1, 2, 3, 4, 5, 6]

# Step 1: filter() keeps only even numbers -> [2, 4, 6]
evens = filter(lambda x: x % 2 == 0, numbers)

# Step 2: map() doubles those filtered numbers -> [4, 8, 12]
doubled_evens = list(map(lambda x: x * 2, evens))

print(doubled_evens)  # Outputs: [4, 8, 12]

Or written in a single line:Pythonresult = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 8, 12]
Now that you see how they connect,
 let's practice map() on its own first so you get the hang of transforming
items!Question 1 of map()Given this list of numbers:
numbers = [1, 2, 3, 4, 5]Write a map() expression using a lambda function to double
every number (x * 2).Wrap the result in list(), save it to a variable,
and print() it.What is your code?

'''
number = list(map(lambda x: x * 2 , [1, 2, 3, 4, 5] ))
print(number)


'''
Spot on! You nailed it on the first try! That outputs [2, 4, 6, 8, 10].
What You Mastered

    You successfully used map() with a lambda to transform every item in a list.

    You wrapped the result in list() to display the transformed output.
'''
