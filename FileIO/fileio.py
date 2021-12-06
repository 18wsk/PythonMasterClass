# jabber = open("sample.txt", 'r')
# # jabber = open("C:\\Users\\Willi\\Desktop\\Python\\Resources\\IO\\sample.txt",'r')
# # open() -> built in function to open a file
# # 'r' -> stands for read only
#
# for line in jabber:
#     if "jabberwock" in line.lower(): #only returns lines with jabbwerwock
#         print(line, end='') # space instead of newline character
#
# jabber.close()
# # .close() -> closes the file
########################################################################
# with open("sample.txt", 'r') as jabber:
# #with open() does not require a close()
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
########################################################################
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline() # reads line by line and returns each as a string
#     while line:
#         print(line, end='')
#         line = jabber.readline()
########################################################################
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines() # reads entire file in one go
print(lines)

for line in lines:
    print(line, end='')
########################################################################
# append causes data to be appended to end of file -> does not overwrite
