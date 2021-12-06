letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards) #backwards NOT including a

realBackwards = letters[::-1] #having ::1 is an idium -> reversing a sequence
print(realBackwards) #zyxwvutsrqponmlkjihgfedcba !!!!!!!!!!!!!!
#make sure stop value is greater than start value
#----------------------------------------------------------------------------------------------------------------------
#Challenge

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

#last 8 characters reordered
reorder = letters[:17:-1]
print(reorder)
#-----------------------------------------------------------------------------------------------------------------------
print(letters[-1:]) #z
print(letters[:1]) #is better than letters[0] because if letters is empty index is OUT OF RANGE