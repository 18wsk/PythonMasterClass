shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None #none is a constant = NULL

# for index in range(len(shopping_list)): #len() returns the length of the list (or string)
#     if shopping_list[index] == item_to_find: #if item at index # in shopping_list = spam -> then found_at = index
#         found_at = index
#         break #will stop the loop from searching after item is found
#

#this is a more efficient way of writting ^^^^^^^^^^^
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at != None:
    print("The item {0}, was found at index {1}".format(item_to_find, found_at))
else:
    print("{} Not found".format(item_to_find))
