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

# what comes after = here abve, is a expression. it is a piece of code that produces a value ->{iq / 5}. this produces a value that would be asign to user_age. it is not the answer that is the expression but exactly what i asign with the arcel that is the expression. the expression is the cause and what come out of it is the consquense in this situation the value assign to the variable: user_age

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


# user = {
#     'basket': [1,2,3],
#     'greet': 'hello',
#     'age': 20
# }

# print(user.update({'ages':55}))
# print(user)

# ---------------------------------------------------------------
#  Lesson: Tuples

# Tuple

# my_tuple = (1,2,3,4,5)

# Tuples are immutable, once created, it is the way it is.
# you cant sort it, or reverse it like a list.

# print(5 in my_tuple)

# Tuples are good, if you dont want to change the existing list. other programmers would't be able to make mistakes either(atleast if they dont like force it.)

# unlike a list you want to stay tuples the way it is, it makes thing easier and more efficient. 

# It makes code more predictable, however it is less flexible than a list. and because they are less flexible the other good thing about them is that they are slightly more performative than list. which means that they are faster.

# a good example for using a tuple instead of a list is, that if you work at uber. their geographic location and coordination doeesnt often changes. so you use a tuple. 

# while your car may move so we have to use list as the coordination of you car keeps changing. 

# in dictionaries you can use tuple's as a value for key for dictionaries. for example:

# user = {
#     (1,2): [1,2,3]
# }

# the key here as you can see is in tuples, as keys are immutable and tuples too. 

# print(user[(1,2)])


# ---------------------------------------------------------------
#  Lesson: Tuples 2

# # Tuple
# x,y,z, *other = (1,2,3,4,5)


# print(other)

# a tuple has 2 methods that we care about, mostly the ones that we use are count() and index(). count returns the number of times a specified value occurs in a tuple. and index Searches the tuple for a specified value and returns the position of where it was found. 

# my_tuple = (1,2,3,4,5,5,5,5)

# print(len(my_tuple))

# ---------------------------------------------------------------
#  Lesson: set

# sets are unordered collection of unique objects, 
# are over the place in memory


# my_set = {1,2,3,4,5,5}
# my_set.add(100)
# my_set.add(2)

# print(my_set)

#  in a sets there are no duplicates.

# my_list = [1,2,3,4,5,5]

# my_set = set(my_list)

# print(my_set)

# Converting, This would be usefull when using emails, like when collecting emails for a page, you dont want to collect duplicate emails, as you already have the same email in the system. which would be not efficent and unnaccary usage of resources. 

# my_set = {1,2,3,4,5,5}
# print(my_set[0]) doesnt work

# print( 1 in my_set)
# print(len(my_set))

# new_set = my_set.copy()

# my_set.clear()
# print(new_set)


# ---------------------------------------------------------------
#  Lesson: set 2 methods


# my_set = {4,5}
# your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# print(my_set.discard(5))
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set.intersection(your_set)) & print(my_set &your_set)
# print(my_set.isdisjoint(your_set)) 
# print(my_set.union(your_set)) or print(my_set | your_set)
# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))


# ---------------------------------------------------------------
#  Lesson: Conditional Logic


# is_old = False
# is_licenced = False

# if is_old and is_licenced:
#     print(f"You are old enough to drive, and you have a licence!")
# elif condition:
# elif condition:
# else:
#     print(f"You are not of age!")

# print("okoko")

# ---------------------------------------------------------------
#  Lesson:Indentation In Python

# The indentation within the python editor makes it such that conditions are put much more logical to use. 

# so with indentation you have to be aware that there is a hiarchy with the spaces. if the is no space, en next line has space then you know that the first line is the parent of the second line. 

# At the same time the child belongs to that specific parent and if the parent doesnt get excecuted the child would not be executed either :o. which make that a code of block on it's own.

# ---------------------------------------------------------------
#  Lesson: Truthy vs Falsey

# is_old = bool('hello')
# is_licenced = bool(5)

# print(bool('hello'))
# print(bool(5))
# Both of them here above code print True; this is what we call a Truthy value in python. As this value what we have given above comes out as True. 

