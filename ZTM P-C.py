# -------------------------------------------------------
# userinput_name = input(f"Hey, what is your name?")

# print(f"Hello {userinput_name}!")

# user_location = input(f"Where do you come from?")

# print(f"That is very cool that you come from {user_location}!")


# user_name = input(f"Please enter your Username: ")

# print(f"Hello {user_name}.")

# user_pw = input(f"Please enter your password: ")

# password = int(123)

# if int(user_pw) == password:
#     print(f"Password Accepted!")
#     print(f"Access Authorized")
#     print(f"Welcome back {user_name}!")
# else:
#     print(f"Password Incorrect!")
#     print(f"Access Denied")

# hopefully this should work out...

# trying_change = input(f"Helloo i am under the water, are you? ")

# if trying_change == "yes":
#     print(f"OOOhhh nooo, now we both need halp!")
# else:
#     print(f"Please save me, i will reward you!!!")

# Well well well if this isnt the third day i am messing with git XD.

# -----------------------------------------------
# Lesson: Fundamental Data Type

# int and float

# print(type(2+4))
# print(type(2-4))
# print(type(2*4))
# print(type(2/4))

#Still a Float
# print(type(9.9+1.1))

# #exponential
# print(2**3)

# #rounds of to a integer
# print(2//4)
# print(11//4)

#modulo, is to represent what the remainder is of a division
# print(6%4)

# Math functions
# print(round(3.1))
# print(round(3.9))

# print(abs(-20))

# you can google for math functions python 3 if you want to use more functions

#they key is to underestand how to google and use them.


# Lesson: Operator precedence

# print(20 + 3 * 4)

# What takes priority(essentially just like math's):
# ()
# **
# */
# +-

# -----------------------------------------------
# Exercise: Operator Precedence

# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

# print((5 + 4) * 10 / 2)         

# # answer:5 + 4 = 9, 10 / 2 = 5, 9 * 5 = 45

# print(((5 + 4) * 10) / 2)

# # answer: 5 + 4 = 9, 9 * 10 = 90, 90 / 2 = 45 

# print((5 + 4) * (10 / 2))

# # answer:9 * 5 = 45

# print(5 + (4 * 10) / 2)

# # answer:4 * 10 = 40, 40 / 2 = 20, 5 + 20 = 25

# print(5 + 4 * 10 // 2)

# # answer: 4 * 10 = 40, 40 // 2 = 20, 5 + 20 = 25

# i made a mistake in calculating that i didnt take in acount, that when dividing that the numbers become float, and with // it becomes whole so in turns into a integer

# so intsead of 45, i should have answered 45.0


# Optional: bin() and complex

# int float
# complex

# bin turns a number into binary
# print(bin(5))

# turns binary into normal
# print(int('0b101', 2))

# ------------------------------------------
# Lesson: Variables

# example
# storing a value by asinging a name to it. storing information in the computer

# iq = 190
# # the number is bound to the name/id

# print(iq)

# Best practices when programming when using variables:
# -snake_case
# -Start with a lowercase or underscore
# -letters, numbers, underscores
# -Case sensitive
# -Don't overwrite keywords - dont use words that the python language uses, for example dont create a variable with the name print or if or input. Don't use Python keywords


# be carefull with this:
# constants
# PI = 3.14
# PI = 0

# If you see something in full capital case, then that means that that value to that variable is constant. it does not change unless the dev as seen here overwrites the constant value. but then again it would then stay at that last overwritten value.

# Another thing to be careful of is this:
# __

# Here above are 2 underscores, when you see these with a variable these are called: dunder variables.

# Dunder variables are meant to be left alone and you should't touch or change them.

# Naming variables is one the most important skill to have so people understand your code. that is the point of writing good code. writing good code is that its readable and understandble by other programmers.


# This trick here under is to asign variables quickly and multiple times.

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)
# print(a,b,c)

# ----------------------------------------
# Lesson: Expressions vs Statements


