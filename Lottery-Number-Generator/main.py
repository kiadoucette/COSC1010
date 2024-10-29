#
# Kiara Doucette
# 10/28/2024
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Importing Random 
import random
# Declaring Variables
MAX_DIGITS = 7
START = 0
END = 9

# Main Function
def main():
    # Create A List
    numbers = [0] * 7

    # Populating The List With Random Numbers
    for index in range(MAX_DIGITS):
        # Creating List
        numbers[index] = random.randint(START, END)
    
    # Displaying The Random Numbers
    print("Here are your lottery numbers: ")
    # Checks For Range
    for index in range(MAX_DIGITS):
        # Prints The Lottery Number
        print(numbers[index], end = '')
        print()

main()