# print(bool(''))
# print(bool(0))
# print(bool(None))
#Both of the here above code print False; It's not actualy false, but it is Falsey because if we run the boolean code on it to phython; mostly there is no value to it so it shows False. 

# user_name = "Maximilion"
# pass_word = "123"

# if pass_word and user_name:
#     print(f"Welcome back user!")
# else:
#     print(f"please Enter your username and password")

# In this situation the values are both truthy so when the conditional code check if the value is true, it comes out as truthy for both of them so the condition of if would be excuted which is to print welcome back user. 

# ---------------------------------------------------------------
#  Lesson: Ternary Operator


# Ternary Operator's are called conditional expression's.
# an expression evaluate to evalue. conditional expression is operation that evaluete's to something based on the condition being True of False. 

# condition_if_true if condition else condition_if_false

# Facebook coding situation 
# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message) 

# ---------------------------------------------------------------
#  Lesson: Short Circuiting

# is_friend = True
# is_user = True

# if is_friend or is_user:
#     print("best friends forever")

# short circuiting is when the interpeter executes the code until i thinks it did enough. for example here above. whe the if condition for the is friend became true, because of the or, condition that if either one of the is true that you can print best friends forever. so basicaly python stops at the first excustion if possible rather than going trouthg the whole code if allowed like here. if it was and. then pytthon would have to check if both conditions are True, which goes trout both condition first to check if both of them needed to get printed.. 

# if you need to check both statements you will have to use and.

# this is about efficieny, and by using this method whenever possible you make the code efficent.


# ---------------------------------------------------------------
#  Lesson: Logical Operators

# and , or , not are logical operators. Almost like math's.

# well that was easy, we just had a lesson and the next lesson is the excercise about it 

# print(5>3)
# print(10<30)
# print(4>3)
# print(7<1)
# print(90>120)

# ---------------------------------------------------------------
#  Exercise: Logical Operators

# is_athlete = True
# is_expert = False

# # check if atlete and professional: "You are a professional athlete!" 

# #check if athlete but not professional:
# # "at least you're getting there..."

# #if you're not a athlete: "you need to train!"


# if is_athlete and is_expert:
#     print(f"You are a professional athlete!")

# # down here is how i did it, and down there is how it supposed to be. 
# # elif is_athlete and is_expert == False:
# #     print(f"at least you're getting there...")

# elif is_athlete and not is_expert:
#     print("at least you're getting there")

# # my way under
# # else:
# #     print(f"you need to train!")
 
# elif not is_athlete:
#     print(f"you need to train!")


# ---------------------------------------------------------------
#  Lesson: is vs ==

# # None is a special object that represent "no value" in a code
# print(None == None)

# # Zero is a nummerical value that represent the number 0.
# print(None != 0)

# print([] == None)
# # As a empty list(array) it has nothing in it, but it still represent a list or an Array as an existing object. 

# print([] == 0)
# # An empty array is object with nothing in it, and represents falsy, while a zero is a numerical value with the value of zero. which mean that they are not equal to each other

# # All of these above; The list(Array), 0(zero) and None are represented Falsey. but are not the same in value. as they a mean different things.

#  == checks for equality, "is" actualy checks the value in the same memmory
# while a list, a data structure is created everytime in a new location, will be memorized in different locations and does not come True with "is". 
# so "is" operator checks for the exact thing that you are looking for. and if there is it will come out as True. 
# while "==" operator checks the value. 

# ---------------------------------------------------------------
#  Lesson: For Loops

#  for are for-loops called

# for item in 'Zero to Mastery':

#  so basically its says here for every item in zero to mastery do something
# The 'zero to mastery' in the for loop above is what is called a itterable,
# an itterable is something that is able to get looped over. 

# for item in 'Zero to Mastery':
#     print(item)


# for something in object:(do the following here under)
            # print(something)

# Terminal:
# Terminal will then print something that is in the object in this situation a string or an array(list,tuples,sets). so for every value that is within the object python will execute the command that you have given to do, under it's for loop line after ":". 
# make note, for EVERY element in the object, do this action. 
# when reading for loop. 

