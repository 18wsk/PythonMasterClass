# pickle items all have to be loaded back in memory
# if dealing with large objects - > loading is not an option
# shelve module -> provides a shelve (dictionary) -> stored in a file rather than memory
# like a dictionary the shelve holds key value pairs that can be pickled (really anything)
# Shelve keys are ONLY STRINGS -> items can be whatever
import shelve

# with shelve.open("ShelfTest") as fruit:
fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# print("+" * 40)
# fruit["lime"] = "great with tequila"  # adding an item to shelve
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
########################################################################
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We do not have a " + dict_key)
########################################################################
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print((f + " - " + fruit[f]))
########################################################################
for v in fruit.values():
    print(v)
print(fruit.values())

print()

for f in fruit.items():
    print(f)
print(fruit.items())
########################################################################
fruit.close()


