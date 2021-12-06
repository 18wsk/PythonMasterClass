numbers = [1, 45, 31, 60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine") #associated with the for loop

#we do not want the code to execute if we break out of the loop, only
#when it goes all the way around