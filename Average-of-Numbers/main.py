#
# Kiara Doucette
# 10/21/2024
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Assume a file containing a series of integers is
# named 'numbers.txt' and exists on the computer's
# disk. Write a program that calculates the average 
# of all the numbers stored in the file

# Declaring Variables
myFile = ' '
addingAllNumbers = 0
number = 0
count = 0

# Opening The File
myFile = open('numbers.txt', 'r')

# Read and Calculate The File's Content
for line in myFile:
    number = int(line)
    count = count + 1
    addingAllNumbers = addingAllNumbers + number

# Closing File
myFile.close()

# Grabbing Average of All File's Content Number's Added
average = addingAllNumbers / count
# Printing Results 
print("The Average of All Numbers on File: ", average)