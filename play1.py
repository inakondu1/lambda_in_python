'''Challenge 2: The Username Creator

Write a function create_username(first_name, birth_year) that takes a string and a number,
 and returns a username combining the first 3 letters of the name (in lowercase)
   with the birth year.

    Hint: Use slicing first_name[:3] to get the first 3 letters, and remember to convert
      birth_year if using + (or just use an f-string!).

    Example Test: create_username("Hadiza", 1997)

    Expected Output: "had1997"
    '''

def create_username(first_name, birth_year):
    name = first_name[:3].lower()
    return f"{name}{birth_year}"
print(create_username("Hadiza", "1997"))
