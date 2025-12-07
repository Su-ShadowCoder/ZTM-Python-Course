
# Chat gpt-exercises 


# ////////////// 1. User Input & Conditional Logic \\\\\\\\\\\\\\\\\\\

# Exercises:

# /////////////////////
# 1. Ask the user for their favorite color and print a message like: “Wow, I like [color] too!”

# usr_fav_clr = input(f"What is your favorate color? \n--> ")

# print(f"Wow, I like {usr_fav_clr} too!")
# /////////////////////

# /////////////////////
# 2. Write a program to ask for a number. If it’s even, print “Even! otherwise  print “Odd!”.

# usr_inp = int(input(f"Please enter a number to check if it's even or odd:\n10--> "))

# if usr_inp % 2 == 0:
#     print("Even!")
# else:
#     print("Odd!")
# /////////////////////

# /////////////////////
# 3. Create a login simulation:
# - Ask for username and password.
# - Set a predefined password (like 1234).
# - Print “Access Granted” or “Access Denied” based on user input.

# # Authntication Anouncement:
# input(f"Welcome to our secret service Agency ICE-C!\nPlease enter something to proceed with authentication:\n--> ")

# # Username 
# print(f"|||Authentication starting|||")
# usr_name = input(f"Please enter you username here:\n--> ")
# usr_pswrd = input(f"Please enter you user password here:\n--> ")
# # password authentication
# if usr_pswrd == "1234":
#     print(f"Authenication succesfull!\nAccess Granted\n-->Welcome back Special Agent CSOC Analyst {usr_name}. ")
# else:
#     print(f"Access Denied!\nPlease stay where you are {usr_name}, we will be 'checking' up with you")
#     print(f"'BEEP'-'BEEP'-'BEEP'\nCODE SKY! I REPEAT. CODE SKY!\n'BEEP'-'BEEP'-'BEEP' ")
# /////////////////////

# /////////////////////
# 4. Ask the user a yes/no question (like your “under the water” example) and respond differently for “yes” and “no” inputs.
# usr_answr_1 = input("Have you ever visited outer space?\n")
# if usr_answr_1 == "yes":
#     print(f"Wowwww, really? \nThat's so cool!")
# else:
#     print(f"Me neither, so that makes it the both of us.\n:)")
# /////////////////////

# /////////////////////
# Challenge question:
# How would you make the password check case-insensitive if it were a string?
# by a conditional if password statement. but it does it automaticly because python is case sensitive, so you can always say that the password is incorect, and to watch out if your password is case sensitive, you would also make a for loop and go trough every letter to check if it is upper case or not, and based on the password you could correspond if they are the same letter but not in the correct state. then you tell the user too by else. 
# /////////////////////




























# ////////////// 2. Data Types & Math Operators \\\\\\\\\\\\\\\\\\\

# Exercises:

# Print the type of the following operations:

# 7 + 2

# 7 / 2

# 7 // 2

# 7 ** 2

# 7 % 2

# Use round(), abs(), and other math functions to perform operations.

# Create expressions combining multiple operators and predict the output using operator precedence before running the code:

# (2 + 3) * 4 / 2

# 5 + 6 * 2 ** 2 // 3

# Challenge question:

# Why does 5 + 4 * 10 // 2 give an integer, but 5 + 4 * 10 / 2 gives a float?







# 3. Variables & Expressions

# Exercises:

# Assign values to variables using multiple assignment:

# a, b, c = 10, 20, 30


# Create an expression using variables and assign it to another variable:

# x = 10
# y = 5
# z = x * 2 + y


# Experiment with constants (like PI = 3.14) and try reassigning them. Observe behavior.

# Challenge question:

# What’s the difference between an expression and a statement? Give an example of each.







# 4. Augmented Assignment

# Exercises:

# Use +=, -=, *=, and /= on a variable. Example:

# value = 10
# value += 5  # What is value now?
# value *= 2


# Rewrite normal assignment expressions using augmented assignment operators.

# Challenge question:

# Can you use augmented assignment with strings? Try "Hello " += "World" and see what happens.








# 5. Strings & String Manipulation

# Exercises:

# Concatenate first and last name to create a full name.

# Use slicing to extract specific parts of a string:

# text = "I love Python programming"


# Extract "Python"

# Extract "I love"

# Experiment with immutability:

# Try changing a character in a string (text[0] = "J") and see what happens.

# Challenge question:

# How can you “modify” a string if it’s immutable?







# 6. Type Conversion

# Exercises:

# Convert integers to strings and vice versa.

# Combine a number and string using conversion:

# age = 25
# print("I am " + str(age) + " years old")


# Chain conversions like int(str(float(10))) and predict the final type.

# Challenge question:

# Why do you sometimes need to convert types before concatenating?






# 7. Escape Sequences

# Exercises:

# Print a sentence with quotes inside: "It’s “awesome”!"

# Use \n to print multiple lines and \t for tab spacing.

# Combine both in a formatted message.

# Challenge question:

# What’s the difference between using single quotes and double quotes for strings in Python?






# 8. Formatted Strings

# Exercises:

# Use f-strings to print a message with variables:

# name = "Ali"
# age = 30


# Use .format() to achieve the same output.

# Practice numbered placeholders and named placeholders in .format().

# Challenge question:

# Which method is better for readability: f-string or .format()? Why?






# 9. Bonus: Binary & Complex Numbers

# Exercises:

# Convert an integer to binary using bin() and back using int().

# Create a complex number and print its real and imaginary parts:

# z = 2 + 3j


# Challenge question:

# What happens when you try to add an integer and a complex number?









# //////////////  \\\\\\\\\\\\\\\\\\\
# //////////////  \\\\\\\\\\\\\\\\\\\
# //////////////  \\\\\\\\\\\\\\\\\\\
# //////////////  \\\\\\\\\\\\\\\\\\\
# //////////////  \\\\\\\\\\\\\\\\\\\
# //////////////  \\\\\\\\\\\\\\\\\\\