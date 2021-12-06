#Python 2 formatting operator is % followed by letter by how formatting should work
age = 19
print("My age is %d years" % age)
# %d = int
# %f = float
# %s string

major = "Years"
minor = "Months"

print("My age is %d %s, %d %s" %(age, major, 6, minor))
print("Pi is approximately %f" %(22/7))

print("PI is approximately %60.50f" %(22/7))