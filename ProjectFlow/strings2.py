number = input("Please enter a series of numbers, using any seperators you would like: ")
separators = "" #separators must be bound to empty string -> to give it a current value to add to

for char in number:
    if not char.isnumeric(): #returns true if all characters in a string are numeric
        separators = separators + char

#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values])) #Now calculates the sum of the numbers -> without caring about their separators