# CHANGE THE CODE TO MAKE IT WORK
# BELOW IS THE COMPLETE PROGRAM FROM THE LAST VID BUT WITH THE LOCATIONS
# DICTIONARY MODIFIED SO THAT EVERYTHING IS IN A SINGLE DICTIONARY
locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {"Q": 0},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4,}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

loc = 1
while True:
    available_exits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are: " + available_exits + "\n").upper()
    print()
    # parse the user input using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter so check vocab
        words = direction.split()  # default split is spaces
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]

    if direction in allExits:
        loc = locations[loc]["exits"][direction]
    else:
        print("You cannot go in that direction")