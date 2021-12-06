import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    for key in bike:
        print(key)
    print("+" * 40)

    # del bike['engin_size']

    # if key is mispelled then corrected -> there will be 2 keys
    # shelves are persistant to a file

    print(bike["engine_size"])
    print(bike["colour"])
