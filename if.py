# IF & ELSE

#if is a keyword that checks if a condition is true or false (or we call it a boolean value).
#else is a keyword that is used when the if condition is false.
#so "if" condition is true, it will execute the code inside the if block.
#If the condition is false, it will execute the code inside the else 
#= is an operator to assign a value to a variable.
#== is an operator to compare two values, and it returns True if they are equal, or False if they are not.

# Defining variable for Andrew here:
name = "Andrew" #his name is Andrew
age = 34 #his age is 34
occupation = "Salesman" #his occupation is Salesman
workplace = "Adira Assurance" #he works at Adira Assurance
skills = ["Sales, Marketing, Customer Service, Communication"] #using [] (list) to define a list of his skills.
#use [] to define a list, which is a collection of items that can be of any data type.

#Defining variable for eligibly work at Adira Assurance here:
minimum_age = 19 #let's say the minimum age for the job is 19, so if the age is less than 19, they're not eligible to work here.
maximum_age = 50 #let's say the maximum age for the job is 45, so if the age is more than 45, they're too old to work here.
skills_required = ["Sales, Marketing, Customer Service, Communication"] #using [] (list) to define a list of required skills for the job.
#skills must have the exact same value as skills_required to be eligible for the job. 

# If and else statement example
if age < maximum_age: #let's say the age limit for the job is 45, if the age is less than 45, then this message will be printed.
    print(f"{name} is still eligible to work at {workplace} as a {occupation}.")
    #f-string here because we want to mix variables and strings together.
    if skills == skills_required:
        print(f"{name} has the required skills to work at {workplace} as a {occupation}.")
    else:
        print(f"{name} does not have the required skills to work at {workplace} as a {occupation}.")
else: #so if the age is not less than 45, then this message will be printed.
    print(f"{name} is not eligible to work at {workplace} as a {occupation} anymore.")