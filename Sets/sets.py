# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
# # first way to define a set is like a dictionary but contains no keys
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
# #
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
# # second way is to use the set([])
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
# # this adds item to sets -> but sets are printed out in random order
#
# empty_set = set()
# empty_set.add("a")
# print(empty_set)
#
# even = set(range(0, 42, 2))
# print(even)
#
# squares_tuple = (4, 6, 9, 16, 2)
# squares = set(squares_tuple)
# print(squares)
########################################################################
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
# # union() returns a set that contains all items from both sets -> except duplicates
#
# print("*" * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
# # intersection() -> returns duplicates between sets
#######################################################################
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(even - squares)
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(squares - even)
# # The difference() method in Python returns the difference between two given sets
# #######################################################################
# print("=" *40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
# # the difference() method returns a new set, without the unwanted items,
# # and the difference_update() method removes the unwanted items from the original set.
#########################################################################
# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
#
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
#symmetric_difference() method returns the symmetric difference of two sets.
# The symmetric difference of two sets A and B is the set of elements that
# are in either A or B , but not in their intersection.
########################################################################
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# squares.discard(4)
# squares.discard(16)
# squares.discard(8) #does not return an error even if item not there
# print(squares)
#squares.remove(8) -> would return an error since 8 doesnt exist in that set
# if 8 in squares:
#     squares.remove(8)
# print(squares)
#
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")
#######################################################################
even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)
if squares.issubset(even):
    print("Squares is a subset of even")
if even.issuperset(squares):
    print("Even is a superset of squares")
#######################################################################
# frozen set is an immutable set -> cant be changed
# can be used as a dictionary key
# can also add a frozen set as a member as a set -> no add/remove/discard

even = frozenset(range(0, 100, 2))
print(even)

