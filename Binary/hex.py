# for i in range(17):
#     print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x*y)
#
# print(0b101010)

#When converting a decimal number to binary, you look for the highest powe
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power -putting a 1
# if it goes into the remainder and a zero other wise. keep repeating until you
# have dealt with all powers down to 2 ** 0 (ie - 1)

#write a progeam that request a number from the keyboard, then prints out
#its binary representation

#the porblem should cater for numbers up to 65535; ie - (2**16)-1

powers = []
for power in range(15, -1, -1):
    powers.append(2**power)
print(powers)

user_in = int(input("Please Enter A Number: "))

printing = False
for power in powers:
    bit = user_in//power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(user_in//power, end='')
    user_in %= power