# for element in [1,2,3,4,5]:
#     print(element)
#     print(element)
#     print(element)
# print(f"hi")


# for element in [1,2,3,4,5]:
#     print(element)
#     print(element)
#     print(element)
# print(element)

# notice that the terminal is giving the output of 5. That is because the for loops ends with 5 so it outputs a 5. 


# here you see that you can nest for loops. 

# for element in [1,2,3,4,5]:
#     for x in ['a', 'b', 'c']:
#         print(element, x)

# # my guess what the output would be: 
# 1a1b1c
# 2a2b2c
# 3a3b3c
# 4a4b4c
# 5a5b5c

# i was wrong, but i understand my mistake. that is that it prints every element in the nested loop, which means that it doesnt print everthing of the object at the same time, because the nested loop is STILL a loop. so i have to go overthat action for every element that the nested loop has. 

# ---------------------------------------------------------------
#  Lesson: Iterables

# Iterable simply means it is an object or a collection that can be iterated over. basicly something you can keep repeating on until you cant according to the code. 

# iterable - list, dictionary, tuple, set, string. 

# iterated -> is the action of: one by one check each item in the collection. 

# user = {
#     'name' : 'Golem',
#     'age': 5006,
#     'can_swim': False
# }

# for item in user:
#     print(item)

# Dictionaries have three methods that are very useful when looping over their keys and values. 

# user = {
#     'name' : 'Golem',
#     'age': 5006,
#     'can_swim': False
# }

# for item in user.items():
#     print(item)

#  .items()    # The first method is .items(). with this method you get the key   and the value when iterating over a dictionary. 

#  .values()   # then you have the .values(), here the values gets iterated

#  .keys()     # finally the .keys(). for keys. This is more descryptive.  


# here above the ouput returns in tuple,
# and here under is to return the ouput in seperate columns
# tuplle unpacking.


# user = {
#     'name' : 'Golem',
#     'age': 5006,
#     'can_swim': False
# }

# for item in user.items():
#     key, value = item
#     print(key, value)

# for cleaner and faster method

# for key, value in user.items():
#     print(key, value)

#  you might even see this: for k, v in user.items():

# an integer value is not a object or collection of item that can be iterated over. 

# ---------------------------------------------------------------
#  Lesson: Exercise: Tricky Counter

# Counter

# my_list = [1,2,3,4,5,6,7,8,9,10]

# summed_result = 0

# for element in my_list:
#     summed_result += element

# print(summed_result)

# could have done here like here under. 
# my_list = [1,2,3,4,5,6,7,8,9,10]

# summed_result = 0

# for element in my_list:
#     summed_result = summed_result + element

# print(summed_result)

# ---------------------------------------------------------------
#  Lesson: range()

# range() is a special type of object/function that used in for loops, you can iterate of that range. 
 
# for number in range(0, 100):
#     print(number)

# when specifiying range you can have a 3 parameter, that stands for stepover. 
# depending on the value of the parameter you can change the order of the range you have specified and also to step over a value, which is to skip one value in range of order. 

# for _ in range(0, 10 , 2):
#     print(_)

# puting  the last value in negative would reverse the range in which it riterates but have to but the max value first in range. 

# This wont work.
# for _ in range(0, 10 , -1):
#     print(_)

# correct. for reversing
# for _ in range(10, 0, -1):
#     print(_)


# you loop also the printing of the list, in this example below the output would be: 2 times list from 0 to 9. 
# for _ in range(2):
#     print(list(range(10)))

# quick way to create a list that has integers

# ---------------------------------------------------------------
#  Lesson: enumerate()

# enumarete = To count off or name one by one; list. 
# in python enumerate takes a collection and returns it as an enerated object. it also ads as counter as the key of the enumerate object. 

# ultimatelly enumerate is usefull if you need the index counter of the item that youre looping through. 

# for i, element in enumerate('hello'):
#     print(i, element)


# Excercise 

# for i, element in enumerate(list(range(100))):
#     if i == 50:
#         print(f"The index of 50 is: {i}!")
# youre asking for the index of 50, not that index is 50. and not the element of the range object. 

