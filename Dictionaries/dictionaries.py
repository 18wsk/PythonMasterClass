#an unordered list not accessed by index but by a key

fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",}

# del fruit["lemon"]
# print(fruit)
# #del is used to delete items out of a dictionary
#
# fruit.clear()
# print(fruit)
# #.clear() is used to clear the entire dictionary
# #the issue is if keys are entered that do not exist they will crash the code

# print(fruit)
# while True:
#     dict_key = input("Please Enter a Fruit: ")
#     if dict_key.casefold() == "quit":
#         break
#     description = fruit.get(dict_key, "We do not have a " + dict_key)
#     #.get() method returns the value of the item with the specific key
#     #will default to "we dont have a..." if key doesnt exist
#     #will print description if it does

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
# #sorting it in alphabetical order
#
# for key in fruit:
#     print(fruit[key])
# print("*" * 40)
#
#
# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "Not nice with ice cream"
# print(fruit_keys)


print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)
print()

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
#creating tuple from dict

print()

print(dict(f_tuple))
#making a dict from a tuple