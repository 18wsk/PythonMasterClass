shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

print()

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list)) #the id remains unchanged
#new item added to end of list without making a new list

print(another_list)
#it is updated with cookie as well
#another_list and shopping_list are both bound to the same object
#that object now has cookies in it -> so it will be updated


a = b = c = d = another_list
#there are now 6 references to the SAME list
#did not change the list -> just bounded more names to it

print(a)
print("Adding cream")
b.append("cream") #.append() method adds an item to end of a list
print(c)
print(d)
