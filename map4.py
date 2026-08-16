'''
question 5 of map(): Combining map() and filter() Hand-in-Hand!

Now let's bring it all together for the final challenge!

Suppose we have a list of test scores out of 100:
scores = [45, 80, 62, 30, 95]

We want to perform two steps:

    Filter: Keep only passing scores (score >= 50).

    Map: Add a 5-point bonus to each passing score (score + 5).

Your Task:
Write a combined statement (or step-by-step) that filters scores first, 
then maps the bonus over the filtered result.

Print the final list to see the upgraded passing scores!

What is your code?
Where would you like to take this next?

'''
scores = [45, 80, 62, 30, 95]

step_step = filter(lambda step: step >= 50, scores)

date_name = list(map(lambda step: step + 5, step_step ))
print(date_name)




