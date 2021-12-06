
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Weird")

# If the python interpreter is running that module (the source file) as the main
# program, it sets the special __name__ variable to have a value “__main__”.
# If this file is being imported from another module, __name__ will be set to the
# module’s name. Module’s name is available as value to __name__ global variable.
