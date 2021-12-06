string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " "probably " "pining " "for the " "fjords")
#----------------------------------------------------------------------------------------------------------------------
print("Hello " * 5) #will pring the string 5 times

print("Hello " * (5 + 4)) #BEDMAS applies -> 9
print("Hello " * 5 + "4")
#----------------------------------------------------------------------------------------------------------------------
#Checking is something is a sub string -> return Boolean T/F
today = "Friday"
print("day" in today) #True
print("Fri" in today) #True
print("Will" in today) #False
print("parrot" in "fjord") #False