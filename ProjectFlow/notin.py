activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): #casefold functions converts string to lowercase when comparing strings
    print("But I want to go to the Movies")
else:
    print("So what movie are we seeing then")

#Other String Methods
# .capitalize()
# .casefold()
# .center(width[, fillchar])
# .count(sub[, start, [end]])