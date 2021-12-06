# Write a GUI program to create a simple calculator
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
# ########################################################################
import tkinter
# title
mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindowPadding = 8
mainWindow['padx'] = mainWindowPadding
########################################################################
# keypad Frame
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')
#######################################################################
# answer bar
answerbar = tkinter.Entry(keyPad)
answerbar.grid(row=0, column=0, sticky='nsew', columnspan=4)
#######################################################################
# C and CE
cbutton = tkinter.Button(keyPad, text='C')
cebutton = tkinter.Button(keyPad, text='CE')
cbutton.grid(row=1, column=0, sticky="nsew")
cebutton.grid(row=1, column=1, sticky="nsew")

# numbers 0 - 9
button0 = tkinter.Button(keyPad, text='0')
button1 = tkinter.Button(keyPad, text='1')
button2 = tkinter.Button(keyPad, text='2')
button3 = tkinter.Button(keyPad, text='3')
button4 = tkinter.Button(keyPad, text='4')
button5 = tkinter.Button(keyPad, text='5')
button6 = tkinter.Button(keyPad, text='6')
button7 = tkinter.Button(keyPad, text='7')
button8 = tkinter.Button(keyPad, text='8')
button9 = tkinter.Button(keyPad, text='9')
button0.grid(row=5, column=0, sticky='nsew')
button1.grid(row=4, column=0, sticky='nsew')
button2.grid(row=4, column=1, sticky='nsew')
button3.grid(row=4, column=2, sticky='nsew')
button4.grid(row=3, column=0, sticky='nsew')
button5.grid(row=3, column=1, sticky='nsew')
button6.grid(row=3, column=2, sticky='nsew')
button7.grid(row=2, column=0, sticky='nsew')
button8.grid(row=2, column=1, sticky='nsew')
button9.grid(row=2, column=2, sticky='nsew')

# Extras
equalButton = tkinter.Button(keyPad, text='=')
slashButton = tkinter.Button(keyPad, text='/')
addButton = tkinter.Button(keyPad, text='+')
mulButton = tkinter.Button(keyPad, text='*')
subButton = tkinter.Button(keyPad, text='-')
equalButton.grid(row=5, column=1, sticky='nsew',  columnspan=2)
slashButton.grid(row=5, column=3)
addButton.grid(row=2, column=3)
mulButton.grid(row=4, column=3)
subButton.grid(row=3, column=3)


mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, answerbar.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + 50 + mainWindowPadding, answerbar.winfo_height() + 50 + keyPad.winfo_height())
mainWindow.mainloop()
