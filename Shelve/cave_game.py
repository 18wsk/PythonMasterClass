import shelve

locations = shelve.open('locations')
vocabulary = shelve.open('vocabulary')

loc = '1'
while True:
    available_exits = ", ".join(locations[loc][loc["exits"]].keys())

    print(locations[loc]["desc"])

    if loc == '0':
        break
    else:
        allExits = locations[loc][loc["exits"]].copy()
        allExits.update(locations[loc][loc["namedExits"]])

    direction = input("Available exits are: " + available_exits + "\n").upper()
    print()
    # parse the user input using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter so check vocab
        words = direction.split()  # default split is spaces
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]

    if direction in allExits:
        loc = locations[loc][loc["exits"]][direction]
    else:
        print("You cannot go in that direction")

vocabulary.close()
locations.close()
