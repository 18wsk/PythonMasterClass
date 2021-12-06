import shelve
# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
########################################################################
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
    # the shelf has no way to know these lists have changed

    # temp_list = recipes["blt"]
    # temp_list.append("butter") # THIS IS THE CORRECT WAY OF ^
    # recipes["blt"] = temp_list
    #
    # temp_lis = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
########################################################################
    recipes["soup"].append("croutons")  # using writeback = True
    # The writeback flag causes the shelf to remember all of the objects
    # retrieved from the database using an in-memory cache.
    # Each cache object is also written back to the database when the
    # shelf is closed

    for snack in recipes:
        print(snack, recipes[snack])
