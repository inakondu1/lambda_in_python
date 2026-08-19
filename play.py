'''Challenge 1: The Email Generator

Write a function create_email(first_name, last_name, domain) that takes three strings and returns a lowercased email address formatted as first_name.last_name@domain.

    Hint: Use .lower() on the result or variables.

    Example Test: create_email("Ina", "Isah", "gmail.com")

    Expected Output: "ina.isah@gmail.com"
    '''
def create_email(first_name, last_name, domain):
    data = first_name.lower()
    date = last_name.lower()
    return  f"{data}.{date}{domain}"


print(create_email("Ina", "Isah", "@gmail.com"))
