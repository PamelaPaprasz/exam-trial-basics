def count_as(my_file):
    try:
        my_file = open(my_file, 'r')
        
        number_of_a = 0
        
        for i in my_file:
            if i == 'a':
                number_of_a += 1
        return number_of_a
        my_file.close()
        
    except FileNotFoundError:
        return 0

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0


# Create a function that takes a filename as string parameter,
# counts the occurances of the letter "a", and returns it as a number.
# If the file does not exist, the function should return 0 and not break.
