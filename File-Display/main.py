#
# Kiara Doucette
# 10/21/2024
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Declaring String Variable For File
myFile = ' '
# Open the file.
myFile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myFile:
    number = int(line)
    print(number)

# Close the file.
myFile.close()