#
# Kiara Doucette
# 10/28/2024
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
# Modify the program that you wrote for 'Average of Numbers'
# so it handles the following exceptions:
# - It should handle any 'IOError' exceptions that are raised
# when the file is opened and data is read from it.
# 
# - It should handle any 'ValueError' exceptions that are
# raised when the items that are read from the file are
# converted to a number. 


# Declaring Variables
myFile = ' '
addingAllNumbers = 0
number = 0
count = 0

# Checking for IOError
try: 

    with open('numbers.txt', 'r') as myFile:

        # Read and Calculate The File's Content
     for line in myFile:
        # Checking For ValueError
        try:
            number = int(line)
            count = count + 1
            addingAllNumbers = addingAllNumbers + number
        except ValueError:
            print(f"Warning: ", line, " is not a valid number and will be skipped")

        if count > 0:
            # Grabbing Average of All File's Content Number's Added
            average = addingAllNumbers / count
            # Printing Results 
            print("The Average of All Numbers on File: ", average)
        else:
            print("No valid numbers found in the file.")
except IOError:
    print(f"Error: The file " , myFile.name, "could not be opened or read.")