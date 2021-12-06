try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter
import math


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


# CHALLENGE
# MODIFY CIRCLE FUNCTION SO THAT IT ALLOWS COLOR = SPECIFIED AND DEFAULTS TO RED. REV PREV LECTURE
def circle(page, radius, g, h):
    user_in = input("Please Select a Color: ")
    if user_in == "":
        user_in = "red"
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=user_in, width=2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g)**2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axis(page):
    page.update()     # TO MAKE SURE WE CAN ACCESS WIDTH AND HEIGHT OF CANVAS
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0, -y_origin, fill='black')
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y+1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)
# circle(canvas, 100, 100, -100)
# circle(canvas, 100, -100, 100)
# circle(canvas, 100, -100, -100)

mainWindow.mainloop()
