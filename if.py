# IF & ELSE

#if is a keyword that checks if a condition is true or false (or we call it a boolean value).
#else is a keyword that is used when the if condition is false.
#so "if" condition is true, it will execute the code inside the if block.
#If the condition is false, it will execute the code inside the else 
#= is an operator to assign a value to a variable.
#== is an operator to compare two values, and it returns True if they are equal, or False if they are not.

# Defining variable here
name = "Andrew"
age = 34
occupation = "Salesman"
workplace = "Adira Assurance"

# If and else statement example
if age < 45: #let's say the age limit for the job is 45, if the age is less than 45, then this message will be printed.
    print(f"{name} is still eligible to work at {workplace} as a {occupation}.")
    #f-string here because we want to mix variables and strings together.

else: #so if the age is not less than 45, then this message will be printed.
    print(f"{name} is not eligible to work at {workplace} as a {occupation} anymore.")