# This is a nice way to check if there is something in a list youre searching for 
# for i, element in enumerate(list(range(100))):
#         print(i == 50, element)

# ---------------------------------------------------------------
#  Lesson: While Loops


# There is another way to loop besides for loop.
# while a condition is happening do something.

i = 0

# while i < 50:
#     print(i)
    
# This will keep printing the zero output as the "i" stays fifty in accordance with the code. unless the machine turns of it will keep printing and executing its code. that is why a while loop can be dangerous. you can solve this with the 'break' python keyword. it simply breaks the while loop when you code that into the code. as in example. 

# while i < 50:
#     print(i)
#     break

# breaking out of the while loops can also be done by turning a condition into false. Notice that it stop right before 50, because the loops goes on while 0 is smaller than 50. so it prints zero until 49. 

# while i < 50:
#     print(i)
#     i += 1

# else, the else statement in a while loop either gets executed if the condition is false for the while loop or when the condition becomes false after the true condition became false because of the execution of the code. 

# while i < 50:
#     print(i)
#     i += 1
# else:
#     print('done with all the work.')

# The reason for using else instead of just writing it in a new line is because when you use the break function word to break the loop. you execute the while loop and and consider the while loop to be true, then it ignores the else for what it should do because there is no need to execute else code. so basicly the while loop goes then the else or while loop false so else. with break: the while loop goes;while is positive so break, ignore else. 

# while i < 50:
#     print(i)
#     i += 1
#     break
# else:
#     print('done with all the work.')

# ---------------------------------------------------------------
#  Lesson: While Loops 2

# for simple loops or iterating over iterable object for loops are great. 
# if you are not sure how long you want loop something, or you want to keep looping until something; a condition. for example; to go trough a email list that you have collected on a website and for each email list you want to send a email. While the list is still keep sending emails. 

# The most used ways for while loop is like this:

# while True:
#     response = input("say something: ")
#     if (response == "bye"):
#         break

# while loops are use fu for tasks like this, where you dont know how long it's gonna take to do it. or for conditional. 

# ---------------------------------------------------------------
#  Lesson: break, continue, pass

# The key word break works for the for loops as well. 
# The continue key word is used for continueing the iteration. 
# pass is just goig to the next line, you can use this as a place holder. you want to loop through the for loop but we dont know what want to do yet, you can use pass as a temprorary something so you can code further. 
# my_list = [1,2,3]
# for item in my_list:
#     pass
#     print(item)


# i = 0
# while i < len(my_list)
#     pass
#     print(item)

# ---------------------------------------------------------------
#  Lesson: Our First GUI

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!



# i am going to divide and conquer in sha Allah. 
# pic_first_cel = [0,0,0,1,0,0,0]

# result_cel = ""

# for cel in picture:
#   if cel == 1:
#     result_cel += "*"
#   else: 
#     result_cel += " "
# print(result_cel)


# now i going to test how to add two cels so the output prints the image in manner come horizontally with every itteration. 

# two_cel = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0]
# ]


# for element in two_cel:
#   cel_result = ""
#   for cel in element:
#     while cel == 1:
#       cel_result += "*"
#       break
#     else:
#       cel_result += " "
#     result = cel_result
#   print(result) 

# my explanation:
# so if i want to accumulate a variable i put it outside of a loop of that loop, if i want to reset it i do it within the loop. and then i have to also look out that in a nested loop i do this within the firs loop , outside the first nested loop because i only want to acumulate the value from every cell, and not from every element, that every element keeps getting added, no i want to only add the thinngs in the element, which are the cellss toegher in one line string, print that and start anew, so this happens again for the next element 

# chat-gpt explanation
# - Accumulate values: define variable outside the loop.
# - Reset values: define variable inside the loop.
# - Nested loops:
#   - Outer loop: bigger units (e.g., cels)
#   - Inner loop: smaller units (e.g., cells)
#   - To accumulate inner units but reset per outer unit, define accumulator inside outer loop but outside inner loop.
# - Concept: build string from inner elements, print after outer iteration, then start fresh.
# - Key insight: placement of variable initialization controls what persists vs resets.



