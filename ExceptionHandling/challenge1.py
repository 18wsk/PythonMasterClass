import sys


def getint():
    while True:
        try:
            number = int(input("Please Enter a number: "))
            return number
        except EOFError:
            sys.exit(1)
        except ValueError:
            print("Invalid number entered, please try again")
        finally:
            print("The Finally Clause Always Executes")


x = getint()
y = getint()
try:
    print("{} divided by {} = {}".format(x, y, x/y))
except ZeroDivisionError:
    print("Cannot Divide by 0")
    sys.exit(2)
else:
    print("Division Performed Successfuly")

# def divide(a, b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Cannot Divide by 0")
#         sys.exit(2)
#     finally:
#         print("Division Performed Successfuly")
#
#
# print(divide(x, y))
