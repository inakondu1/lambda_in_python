'''
Question

Implement report_for_duty(name).

The function takes a recruit's name and returns:

Recruit [name] reporting for duty.

Do not print the result. Return it.


'''


def report_to_duty(name):
    if not isinstance(name, str):
        return "Only string is allowed"

    name = name.strip()
    if not name:
        return "Name cannot be empty"
    
    return f"Recruit {name} reporting for duty"
print(report_to_duty("ina "))
print(report_to_duty(35))