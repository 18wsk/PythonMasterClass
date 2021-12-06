for i in range(1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3)) # :4 width of 4
print("*" * 80) # print 80 stars
#----------------------------------------------------------------------------------------------------------------------
name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name))) #int((( will ensure that age is an integer and will crash if input isnt
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an x in the box")
# else:
#     print("Pleas comeback in {0} years".format(18 - age))
#-----------------------------------------------------------------------------------------------------------------------
#elif is to check multiple conditions
if age < 18:
    print("Pleas comeback in {0} years".format(18 - age))
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an x in the box")

