
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


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# Exercise 1: Built-In Functions, Methods, Booleans, and Immutability
# Objective: Practice len(), string methods, bool(), and understand immutability.

# Create a variable:
# # quote = "to be or not to be"


# Do the following:
# x Print the length of quote using a built-in function.
# x Print quote in:
# x all uppercase capitalized form
# Find the index of the first occurrence of "be".
# Replace "be" with "me" and:
# Print the result
# Print the original quote again
# Assign the replaced version to a new variable and print both variables.
# Create a boolean variable:
# is_long = len(quote) > 15
# Print:
# is_long
# bool(0)
# bool(len(quote))


# What this tests:
# Built-in functions vs methods
# String immutability
# Boolean evaluation
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# quote = "to be or not to be"

# # print(len(quote))

# # x = quote.upper()
# # print(x)

# # print(quote.find("be"))

# x = quote.replace("be", "me")
# print(x)
# print(quote)
# is_long = len(quote) > 15
# print(is_long)
# bool(0)
# bool(len(quote))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Short Exercise: Built-In Functions, Methods, Booleans

# Create a string variable containing a short sentence of your choice.

# Use one built-in function on the string and print the result.

# Use two different string methods on the same string and print their results.

# Create one boolean variable based on a comparison that involves the string.

# Print the boolean variable.


# sentence = "It is, what it is."

# u_sent = sentence.upper()
# print(u_sent)
# print(bool(u_sent))

# x = u_sent.find("WHAT")
# print(x)

# y = "apple"
# z = "moes"

# s = y == z

# print(s)

# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Exercise 1: Matrix Access

# Create a 3×3 matrix using a 2D list (numbers of your choice).

# Print the element in the second row, third column.

# Change the element in the first row, first column to a new value.

# Print the entire matrix.
# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# matrix = [
#     [9,8,7],
#     [7,6,5],
#     [3,2,1]
# ]

# print(matrix[1][2])

# matrix[0][0] = 10

# print(matrix)

# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Exercise 2: List Methods & Patterns
# Use this list for reference:
# fruits = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove the first and last item.

# Add "Kiwi" at the end.

# Insert "Mango" at the beginning.

# Count how many "Apples" are in the list.

# Reverse the list.

# Print a copy of the list sorted alphabetically without modifying the original list.
# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# fruits = ["Banana", "Apples", "Oranges", "Blueberries"]
# og = fruits.copy()

# fruits.pop(0)
# # or fruits.remove("Banana")
# print(fruits)

# fruits.append("kiwi")
# fruits.insert(1, "Mango")
# print(fruits.count("Apples"))
# print(fruits)

# fruits.reverse()
# print(fruits)

# print(og)
# og.sort()
# print(og)


# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Exercise 3: List Slicing & Unpacking

# Create a list of numbers from 1 to 10.

# Slice the list to get all even numbers.

# Use unpacking to assign the first two numbers to variables a and b, the last number to z, and the rest to a list rest.

# Print a, b, rest, and z.
# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# my_list = []
# for element in range(1, 11):
#     my_list.append(element)
# print(my_list)

# # or 
# # your_lst = list(range(1,11))
# # print(your_lst)
# og = my_list.copy()

# even = my_list[::-2]
# even.reverse()
# print(even)

# print(og)

# a, b, *list_rest, z = og

# print(a)
# print(b)
# print(z)
# print(list_rest)



# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Exercise 4: Dictionary Basics

# Create a dictionary representing a user with keys: "name", "age", and "basket" (a list of items).

# Access and print the "age".

# Add a new key "is_active" with a boolean value.

# Update --> very misleading btw, you should have told not to use update function but to update the list. the "basket" by adding one new item.

# Print all keys and all values separately.
# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# this_dict = {
#     'name':'Jan',
#     'age':24,
#     'basket':["powerranger", "supersoldier", "pipilangkous"]
# }

# print(this_dict.get('age'))

# this_dict["is_active"] = True

# this_dict['basket'].append("actionman")

# print(this_dict.items())

# # # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # Exercise 5: Dictionary & List Combination

# # Create a list of 2 dictionaries, each representing a user (name and age).

# # Access the age of the second user.

# # Add a new key "country" to the first user.

# # Print the entire list of dictionaries.
# # # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# lst_of_dicts = [{
#     'name':'sam',
#     'age': 19
# }, {
#     'name':'clover',
#     'age': 20 }]

# print(lst_of_dicts[1].get('age'))

# lst_of_dicts[0].update({'country': None})

# print(lst_of_dicts)

# # # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\





# ====================================================
# Exercise 1: Tuples & Sets
# ====================================================

# 1. Create a tuple with 6 numbers of your choice.

# 2. Check if the number 3 is in the tuple and print the result.

# 3. Use tuple unpacking to assign the first two numbers to 'a' and 'b', and the rest to 'rest'. Print them.

# 4. Use a tuple method to count how many times the first number appears in the tuple.

# 5. Create a set from the tuple.

# 6. Add a new number to the set and remove a number of your choice.

# 7. Create another set {4,5,6,7,8} and print:
#    - The union of the two sets
#    - The intersection of the two sets
#    - Whether your first set is a subset of the second set



# tpl = tuple(range(1, 7))
# print(tpl)

# if 3 in tpl:
#     print(True)

# (a, b, *rest) = tpl
# print(a)
# print(b)
# print(rest)

# x = tpl.count(a)
# print(x)

# y = set(tpl)
# print(y)

