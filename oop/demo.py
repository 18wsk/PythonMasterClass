a_string = "this is \na string split\t\tand tabbed"
print(a_string)

raw_string = r"this is \na string split\t\tand tabbed"
print(raw_string)
# raw string ignores the special characters

b_string = "this is " + chr(13) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "this is a backslash \followed by some text"
print(backslash_string)
backslash2_string = "this is a backslash \\followed by some text"
print(backslash2_string)

error_string = r"this string ends with \\"
