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

# selfish = "01234567"
#         # _01234567_

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
# Lesson: Exercise: Type conversion

# coding an age guessing program by entering the birth year. 

# import datetime

# user_birthyear = int(input(f"Hello, I can guess your age by knowing your "
# "birth year,\nPlease enter your birth year to know your age:\n"))


# current_dt = datetime.datetime.now()
# current_year = current_dt.year

# # print(current_year) we have tested that it worked. very nice

# age = current_year - user_birthyear

# if age == 1:
#         print(f"You are {age} year old!")
# else:
#         print(f"You are {age} years old!")


# ----------------------------------------------------------------
# Lesson: DEVELOPER FUNDAMENTALS: II


# ---------------------------------------------------------------
# Lesson:  Exercise: Password Checker


# user_name = input(f"Please enter your username:\n")
# user_passwrd = input(f"Please enter your password:\n")

# star_secret = "*"
# passwrd_length = len(user_passwrd)
# keep_secret = passwrd_length * star_secret


# print(f"Hello {user_name}, your password: \"{keep_secret}\", is {passwrd_length} letters long!")


# ---------------------------------------------------------------
# Lesson: Lists

# a list is a ordered sequence of objects , that can be of any type.

# lst = [1,2,3,4,5]
# lst2 = ['a','b','c']
# lst3 = [1,2,'s',False]

# list is a collection of items, or "Arrays" if you will.
# data structure is a container around you data. that contains for example the list in the objects ina contained fashion. those brackets acts like data structure. 

# amazon_cart = ['notebooks','sunglasses']
# print(amazon_cart[1])



# ---------------------------------------------------------------
# Lesson: List Slicing

# with string slicing we were able to slice a variable that contained strings, we were using this format to slice: [start:stop:stepover]. with this were able to start and stop and stepover at the desired index(Caracter) we wanted.

# so list slicing is also a thing.



# amazon_cart = [
#         'notebooks',
#         'sunglasses',
#         'toys',
#         'grapes',
# ]

# print(amazon_cart)

# strings are immutable
# but lists ARE mutable. 

# amazon_cart[0] = 'laptop'
# print(amazon_cart[1:3])
# print(amazon_cart)

# when you slice a list, you are creating a new list, a copy of the existing list and then modified according to how you have sliced the list. 


# new_cart_list =  amazon_cart[1:3]
# new_cart_list[0] = 'gum' 
# print(new_cart_list)
# print(amazon_cart)

# you can see when  you run this code that is has become a different list in accordance with what you have sliced. 
# you can even change te object in the list again and make a new list out of the new list!

# evertime you do list slicing you make a copy of the existing list. 


# ---------------------------------------------------------------
# Lesson: Matrix

# a matrix is a way to describe a 2D lists, or multi dimensional lists. it is reconizable by looking the array that is within the array were the numbers are. 

# matrix = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
# ]

# it is used in machine learning, photo procesing, etc. 


# print(matrix[0][1])

# accesing information on an array or lists in python we use the term list.


# ---------------------------------------------------------------
# Lesson:  List Methods - Part 1.


# basket = [1,2,3,4,5]


# adding 


# new_list = basket.append(100)
# print(basket)
# print(new_list)

# when you append in does it in place, which means it doesnt do anything else, so you have to first append and then make it a new list. this is unlike list slicing where you get a new copy of the list. which does not happen here. 

# basket.append(100)
# new_list = basket
# print(new_list)
# ----------------------------


# basket.insert(4, 100)
# new_list = basket
# print(new_list)

#same insert modify's the list in place, that it doesnt realy output a new list, it just modifys whatever is existing in memory.


# new_list = basket.extend([100, 101])
# new_list = basket
# print(new_list)
# ---------------------------------



# basket = [1,2,3,4,5]
# #adding
# basket.extend([100])

# print(new_list)

# removing
# new_list = basket.pop(4)
# with pop we want to specify the index, we want to remove, en if you print it like here above , it returns whatever you have just specified to remove.  

# new_list = basket.remove(4)
#and with remove method we want to specify the value we want to remove. 
# print(new_list)

# and remove is still a method that works in place. which means it just removes whatever is existing in a memory, without making new list

#some methods returns none, when you modify a list, which means that it's only going to change or extend a list that it was given, so it wont give you a new list of what you have changed. you still would need to specify a new variable for the changed variable by assigning a new variable to the variable AFTER you have changed is like this for example
# basket. remove(4)
# new_list = basket
# THEN YOU HAVE A NEW MODIFIED LIST. 
# print(new_list)


