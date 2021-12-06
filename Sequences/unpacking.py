a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76 #data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a List")
data_list = [12, 13, 14]
x, y, z = data_list
print(x)
print(y)
print(z)
# However if a list changes cuz it is mutable
# Then you try to unpack == code crash