# Excercise results:

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for element in picture:
#   cel_result = ""
#   for cel in element:
#     while cel == 1:
#       cel_result += "*"
#       break
#     else:
#       cel_result += " "
#   print(cel_result)


# Successful!!!!


# excercise solution:
# i should write a strategy of what i want to do.
# and use end="" to continue printing in the same row of the iteration(loop)



# ---------------------------------------------------------------
#  Lesson: DEVELOPER FUNDAMENTALS: IV


# What is clean good code?

# Clean
# Readability  
# predictability
# DRY ; Do not repeat yourself

# ---------------------------------------------------------------
#  Lesson: Exercise: Find Duplicates

#  Exercise: Check for duplicates in list:

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# .count
# append()

# i want to check how many time something happends in a list,
# i do that wit len(), 
# if something from some_list has more of the same value
# so i searched on internet, and i can use the count method for lists to count the same value that apear in the list we can use this, that if a element come more that 1 time then add that to the dup list. 

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
 
# dup_lst = []

# for element in some_list:
#     if some_list.count(element) >= 2:
#         if element not in dup_lst:
#             dup_lst.append(element)


# print(dup_lst)


# success Alhamdulillah!



# using a while loop only 
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# indx_numb = 0

# dup_lst = []

# while indx_numb < len(some_list):
#         element = some_list[indx_numb]
#         if some_list.count(element) >= 2:
#             if element not in dup_lst:
#                 dup_lst.append(element)
        
#         indx_numb += 1

# print(dup_lst)


# ---------------------------------------------------------------
#  Lesson: Functions

# Functions are 

# def is defining a function, you use the same naming
# protocol to define a function

# Built-in functions = Python gives you ready-made tools (print(), len(), etc.) you can use immediately.

# Your own functions = You define reusable blocks of code that act like your own custom tools for your program.

# def say_hello():
#     print('hellooooo')

# say_hello()


# Dont forget the brackets. after the functions, otherwise 
# python won't executed it.

# The function is a powerfull to reause the same code 
# you want to execute without repeating your self. DRY
# Dont repeat yourself. 


# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# def image_printer():
#     for element in picture:
#         cel_result = ""
#         for cel in element:
#             while cel == 1:
#                 cel_result += "*"
#                 break
#             else:
#                 cel_result += " "
#         print(cel_result)


# image_printer()
# image_printer()
# image_printer()

# you cannot put you custom function above the cunstom function code
# so you have to try to define functions above rest of the code. 


# ---------------------------------------------------------------
#  Lesson: Parameters and Arguments
# parameters


# def say_hello(name, emoji): 
#     print(f"hellloooo {name} {emoji}")



# Arguments 
# say_hello("abdullah", ':)')

# call or invoking the function 

# 

# say_hello('Muhammad saw', ':)')
# say_hello('hisam', ':)')
# say_hello('myself', ':)')

# with this we keep our code DRY and Clean. 


# ---------------------------------------------------------------
#  Lesson: Default Parameters and Keyword Arguments


#Parameters
# def say_hello(name, emoji): 
    # print(f"hellloooo {name} {emoji}")



#  positional Arguments 
# say_hello("abdullah", ':)')

# positional Argument Are arguements that require to be in the proper position 


# There something called keyword argument. it allowes us to not worry about the possition. 

# say_hello(emoji=':)', name='bibi')

# This is bad practices. you should stick to the postional arguments in accordance with the function. 
# sometime keyword arguments are sometimes confused with default parameters. 
# keyword arguments increases readability because you know exactly why we say hello. 
# but positional arguments are still more important to use because you are following the functions and is easy to read, to say it practical it is what the Profesionals do. 

# Default Parameters:
# def say_hello(name='Darth Vader', emoji='>:D'): 
#     print(f"hellloooo {name} {emoji}")

# say_hello('abdullah', ':)')

# say_hello()

# When there is nothing in the function specified when used then this allowed there still to have a specified default parameter that was already embedded in the function. It's literally in the name Default Parameter. 
# Default functions allows us to be little bit more safe to make sure that when we use a variable that we are gonna have a Default answer no matter what. 
# regarless of how being called. 



