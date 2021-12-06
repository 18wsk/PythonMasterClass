panagram = """The quick brown 
fox jumps\tover the lazy dog"""

words = panagram.split()
print(words)
# split method splits a string up into words
# did not define any arguments to split
# defaults to white space -> tabs, spaces

numbers = "9,223,372,036,854, 775,807"
print(numbers.split(","))
# defining the argument of where to split
print()

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)
# Join lets you create a string from a sequence such as a list

values_list = values.split()
print(values_list)
# the split will the string up and put them into a list of strings

final_list = "".join(generated_list).split()
print(final_list)
# they can be combined to 1 line


# Use a for loop to produce a list of ints, rather than strings.


# create a new list of ints
integer_values = []
for item in values_list:
    integer_values.append(int(item))

print(integer_values)

# or you can modify the components of the 'values_list' list in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)
# range will go 0-6 -> length is 7 but that isnt included in list
