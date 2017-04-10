def seconds(change_this):
    
    change_this = change_this[1:]
    change_this = change_this[::2]
    return change_this
    
print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]

    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

