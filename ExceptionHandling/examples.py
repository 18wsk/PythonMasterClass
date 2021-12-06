def factorial(n):   # Recursive Errors
    if n <= 1:
        return 1
    else:
        # print(n/0)
        return n * factorial(n-1)


# try except blocks prevent errors from crashing programs -> allows for useful testing/debugging as well
try:    # lets you test a block of code for errors
    print(factorial(900))  # if number too large RecursionError: maximum recursion depth exceeded in comparison
except RecursionError:  # lets you handle the errors
    print("This program cannot calculate factorials that large")
except ZeroDivisionError:
    print("No value can be divided by 0")

print("Program Terminating")


