
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

# print(type(    7 + 2  )) 

# print(type(    7 / 2  )) 

# print(type(   7 // 2   )) 

# print(type(   7 ** 2   )) 

# print(type(    7 % 2  )) 

# # Use round(), abs(), and other math functions to perform operations.

# print(    abs(7 + 2  )) 

# print(    round(7 / 2  )) 


# Create expressions combining multiple operators and predict the output using operator precedence before running the code:

# (2 + 3) * 4 / 2
# anticipate = 10.0

# 5 + 6 * 2 ** 2 // 3
# 13

# Challenge question:

# Why does 5 + 4 * 10 // 2 give an integer, but 5 + 4 * 10 / 2 gives a float?

# because int is whole number and float is a number with decimal, or value with decimal 




# Exercise 1: Variables, Expressions & Augmented Assignment

# Assign values to three variables in one line: a, b, c = 10, 20, 30.

# Create a new variable z that calculates a * 2 + b.

# Increment z by 5 using an augmented assignment operator.

# Multiply z by c using another augmented assignment operator.

# Challenge: Explain the difference between an expression and a statement in this context.

# ✅ This combines Variables, Expressions, and Augmented Assignment.

# a, b, c = 10, 20, 30

# z = a * 2 + b 

# z += 5
# print(z)

# z *= c
# print(z)

# An expression is that you do something with a variable, and a statement means to assign a variable. 




# Exercise 2: Strings & Type Conversion

# Create variables for first name and last name and concatenate them to make a full name.

# Take the sentence "I love Python programming" and:

# Extract "Python" using slicing

# Extract "I love" using slicing

# Experiment with immutability: try changing a character in the string. Observe what happens.

# Convert an integer age = 25 to a string and print "I am 25 years old" using both concatenation and f-strings.

# Chain conversions like int(str(float(10))) and predict the final type.

# Challenge: Why do you sometimes need type conversion before concatenating?

# name = "abdullah"
# last_name = "ibn isa"
# full_name = name + " " + last_name
# print(full_name)

# sentc = "I love Python programming"
# print(sentc[7:13])
# print(sentc[0:7])
# sentc[1:] = "y"
# print(sentc)

# age = 25
# str(age)
# print(f"I am {age} years old")

# ✅ This combines Strings, String Manipulation, Type Conversion, and Formatted Strings.





# Exercise 3: Escape Sequences, Binary & Complex Numbers

# Print a sentence with quotes inside, e.g., "It’s “awesome”!".

# Print multiple lines using \n and tab spacing using \t. Combine both in one formatted message.

# Convert an integer (e.g., 5) to binary using bin() and back to an integer.

# Create a complex number, e.g., z = 2 + 3j, and print its real and imaginary parts.

# Challenge: What happens when you try to add an integer and a complex number?

# print("\"It\"s \"awesome\"!\"")

# numb = 5

# bin_numb = bin(numb)

# real_bin = bin_numb[3:]

# real_i_bin = str(real_bin)

# temp = 0

# for element in real_i_bin:
#     if element != 0:
#         for index in len(real_i_bin):
#             decimal = index * 2


# print(numb)
# print(bin_numb)
# print(decimal)


