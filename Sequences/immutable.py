# result = True
# another_result = result
#
# print(id(result))
# print(id(another_result))
# #id function returns identity (unique integer) of an object
#
# result = False
# print(id(result))
# #bools are immutable id of true cannot be changed
# #python has now bound result to a new value false

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
#result has now a different id because you cannot change the string