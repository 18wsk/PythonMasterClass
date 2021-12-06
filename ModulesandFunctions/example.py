# print(dir())
# # anything who's name starts with "_" should not be changed unless for good reason
# # "__" are not intended to be changed at all
# # Python does not have any private variables
# # "_" signifies a variable private to that module
#
# for m in dir(__builtins__):
#     print(m)
# # dir() is a powerful inbuilt function in Python3,
# # which returns list of the attributes and methods of any object
########################################################################
# import shelve
#
# print(dir())
# print()
# print(dir(shelve))
#######################################################################
# import shelve
#
# for obj in dir(shelve.Shelf):
#     if obj[0] != '_':
#         print(obj)
#######################################################################
import random

help(random.randint)
# Python help() function is used to get the documentation of specified
# module, class, function, variables etc.
