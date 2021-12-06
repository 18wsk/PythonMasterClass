import random #importing the built in random number generator that comes with python

highest = 10
lowest = 1
answer = random.randint(lowest, highest)  #answer will be a random integer between 1-10 -> using dot notation
print(answer) #TODO: remove after testing

print("Please Guess a number between {0} and {1}: ".format(lowest, highest))
guess = int(input()) #convert their input into an integer

if guess == answer:
    print("Well done you got it first try")
else:
    if guess > answer:
        print("Please Guess Lower")
    else:
        print("Please Guess Higher")
    guess = int(input())
    if guess == answer:
        print("You Finally Guessed it right")
    else:
     print("You Guessed Incorrectly again - Game over")
