#
# Kiara Doucette
# 09/30/2024
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# One foot equals 12 inches. Write a funtion named feet_to_inches
# that accepts a number of feet as an argument and returns the 
# number of inches in that many feet. Use the function in a
# program that prompts the user to enter a number of feet then
# displays the number of inches in that many feet.

# Declaring Variables
inches_per_foot = 12
feet = 0

# Declaring Main Function
def main():
    # Get Input Of Feet From The User.
    feet = int(input("Enter A Number Of Feet: "))

    # Printing Statement That Converts Feet To Inches
    print(feet, "Equals", feet_to_inches(feet), "Inches.")

# Declaring Conversion Function
def feet_to_inches(feet):
    # Equation To Return Inches Per Foot
    return feet * inches_per_foot

# Call To The Main Function
main()
