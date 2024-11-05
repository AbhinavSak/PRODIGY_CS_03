import re

password = input("Enter the password : ")
if len(password) < 8:
    print("password must be of 8 characters long" )
elif not re.search("[A-Z]", password):
    print("password must contain one upper case letter")
elif not re.search("[a-z]", password):
    print("password must contain one lower case letter")
elif not re.search("[0-9]", password):
    print("password must contain one digit")
else:
    print("password is strong")  