import tkinter
from tkinter import messagebox

mainWindow = tkinter.Tk()
mainWindow.title("Fraction Calculator (18wsk 20120570)")
mainWindow.geometry('640x480-8-200')
mainWindowPadding = 8
mainWindow['padx'] = mainWindowPadding
mainWindow['pady'] = mainWindowPadding


def display_add():
    global operator_value
    operator_value.set("+")


def display_subtract():
    global operator_value
    operator_value.set("-")


def display_multiply():
    global operator_value
    operator_value.set("x")


def display_divide():
    global operator_value
    operator_value.set("÷")


def clear_calculator():
    global operator_value
    global numerator_one
    global numerator_two
    global denominator_one
    global denominator_two
    global answer_label

    numerator_one.delete(0, 'end')
    numerator_two.delete(0, 'end')
    denominator_one.delete(0, 'end')
    denominator_two.delete(0, 'end')
    answer_value.set("")
    operator_value.set("")


def close_gui():
    mainWindow.destroy()


def equal_operation():
    global operator_value
    global numerator_one
    global numerator_two
    global denominator_one
    global denominator_two

    global answer_label
    global answer_value
    # global variables have now be initialized. Now local variables must be initialized before they are referenced
    denom2 = 0
    num1 = 0
    num2 = 0
    denom1 = 0
    # str_foo will hold the user input and will be evaluated for errors before being converted to int, calculated result
    # based on operator then return solution as a string
    str_num1 = numerator_one.get()
    str_num2 = numerator_two.get()
    str_denom1 = denominator_one.get()
    str_denom2 = denominator_two.get()
    acceptable_vals = '1234567890-'
    error_count = 0
#######################################################################################################################
    # checking to ensure that inputs are not blank, not characters and denominators are not 0
    if numerator_one.get() == '' or numerator_two.get() == '' or denominator_one.get() == '' \
            or denominator_two.get() == '':
        messagebox.showwarning("Missing Field", "Please fill out all fields before performing mathematical operation")
    if str_denom1 == '0' or str_denom2 == '0' or str_denom1 == '-0' or str_denom2 == '-0':
        messagebox.showwarning("Undefined Reference", "Please ensure denominator is not 0")
#######################################################################################################################
    # Checking that all characters are valid and that if there is a negative sign its only in first character space
    for i in str_num1:
        if i not in acceptable_vals or i == '-' and str_num1[0] != i:
            error_count += 1
    for i in str_num2:
        if i not in acceptable_vals or i == '-' and str_num2[0] != i:
            error_count += 1
    for i in str_denom1:
        if i not in acceptable_vals or i == '-' and str_denom1[0] != i:
            error_count += 1
    for index, value in enumerate(str_denom2):
        if value not in acceptable_vals or value == '-' and str_denom2[0] != value:
            error_count += 1
    if error_count > 0:
        messagebox.showwarning("Unrecognized Number", "Please ensure only numbers and inputted")

#######################################################################################################################
    # Embedded gcd function used to simplify fractions

    def gcd(n, d):
        if d == 0:
            return n
        else:
            return gcd(d, n % d)

######################################################################################################################
    # error checking for input of size 1 ... making sure "-" is not valid
    len_error_count = 0
    if len(str_num1) == 1:
        if str_num1.isdigit():
            num1 = int(str_num1)
        else:
            len_error_count += 1
    if len(str_num2) == 1:
        if str_num2.isdigit():
            num2 = int(str_num2)
        else:
            len_error_count += 1
    if len(str_denom1) == 1:
        if str_denom1.isdigit():
            denom1 = int(str_denom1)
        else:
            len_error_count += 1
    if len(str_denom2) == 1:
        if str_denom2.isdigit():
            denom2 = int(str_denom2)
        else:
            len_error_count += 1
    if len_error_count > 0:
        messagebox.showwarning("Unrecognized Number", "Please ensure only numbers and inputted")
#######################################################################################################################
    # this block ensures that if the user inputs "-" as first character and the rest of char are digits that it will be
    # assigned as a negative number
    if str_num1[0] == "-":
        num1 = (-1) * int(str_num1[1:])
    elif str_num1[0].isdigit():
        num1 = int(str_num1)

    if str_denom1[0] == "-":
        denom1 = (-1) * int(str_denom1[1:])
    elif str_denom1[0].isdigit():
        denom1 = int(str_denom1)

    if str_num2[0] == "-":
        num2 = (-1) * int(str_num2[1:])
    elif str_num2[0].isdigit():
        num2 = int(str_num2)

    if str_denom2[0] == "-":
        denom2 = (-1) * int(str_denom2[1:])
    elif str_denom2[0].isdigit():
        denom2 = int(str_denom2)
