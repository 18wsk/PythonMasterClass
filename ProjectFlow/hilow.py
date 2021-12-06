low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to Start: ")

guesses = 1

while low != high:  # True is always true so this loop will run forever
    #print("\t Guessing in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2  # calculating midpoint
    high_low = input("My Guess is {}. Should I guess Higher or Lower?"
                     " Enter h or l or c if my guess is correct: "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess Higher -> The low end of the range becomes 1 greater than the guess
        low = guess + 1

    elif high_low == "l":
        # Guess Lower -> High end of the range will be 1 less than the guess
        high = guess - 1

    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break #break out of while loop if guessed correctly -> skips else

    else:
        print("Please Enter h, l or c")

    guesses += 1  # guesses = guesses + 1

else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))