# new_list = basket.clear()
# print(basket)

# clear removes whatever is in the list of basket. 




# ---------------------------------------------------------------
# Lesson:  List Methods - Part 2. 

# basket = ['a','b','c','d','e']

# print(basket.index('d', 0, 4))



# print('d' in basket)


# print('i' in 'Hi my name is Ian.')

# print(basket.count('d'))

# ---------------------------------------------------------------
# Lesson:  List Methods - Part 3.

# basket = ['x','a','b','c','d','e','d']

# print(basket.sort())

# basket.sort()
# print(basket)

# print(sorted(basket))

# sorted_list = sorted(basket)

# print(sorted_list)

# new_basket = basket.copy()
# new_basket.sort()

# basket.sort()
# basket.reverse()

# print(basket)

# ---------------------------------------------------------------
#

# # Exercise List Methods
# # SCROLL FOR ANSWERS!
# # using this list,
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# # 1. Remove the Banana from the list

# basket[0] = ""
# # print(basket)

# # 2. Remove "Blueberries" from the list.

# basket.remove("Blueberries")
# # print(basket)

# # 3. Put "Kiwi" at the end of the list.

# basket.append("Kiwi")
# # print(basket)

# # 4. Add "Apples" at the beginning of the list

# basket.insert(0, "Apples")
# # print(basket)

# # 5. Count how many apples in the basket

# app_count = basket.count("Apples")
# # print(app_count)

# # 6. empty the basket

# basket[:] = []
# print(basket)


# ---------------------------------------------------------------
# Lesson: Common List Patterns

# basket = ['x','a','b','c','d','e','d']
# basket.sort()
# basket.reverse()



# print(len(basket))
# print(basket[::-1])

# print(list(range(101)))



# new_sentence = " ".join(["hi", 'my', 'name', 'is', 'JOJO'])

# print(new_sentence)



# ---------------------------------------------------------------
# Lesson: List unpacking

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# so list unpacking is essentialy exploding the list into variables and assiginng the exploded element to its var, while the * function  makes sure that the rest that is not exploding still is in the list or is protected from exploding/list unpacking. 


# ---------------------------------------------------------------
# Lesson: None

# None stand for absence of value. 

# ---------------------------------------------------------------
# Lesson: Dictionaries

# Dictionary

# dictionary = {
#     'a' : 1,
#     'b' : 2,
#     'x' : 3
# }


# print(dictionary)

# here b is the key and 2 is the value.
# a dictonary is a unordered key value pair
# it means that the pair are not next to each other in memory.  with list we could access it in an orderly manner by using the index of 0 and then index of 1.abs

# a dictionary on the other hand are al over the place

# ---------------------------------------------------------------
# Lesson: DEVELOPER FUNDAMENTALS: III


# a dictionary hold more information than a list.
# while a list have only a variable and a index asigned to it.

# ---------------------------------------------------------------
# Lesson: Dictionary Keys

# dictonary = { 
#     123: [1,2,3],
#     True: 'hello',
    
# }

# print(dictonary[True])

# dictionary key's are immutable,  which means a value that can be changed. because of that anything that has been assigned to the key of a dictionary will be an immutable datatype which means that you cannot assign a list to a key. while the value can have a mutable datatype.
# A key in a dictionary has to be unique, there can only be one key. anytime you make a key with the same name it overides the precvious one.


# ---------------------------------------------------------------
#  Re doing, Lesson:Dictionary


# Dictionary

# dict 

# dictionary = {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True  
# }

# my_list = [
#     {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True  
# },
# {
#     'a': [4,5,6],
#     'b': 'hello',
#     'x': True  
# }

# ]

# print(my_list[0]['a'][2])
# print(dictionary['a'][1])


# a dictionary is a unordered key-value pair.
# which means that they are not right next to each other on the memory. every pair will be in random in memmory. 


# dictionary key's needs to have special property,
# a key is a value that cannot changed. so if you asigned a list to a key, it wont work because lists are mutable but in a dictioanary key you cant have a mutabable.

#  so you can only have a immutable dictionary key.

#  a key in a dictionary has to be unique, there can only be one key,, because that key represent a book shelve in that memory space.

# if you still use two same key names, then its going to overide the previous one with the last one.

# ---------------------------------------------------------------
#  Re doing, Lesson: Dictionary Methods


#Dictionary

# user = {
#     'basket': [1,2,3],
#     'greet': 'hello',
#     'age': 20
# }

# user2 = dict(name='JohnJohn')
# print(user2)


# ---------------------------------------------------------------
#  Lesson: Dictionary Methods 2

