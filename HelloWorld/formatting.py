for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3)) #exponent oprator is **
print()
#-----------------------------------------------------------------------------------------------------------------------
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3)) #the second value is the field WIDTH

print()
#----------------------------------------------------------------------------------------------------------------------
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3)) #< is to LEFT ALIGN the values
print()
#----------------------------------------------------------------------------------------------------------------------
for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3)) #^ CENTERS the values
print()
#----------------------------------------------------------------------------------------------------------------------
print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7)) #default 7 digits for float
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print()
#precision is set after a decimal point -> 50f is 50 values after decimal
#Precision is priority over WIDTH
#MAX PRECISION IS 51-53 digits -> will be padded with 0's
#----------------------------------------------------------------------------------------------------------------------
#The field number in replacement fields is optional
#cant use values more than once or change the order of what values are used
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
