a = 12
b = 3

print(a+b)  #15
print(a-b)  #9
print(a*b)  #36
print(a/b)  #4.0
print(a//b) #4 integer division: rounded down towards minus infinity
print (a%b) #0 modulo: the remainder after integer division
#----------------------------------------------------------------------------------------------------------------------
print()
for i in range(1, 4): #both range types must be int in this case
    print(i)
#OR
print()
for i in range(1, a//b): #integer division required ----> range(#,#),1, and a//b and print(i) are all expressions
    print(i)
#----------------------------------------------------------------------------------------------------------------------
#Expression Proof
print()
i = 1 #showing how i on line 16 is not an expression
print(i)
i = 2
print(i)
i = 3
print(i)
#----------------------------------------------------------------------------------------------------------------------
#Operator Precendence BEDMAS
print(a+b/3 - 4 * 12)
print(a+(b/3)-(4*12))
#VS
print((((a+b)/3)-4)*12)
print(((a+b)/3-4)*12)
#VS
c = a + b
d = c/3
e = d-4
print(e*12)
print()

print(a/(b*a)/b) #1/9 = 0.1111111..