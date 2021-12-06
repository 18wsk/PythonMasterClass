#Example            1
#index    01234567890123...
parrot = "Norwegian Blue"
print(parrot)

print(parrot[3]) #letter at index 3 (w)
#----------------------------------------------------------------------------------------------------------------------
#Mini Challenge-------
#Challenge is to print "we win" all using the index of the string that parrot is bound to
print(parrot[4])
print(parrot[9]) #SPACES COUNT AS CHARACTERS A PART OF INDEXES
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
#----------------------------------------------------------------------------------------------------------------------
#Negative Indexing -> STARTS AT -1 NOT 0
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6]) #we win
#----------------------------------------------------------------------------------------------------------------------
#SLICING (start/stop/stip)
print(parrot[0:6]) #Norweg -> Start at 0 and slice up to NOT including index 6
print(parrot[3:5]) #we

print(parrot[0:9]) #Norwegian
print(parrot[:9]) #NO START/END VALUE NEEDED IF START @ 0 OR END AT LAST

#Mini Challenge --------
print(parrot[10:14]) #Blue
print(parrot[10:])  #Blue

print(parrot[:6] + parrot[6:]) #Norwegian Blue
print(parrot[:]) #PRINTS THE WHOLE STRING
#----------------------------------------------------------------------------------------------------------------------
#NEGATIVE INDEXING
print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl

print(parrot[:-5]) #Norweigen
print(parrot[-4:]) #Blue
print(parrot[:-8]) #Norweg
#----------------------------------------------------------------------------------------------------------------------
#Using A STEP IN A SLICE
print(parrot[0:6:2]) #Nre --> starts @0 extends up to not including 6 -> step through the sequence in steps of 2
print(parrot[0:6:3]) #Nw

number = "9,223;372:036 854,775;807"
print(number[1::4]) #,;: ,;
separators = number[1::4]
print(separators) #,;: ,;

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])





