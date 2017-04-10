def count_as(my_file):
    try:
        my_file = open(my_file, 'r')
        data = my_file.readline()
        data= data.lower()
        my_file.close()
        
        return data.count('a')
        
    except FileNotFoundError:
        return 0

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0


# Create a function that takes a filename as string parameter,
# counts the occurances of the letter "a", and returns it as a number.
# If the file does not exist, the function should return 0 and not break.
