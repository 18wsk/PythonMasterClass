activities = ("Please Choose your options from the list below:\n1.\tLearn Python\n"
      "2.\tLearn Java\n3.\tGo Swimming\n4.\tHave Dinner\n5.\tGo to bed\n0.\tExit\n")

print(activities)
choice = 1

while choice != 0:
    choice = int(input())
    if choice in range(1, 6):
        print("Your choice was number: {}".format(choice))
    else:
        if choice == 0:
            print("Terminating Game")
            break
        elif choice not in range(1, 6):
            print(activities)
            print("Please guess another value, this time between 1 and 5")



#choice = "-"
# while choice != "0":
#   if choice in "12345":
#        print("Your choice was {}".format(choice))
#   else:
#        print("Please Choose your options from the list below: ")
#        print("1.\tLearn Python")
#        print("2.\tLearn Java")
#        print("3.\tGo Swimming")
#        print("4.\tHave Dinner")
#        print("5.\tGo to bed\n0.")
#   choice = input()
