# userinput_name = input(f"Hey, what is your name?")

# print(f"Hello {userinput_name}!")

# user_location = input(f"Where do you come from?")

# print(f"That is very cool that you come from {user_location}!")


user_name = input(f"Please enter your Username: ")

print(f"Hello {user_name}.")

user_pw = input(f"Please enter your password: ")

password = int(123)

if int(user_pw) == password:
    print(f"Password Accepted!")
    print(f"Access Authorized")
    print(f"Welcome back {user_name}!")
else:
    print(f"Password Incorrect!")
    print(f"Access Denied")

