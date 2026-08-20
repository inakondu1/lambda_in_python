'''Challenge 6: The Obfuscated ID Masker

Write a function mask_account_number(account_number) that takes a full 10-digit account
 number as a string and masks all but the last 4 digits with asterisks (*).

    Hint: Use string slicing [-4:] to grab the last 4 characters, and string multiplication
      "*" * 6 for the hidden part!

    Example Test: mask_account_number("0123456789")

    Expected Output: "******6789"

Take your time and give them a shot! Post your code here whenever you're ready.'''

def mask_number(account_number):
    dat = account_number[-4:] 
    account_number = '*' * 6
    name  = account_number + dat
    return name
print(mask_number("0123456789"))

