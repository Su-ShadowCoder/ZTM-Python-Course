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

# iq = 100

# user_age = iq / 5

# what comes after = here abve, is a expression. it is a piece of code that produces a value ->{iq / 5}. this produces a value that would be asign to user_age. it is not the answer that is the expression but exactly what i asign with the arrow that is the expression. the expression is the cause and what come out of it is the consquense in this situation the value assign to the variable: user_age

# A Statement on the other hand is a entire line of code in this 
# example: user_age = iq / 5
# that perform a action.
# so what happens is 100/5 and then assigning that value to the user_age

# ------------------------------------------------------
# Lesson: Augmented Assignment Operator

# some_value = 5
# some_value = 5 + 2
# some_value = some_value + 2

# or 
# Augmented assignment Operator
# some_value += 2
# some_value *= 2

# The operator comes to the left of the equel signed.


# --------------------------------------------------
# Lesson: Strings

# str = string, a string is a collectrion of character's within the quotions marks "".


# print(type(f"hi hello there!"))

# user_name = "supercoder"
# pass_word = "supersecret"
# long_string = """ you can write this as it is
# and you dont have to worry about line and can write multiline strings"""

# first_name = "suda"
# last_name = "kanda."
# full_name = first_name + " " + last_name
# print(f"{full_name}")

# ----------------------------------------------------
# Lesson: string Concatenation
# it means adding strings togheter

# print(f"hello" + " " + "suda")

# string Concatenation only works with Strings
# print(f"hello" + 5) ---> Error message.


#  -------------------------------------------------------
# Lesson: Type Conversion:

# print(type(str(100))) 

# we have converted 100 into a string 

# print(type(int(str(100))))

# here in a very roundabout manner we have converted an int, into an str into 
# an int finaly. that is because of the brackets order like russian nestling 
# doll. 

# a = str(100)
# b = int(a)
# c = type(b)

# print(c)

# This is the idea of type conversion, we are converting datatype's from one
# data type to another datatype.

# ------------------------------------------------------------------------
# Lesson: Escape Sequences

# problem with quotation marks, so you tell python what ever comes after a
# backslash is a string 

# weather = "It\'s \"kind of\" sunny"
# print(weather)

# ----

# adding a tab spacing

# weather = "\t It\'s \"kind of\" sunny"
# print(weather)

# ----

# another one is using \n for a new line 

# weather = "\t It\'s \"kind of\" sunny, \n hope you have a good day!"
# print(weather)




# ----------------------------------------------------------------
# Lesson: Formatted Strings

# name = "Johnny"
# age = 55
# print(f"Hi {name}. You are {age} years old")
# # here above is the new method of adding variables to a string, which is the best method in my opinion.


# print("Hi {}. You are {} years old".format("Johnny","55"))
# # This is how it used to be before 3.0 python.



# print("Hi {1}. You are {0} years old".format(name,age))
# #Here above is the method of formatting with a certain order. as computer language you start counting from zero. you could just put the variables in the brackets behind the format, and that according to the place the variables, that would be the number assigned to it. as you could see from the example above where because the number is put reverse you could see that age came first and name came second. of course this is wrong but, this just proves how this method works in order, which is right. 



# print("Hi {new_name}. You are {age} years old.".format(new_name="sally", age="100"))
# # With this method you can also make variables in the format statement like here above. 


# ----------------------------------------------------------------
# Lesson: String indexes


# "me me me"
# _01234567_

# -----------


# self_ish =  "me me me"
#         #   _01234567_

# print(self_ish[0])
# print(self_ish[7])

# [start:stop:stepover]


# user_answer = "I like icecream, and I want it now."

# print(user_answer[3:15])
# answer before run: "ike icecream, "

# so i am wrong, the stop starts counting from 0 to 15 and not the start
# from what is required in the statement here above.

# This is called Slicing

# ----------------------------------------------------------------
# Lesson: Immutabilty

selfish = "01234567"
        # _01234567_

# selfish = 100

# # immutability means that strings in python cannot be changed.

# print(selfish)


# but 

# selfish[0] = "8"

# print(selfish)

# you get a error, while slicing, so you have to completely re asign the value

# so this would work -  here under 

# selfish = "8"
# print(selfish)

# you cant re asign part of a string, once created it exist like that in 
# that form. The only way to create is to change into something new and not while slicing. 

# ----------------------------------------------------------------
# Lesson: Built-In Functions + Methods

# greet = "hellloooo"
# print(greet[0:len(greet)])

# and this ladies and gentleman, is a built-in funtion
# print(len(greet))

# then you also have methods which you would be able to refrences when need it,
# through the we3 website or somewhere elso, just google it. 

# .format() is a method 

# why do we care? with th is, python gives us automatic tools that we
# can use on strings.

# quote = "to be or not to be"
# print(quote.upper())

# everthing cam in upper cappital

# quote = "to be or not to be"
# print(quote.capitalize())

# with this it capitalize the first letter from the left.


# quote = "to be or not to be"
# print(quote.())

# when you press dot then you can scroll trough the methods 
# it gives you to use.


# quote = "to be or not to be"
# print(quote.find("be"))

# we have find, which will find  the thing in the first occurence.
# it gives 3, what it means is that there is a be 
# and it starts at index b which is 
# from 0, 1, 2, 3. it starts on the index 3.abs


# quote = "to be or not to be"

# print(quote.replace("be","me"))
# print(quote)

# when you print this you get this: 
# to me or not to me
# to be or not to be

# the reason being is that strings are immutable, so unless you change it
# (overwrite them),
# or completly delete it. it will always gives you the original string that was
# assigned to the variable.

# quote_2 = quote.replace("be","me")
# print(quote_2)

# in here above we are creating a whole new string, but we never modify
# th string because it's immutable.



# ----------------------------------------------------------------
# Lesson: Booleans

# booleans in python is bool. 

# name = "abdullah"
# is_cool = False
# is_cool = True

# print(is_cool)

# print(bool(0))

# ----------------------------------------------------------------
# Lesson:
