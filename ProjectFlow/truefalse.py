# day = "Saturday"
# temperature = 30
# raining = True #Capital T***
#
# if (day == "Saturday" and temperature > 27) or not raining: #using () is good practice for and + or statements
#     print("Go swimming")
# else:
#     print("Learn Python")

if 0:
    print("True")
else:
    print("False")  #Will evaluate to False since 0 = false in boolean terms

name = input("Please Enter Your Name: ")
if name != "":                                  #comparing name to empty string
    print("Hello {}".format(name))
else:
    print("Are you the man with no name?")
