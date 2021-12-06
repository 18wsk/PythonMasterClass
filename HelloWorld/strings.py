print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We cna even include "quotes" in strings')
print("Hello," + "World!") #concatination
#-----------------------------------------------------------------------------------------------------------------------
greetings = "Hello"
name = "Will"
print(greetings + ' ' + name)
#-----------------------------------------------------------------------------------------------------------------------
name2 = input("Please enter your name: ")
print(greetings + ' ' +name2)
#-----------------------------------------------------------------------------------------------------------------------
#Variables and Types
age = 19
print("Your age is:", age)

print(type(greetings))
print(type(age))

age = "2 years" #rebinding -> we rebounded the label age to the string 2 years -> variable is something bound to a value
print(age)      #even though it works -> not good practice to reuse variables
print(type(age))
#-----------------------------------------------------------------------------------------------------------------------
#ALWAYS THINK OF Binding a variable to a value!
#It is still a strongly typed language -> TYPES STILL HAVE TO MATCH -> WILL RESULT IN TYPE ERROR
print()
#----------------------------------------------------------------------------------------------------------------------
#f-strings
age_in_words = "2 years"
print(name + f" is {age} years old") #just add and f -> then add variable name inside {}
#all formatting for replacement fields work for f-strings

print(f"Pi is approximately {22/7:12.50f}")
#OR
pi  = (22/7)
print((f"Pi is approximately {pi:12.50f}"))
