availible_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in availible_exits: #will keep prompting until a exit in the list is written
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":  #removes case distinction
        print("Game Over")
        break
else: #prevents from message printing when breaking out of loop
    print("aren't you glad you got out of there")