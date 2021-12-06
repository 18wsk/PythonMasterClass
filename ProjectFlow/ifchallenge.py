name = input("What is your name? ")
age = int(input("How old are you {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the Holiday {0} ".format(name))
else:
    print("Sorry {0}, the only ages allowed are 18-30 ".format(name))