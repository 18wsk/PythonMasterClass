import tkinter
# import math


def parabola(page, size):
    for x_parameter in range(-size, size):
        y_parameter = x_parameter * x_parameter / size
        plot(page, x_parameter, y_parameter)

#######################################################################
# Modify the circle function so that it allows the colour of the circle to be specified
# and defaults to red if a colour is not given


def circle(page, radius, g, h, colour="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)

    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)
########################################################################


def draw_axis(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())


def plot(page, x_parameter, y_parameter):
    page.create_line(x_parameter, -y_parameter, x_parameter + 1, -y_parameter + 1, fill='red')


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry('640x480')

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100, 'green')
circle(canvas, 100, -100, 100, 'yellow')


mainWindow.mainloop()
