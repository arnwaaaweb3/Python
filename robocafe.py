#Variable is a word that contains a value or data.
#Input is a function that takes user input from the console.

#Introduction of the AI assistant
print("Hello, my name is Robocafe!\n" 
      + "Your personal cafe AI assistant.\n")


#Ask for the name of the user
name = input("What is your name? ")
#input() is a function that takes user input from the console.
#name here is a variable that stores the user's name.
#a word without quotes is a variable, which is contain value and data.
#a word with quotes is a string, which is a value that represents text.

if name == "Robocafe, robocafe, AI, robocafe AI, Robocafe AI":
    print("Hey! That's my name! You can't use my name!\n")
    input("Again, what is your name? ")

#Greet the user nicely
print(f"Hello {name}!, welcome to Le Cafe Julien.\n\n"
      +"Thank you for coming in today.\n")
#(f"aaaa") is an f-string, which allows you to mix variables and strings together.
#{name} is a variable that being input by the user
#in the f-string here, I used two newlines (\n\n), one for a new line after the greeting, and another one to create a space before the next sentence.

#Define the menu as a variable
menu = ("- Americano-style\n"
        + "- Latte\n"
        + "- Cappuccino\n"
        + "- Espresso\n"
        + "- Macchiato\n"
        + "- Matcha\n"
        + "- Hot Chocolate\n"
        + "- Tea\n"
        + "- Milktea\n"
        + "- Flat-White\n"
        + "- Cafe au Lait\n"
        + "- Cold Brew\n"
        + "- Affogato\n"
        + "- Frappucino\n"
        + "- Ristretto\n"
        + "- Cortado\n"
        + "- Irish Coffee\n"
        + "- Doppio\n"
        + "- Breve\n"
        + "- Piccolo Latte\n"
        + "- Red Eye\n"
        + "- White Coffee\n"
        + "- Nitro Cold Brew\n"
        + "- Vietnamese Coffee\n"
        + "- Lungo\n"
        + "- Mocha\n")
#\n is a newline character, which should be located at the end of each line but before the quotation mark.
#\n can be multiplied like this: \n\n\n, which will create three new lines below.

#Robocafe will ask the user what they would like to order, based on the menu definition
print(f"Here is our menu:\n" + menu)
print(name + ", what would you like to order today? ")
order = input()
print()
#here, name and menu are already defined variables, so we can use them directly.
#order is a variable that stores the user's order.
#If there's no string in the input, just simply leave it empty, like this: input().
#If you want to add a prompt, you can do it like this: input("What would you like to order? ").

price = 8 #integer
quantity = input("How many " + order + " would you like to order, " + name + "? \n") #string
print()
#quantity here is a variable that contains string and order variable.
#i add the order variable inside, to automatically add the user's order to the string.

#Robocafe notes the order and asks the user to wait
total = price * int(quantity) #because quantity is a string, we need to convert it to an integer using int().
print("Perfect " + name + "!, your " + quantity + " " + order + " will be ready in a moment.")
print(f"That will be $" + str(total) + " in total.\n") #this (total) is still an integer, so we need to convert it to a string using str().
#print here is a function that prints output to the console. () is what inside the print function itself.
#"Perfect " is a string, a text. Do notice that i put a space after the word Perfect, so that the output will be more readable.
#"!, your " is also a string, a text. I also put a space after the word your, so that the output have some space between your and order (variable).
#order is what the user inputted.
#" will be ready in a moment." is a string, a text. I also put a space after the word will, so that there's a space between order (variable) and will.
#str() is a function that converts an integer to a string, so that it can be printed as text.
#int() is a function that converts a string to an integer, so that it can be used in calculations.
