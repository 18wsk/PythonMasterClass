shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"] #list has square brackets ***

# for item in shopping_list:
#     if item != "spam" : #excluding spam form the output
#         print("Buy "+ item)

#SAME AS ^^
for item in shopping_list:
    if item == "spam": #spam excluded again
        continue #continue causes all the remaining code in the block to be skipped -> right back to for loop

    print("Buy " + item)
print("*" * 80)

for item in shopping_list:
    if item == "spam":
        break #once spam is hit the loop is terminated
    print("Buy " + item)