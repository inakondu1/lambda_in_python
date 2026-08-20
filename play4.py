'''
Challenge 5: The File Extension Generator

Write a function generate_filename(project_name, extension)
 that takes a project name and an extension type, cleans them up, 
 and outputs a valid filename.

    Remove any leading or trailing spaces from project_name.

    Replace spaces inside project_name with underscores _.

    Convert the whole filename to lowercase.

    Attach the extension with a dot ..

    Hint: Python strings have a built-in .replace(" ", "_") method!

    Example Test: generate_filename("  My Cool Project  ", "py")

    Expected Output: "my_cool_project.py"

'''
def generate_filename(project_name, extention):
    date = project_name.strip()  + "."  + extention.strip()
    joy = date.replace(" ", "_").lower()
    return joy
print(generate_filename("  My COOL Project  ", "py"))

