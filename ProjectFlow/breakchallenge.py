# # Modify the code inside this loop to stop when i is exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     x = i %11
#     if x == 0 and i > 0:
#         break

# #SAME AS ABOVE
# for i in range(0, 100, 7):
#     print(i)
#     if i % 11 == 0 and i > 0:
#         break
#---------------------------------------------------------------------------------------------------------------------
# for i in range (21):
#     if i%3 == 0 or i%5==0:
#         continue
#     else:
#         print(i)

#should be
for i in range(21):
    if i%3 == 0 or i%5 == 0:
        continue #ignores code below if true
    print(i)