# lst_tpl = list(tpl)
# print(lst_tpl)
# lst_tpl.append(10)
# lst_tpl.remove(1)
# print(lst_tpl)

# st_st = set(range(4, 9))
# print(st_st)

# ult_st = st_st.union(y)
# print(ult_st)

# i = y.intersection(st_st)
# print(i)

# s = y.issubset(st_st)
# print(s)

# if i switch , then it also comes false 



# ====================================================
# Exercise 2: Conditional Logic & Ternary
# ====================================================

# # 1. Create two boolean variables: 'is_old' and 'has_license'.

# is_old = True
# has_licence = True

# # 2. Write an if/elif/else statement to print:
# #    - "You can drive" if is_old and has_license are True
# #    - "You need a license" if is_old is True but has_license is False
# #    - "You are too young" otherwise

# if is_old and has_licence:
#     print(f"You can drive")
# elif is_old == True and has_licence == False:
#     print(f"You need a license")
# else:
#     print(f"You are too young")


# 3. Create variables 'username' and 'password' with any values.
#    Use a conditional statement to print "Welcome back!" only if both are truthy.

# user_name = "beastcatcher69"
# pass_word = "croft"

# Authentication_usr = input(f"Please enter your username\n")
# Authentication_psswrd = input(f"Please enter your password\n")

# if Authentication_usr == user_name and Authentication_psswrd == pass_word:
#     print("Welcome back!")
# else:
#     print("Please try again...")


# 4. Create variables 'is_student' and 'has_ticket'.
#    Use a ternary operator to assign 'status_message':
#    - "Access granted" if both are True
#    - "Check requirements" if only one is True
#    - "Access denied" if both are False
#    Print 'status_message'.

# is_student = False
# has_ticket = False 

# if is_student and has_ticket: status_message = "Access granted"
# elif is_student or has_ticket: status_message ="Check requirements"
# else: status_message = "Access denied"

# print(status_message)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ====================================================
# Exercise 1: User Activity Analyzer
# ====================================================

# You are given a list of tuples.
# Each tuple represents a user in the form:
# (username, age, country, is_active)

# users = [
#     ("ali", 22, "NL", True),
#     ("sara", 17, "BE", False),
#     ("omar", 30, "NL", True),
#     ("fatima", 22, "DE", True),
#     ("ali", 22, "NL", True)
# ]

# Tasks:

# 1. Loop through the users and print only the usernames of active users.


# for element in users:
#     if element[3]:
#         print(element[0])

# 2. Create a set of all unique countries represented in the list.

# countries = []
# for element in users:
#     countries.append(element[2])


# st_countries = set(countries)
# print(st_countries)


# 3. Count how many users are adults (age >= 18).

# count = 0

# for element in users:
#     if element[1] >= 18:
#         count += 1

# print(count)


# 4. Detect duplicate users based on username (no username should appear twice).
#    Store duplicate usernames in a list without repeats.

# username = []
# for element in users:
#     username.append(element[0])
# print(username)

# non_dup_usrnames = set(username)
# print(non_dup_usrnames)

# l_non_dup_usrn = list(non_dup_usrnames)
# print(l_non_dup_usrn)


# for alement in username:
#     new_dup = []
#     for element in l_non_dup_usrn:
#         if alement == element:
#             new_dup.append(alement)

# print(new_dup)

# 5. Using enumerate(), print the index and username of each user
#    in the format: "Index X: username"

# for i, name in enumerate(username):
#     print(f"Index {i}: {name}")

# 6. Create a dictionary where:
#    - keys are countries
#    - values are lists of usernames from that country

# result = {country_: user_name for user_name, _, country_, _ in users}

# print(result)


# 7. Use a conditional expression (ternary operator) to print:
#    "All users inactive" or "At least one active user"
#    based on the data.

# users = [
#     ("ali", 22, "NL", True),
#     ("sara", 17, "BE", False),
#     ("omar", 30, "NL", True),
#     ("fatima", 22, "DE", True),
#     ("ali", 22, "NL", True)
# ]

# has_active_user = any(user[3] for user in users)

# print("At least one active user" if has_active_user else "All users inactive")

# ====================================================
# Exercise 2: System Access & Validation Loop
# ====================================================

# You are building a simple access-control simulation.

# Given:
allowed_ids = (101, 102, 103, 104)
banned_ids = {999, 666}

# Tasks:

# 1. Use a while loop to repeatedly ask the user for an ID (input).
#    - Stop the loop if the user enters "exit".

usr_inp = int(input("Please enter your ID. To exit,-> enter:exit\n"))

id_

while usr_inp != "exit":


    if usr_inp in allowed_ids:
        print(F"Access granted. Welcome back user {usr_inp}")
    elif usr_inp in banned_ids:
        print("Access permanently denied")
        break
    else:
        print("invalid input")
    usr_inp = int(input("Please enter your ID. To exit,-> enter:exit\n"))
        


# 2. Convert the input safely to an integer.
#    - If conversion fails, print "Invalid input" and continue.

# 3. If the ID is in banned_ids:
#    - Print "Access permanently denied"
#    - Break the loop immediately.

# 4. If the ID is in allowed_ids:
#    - Print "Access granted"
#    - Continue asking for IDs.

# 5. If the ID is neither allowed nor banned:
#    - Print "Access denied"

# 6. Track all attempted IDs in a list.

# 7. After the loop ends:
#    - Print the total number of attempts
#    - Print the unique attempted IDs (use a set)
#    - Print whether any banned ID was ever attempted (True / False)
