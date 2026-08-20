'''
Challenge 4: The Title Formatter

Write a function clean_headline(headline) that takes a messy blog post title like 
"   welcome TO python programming   " and does three things:

    Removes any leading or trailing spaces.

    Capitalizes the first letter of each word (Title Case).

    Wraps the title in double quotation marks in the output.

    Hint: Python strings have a built-in method called 
    .title() that converts text to Title Case.

    Example Test: clean_headline("   welcome TO python programming   ")

    Expected Output: "\"Welcome To Python Programming\"" or
      "Welcome To Python Programming" inside quotes.
'''
def clean_headline(headline):
    data = headline.title()
    name = data.strip()
    return f"{name}"
print(clean_headline("   welcome TO python programming   "))
