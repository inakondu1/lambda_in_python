'''
Challenge 3: Product Label Fixer

Write a function format_product(product_code, price) that takes a code string like 
"   pYtHoN_bOoK   " and a price like 25, cleans up the extra whitespace,
 makes the code ALL CAPS, and formats the price with a dollar sign.

    Hint: Use .strip() to remove excess spaces and .upper() for uppercase.

    Example Test: format_product("   pYtHoN_bOoK   ", 25)

    Expected Output: "PYTHON_BOOK - $25"
    '''
def format_product(product_code, price): 
    name = product_code.upper()
    data = name.strip()
    return f" {data} - ${price}"
print(format_product("    python_book     " , "25"))