#######################################################################################################################
    # Now that all error conditions are accounted for we will check operators and perform arithmetic where necessary
    operator = operator_value.get()
    if operator == '':
        messagebox.showwarning("No Operator", "Please select an operator before trying to solve problem")
    elif operator == '+':
        answer_num = ((num1 * denom2) + (num2 * denom1))
        answer_denom = (denom1 * denom2)
        simplified_answer_num = int(answer_num / gcd(answer_num, answer_denom))
        simplified_answer_denom = int(answer_denom / gcd(answer_num, answer_denom))
        if simplified_answer_denom == 1.0 or simplified_answer_denom == 1:
            answer_value.set(str(simplified_answer_num))
        else:
            answer_value.set(str(simplified_answer_num) + "/" + str(simplified_answer_denom))
    elif operator == '-':
        answer_num = ((num1 * denom2) - (num2 * denom1))
        answer_denom = (denom1 * denom2)
        simplified_answer_num = int(answer_num / gcd(answer_num, answer_denom))
        simplified_answer_denom = int(answer_denom / gcd(answer_num, answer_denom))
        if simplified_answer_denom == 1.0 or simplified_answer_denom == 1:
            answer_value.set(str(simplified_answer_num))
        else:
            answer_value.set(str(simplified_answer_num) + "/" + str(simplified_answer_denom))
    elif operator == 'x':
        answer_num = (num1 * num2)
        answer_denom = (denom1 * denom2)
        simplified_answer_num = int(answer_num / gcd(answer_num, answer_denom))
        simplified_answer_denom = int(answer_denom / gcd(answer_num, answer_denom))
        if simplified_answer_denom == 1.0 or simplified_answer_denom == 1:
            answer_value.set(str(simplified_answer_num))
        else:
            answer_value.set(str(simplified_answer_num) + "/" + str(simplified_answer_denom))
    elif operator == '÷':
        answer_num = (num1 * denom2)
        answer_denom = (num2 * denom1)
        simplified_answer_num = int(answer_num / gcd(answer_num, answer_denom))
        simplified_answer_denom = int(answer_denom / gcd(answer_num, answer_denom))
        if simplified_answer_denom == 1.0 or simplified_answer_denom == 1:
            answer_value.set(str(simplified_answer_num))
        else:
            answer_value.set(str(simplified_answer_num) + "/" + str(simplified_answer_denom))
#######################################################################################################################
    # Bug fix for undefined input returning error but also 1/0 in output box
    if answer_value.get() == "1/0":
        answer_value.set("")
        messagebox.showwarning("Undefined Reference", "Please ensure denominator is not 0")


#######################################################################################################################
answer_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1)
answer_frame.grid(row=0, column=0, sticky='nsew', ipadx=70)

numerator_one = tkinter.Entry(answer_frame, borderwidth=1, background='white')
numerator_one.grid(row=0, column=0)
denominator_one = tkinter.Entry(answer_frame, borderwidth=1, background='white')
denominator_one.grid(row=1, column=0)

operator_value = tkinter.StringVar()
operator_label = tkinter.Label(answer_frame, textvariable=operator_value)
operator_label.grid(row=0, column=3, rowspan=2)

numerator_two = tkinter.Entry(answer_frame, borderwidth=1, background='white')
numerator_two.grid(row=0, column=4)
denominator_two = tkinter.Entry(answer_frame, borderwidth=1, background='white')
denominator_two.grid(row=1, column=4)

equal_sign_label = tkinter.Label(answer_frame, text="=")
equal_sign_label.grid(row=0, column=6, rowspan=2)

answer_value = tkinter.StringVar()
answer_label = tkinter.Label(answer_frame, textvariable=answer_value, borderwidth=1)
answer_label.grid(row=0, column=7, columnspan=4, rowspan=2)

########################################################################################################################
keypad_frame = tkinter.Frame(mainWindow, borderwidth=2)
keypad_frame.grid(row=2, column=0, sticky='nsew', columnspan=16)

c_button = tkinter.Button(keypad_frame, borderwidth=1, text="C", command=clear_calculator)
c_button.grid(row=0, column=0, sticky="ew", columnspan=8)

close_button = tkinter.Button(keypad_frame, borderwidth=1, text="Close", command=close_gui)
close_button.grid(row=0, column=9, sticky="ew", columnspan=8)

add_button = tkinter.Button(keypad_frame, borderwidth=1, text="+", command=display_add)
add_button.grid(row=1, column=0, sticky="ew", columnspan=8)

subtract_button = tkinter.Button(keypad_frame, borderwidth=1, text="-", command=display_subtract)
subtract_button.grid(row=1, column=9, sticky="ew", columnspan=8)

multiply_button = tkinter.Button(keypad_frame, borderwidth=1, text="x", command=display_multiply)
multiply_button.grid(row=1, column=18, sticky="ew", columnspan=8)

divide_button = tkinter.Button(keypad_frame, borderwidth=1, text="÷", command=display_divide)
divide_button.grid(row=1, column=28, sticky="ew", columnspan=8)

equal_button = tkinter.Button(keypad_frame, borderwidth=1, text="=", command=equal_operation)
equal_button.grid(row=2, column=0, sticky="ew", columnspan=128)

mainWindow.update()
mainWindow.minsize(keypad_frame.winfo_width() + 50 + mainWindowPadding,
                   answer_frame.winfo_height() + 50 + keypad_frame.winfo_height())
mainWindow.maxsize(keypad_frame.winfo_width() + 100 + mainWindowPadding,
                   answer_frame.winfo_height() + 100 + keypad_frame.winfo_height())
mainWindow.mainloop()
