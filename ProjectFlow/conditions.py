age = int(input("How old are you?: "))

# if age >=16 and age <= 65: IS NOT AS EFFIECIENT
#...
# if 16 <= age <= 65:
#     print("Have a good day at work")
# else:
#     print("Enjoy your free time")
# print("-" * 80)
#
# if age < 16 or age > 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#-----------------------------------------------------------------------
#same conditions with ranges tho
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")
print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")