# ---------------------------------------------------------------
#  Lesson: return


# def sum(num1, num2):
#     return num1 + num2


# print(sum(10, 5))

# Function can return something, or we can have function that doesn't return anything but modifies something. 

# A Function should do one thing realy wel
# A Function should return something 

# total = sum(10, 5)
# print(sum(10,total))

# --------------------------

# Example 1: Original code
# def sum(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2

# total = sum(10, 20)
# print(total)  # Output: None

# Explanation:
# - The outer function 'sum' does not return anything, so by default it returns None.
# - Defining an inner function 'another_func' does not call it automatically.
# - You must call the inner function and return its result to get a value.

# Corrected version: Returning the inner function result
# def sum(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2
#     return another_func(num1, num2)  # Call and return the inner function's result

# total = sum(10, 20)
# print(total)  # Output: 30

# Inner Function Return Behavior:
# - If you call the inner function and return it (return another_func(num1, num2)),
#   the outer function gives the actual value.
# - If you return the inner function itself without calling it (return another_func),
#   the outer function gives the function object (memory reference).
# - To get the value from the returned function object, you must call it separately.


# Key Points:
# 1. Inner functions need to be called explicitly.
# 2. Outer functions must return a value if you want to use it outside.

# Optional Variation: Returning the function itself (closure)
# def sum(num1, num2):
#     def another_func(num1, num2):
#         return num1 + num2
#     return another_func  # Return the function object itself

# func = sum(10, 20)      # 'func' now holds the inner function
# total = func(10, 20)    # Call it separately
# print(total)            # Output: 30

# Use case: Useful for functional programming, closures, or reusable inner functions.

# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func(num1, num2) 
#     return 5
#     return ('hello')

# total = sum(10, 20)
# print(total)

# as soon as you return something from a function it exists the function
# the last to wont be executed. 



# ---------------------------------------------------------------
#  Lesson: Exercise



# def check_driver_age(age=0):
#     user_input = input("What is your age?: ")
#     if  user_input != "":
#         age = int(user_input)

#     if (age) < 18:
#         message = "Sorry, you are too young to drive this car. Powering off"
#     elif (age) > 18:
#         message = "Powering On. Enjoy the ride!"
#     elif (age) == 18:
#         message = "Congratulations on your first year of driving. Enjoy the ride!"
#     return message

# print(check_driver_age())


# ---------------------------------------------------------------
#  Lesson: Methods vs Functions

# what every is on the left of the method owns the method.


# ---------------------------------------------------------------
#  Lesson: Docstrings

# def test(something="a"):
#     '''
#     Info: This function test and prints para a
#     '''
#     return something

# # with Docstring it allow us to comment inside of functions in way that another person/co-workers/coleges would be able to know what it is by typing or hovering over the function. 
# print(test())

# help(test)
# # we can use the function 'help' to look what something is when it comes to function and the out put will then explain it when there are docstring atached to the function. 

# print(test.__doc__)
# # This method also allows you to know what the function does and info about it. 

# ---------------------------------------------------------------
#  Lesson: Clean Code

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else: 
#         num % 2 != 0
#         return False

# print(is_even(90))

# so to clean this code, you need to look what you truly need. and int his situation you only need to know if a number is even. so what you do instead is this:
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else: 
#         return False

# print(is_even(90))


# you remove the unnecassary condition in else, and just keep return to false, as there are only 2 outcomes so with this code is cleaner. 
# in fact you dont even need else because if something is true it will do the first return and then it will exit the function. thats why can do this:
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
#     ''' if the first condition is not true/False, then  it will go to the next line and return false'''

# print(is_even(90))

# To make it even cleaner and to the point of ridicalousnessm, you can even remove the booleans all togheter. as Expressions in Python evaluate to a boolean True or False.: 
# def is_even(num):
#     return num % 2 == 0

# print(is_even(90))

###
# ⭐clean explanation
# Expression = something that evaluates to a value.
# Statement = something that performs an action (assign, loop, define), but doesn’t return a value.
###

# ---------------------------------------------------------------
#  Lesson: *args and **kwargs