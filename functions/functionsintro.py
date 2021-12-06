# Functions in Python are made with the keyword def *functionName*()
# parameter -> variables defined in function definition
# argument -> actual values used when function called
def python_food():
    width = 80
    text = 'spam and eggs'
    left_margin = (width-len(text)) // 2
    print(" " * left_margin, text)
    return 1


# call the function here
python_food()
# all python functions return a result
print("Print(python_food()) returns {}".format(python_food()))
# if one arguments is a function call -> will print contents and return result -> default return = NONE
print()
########################################################################


# * signifies there is a variable number of parameters
def centre_text(*args, sep=' ', end_char='\n', centered_file=None, flush_me=False):
    text = ""   # making an empty string
    for arg in args:    # iterating through args
        text += str(arg) + sep      # concatenate each entry to end of string
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


with open("menu", mode="w") as menu_file:
    s1 = centre_text("spam, spam, spam and eggs")
    print(s1, file=menu_file)
    s2 = centre_text(12)
    print(s2, file=menu_file)
    s3 = centre_text("first", "second", 3, 4, "spam", sep=":")
    print(s3, file=menu_file)

