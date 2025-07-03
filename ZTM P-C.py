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


# Fundamental Data Types
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


#Operator precedence

# print(20 + 3 * 4)

# What takes priority(essentially just like math's):
# ()
# **
# */
# +-

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

print(bin(5))
print(int('0b101', 2))
