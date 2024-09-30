#
# Kiara Doucette
# 09/30/2024
# Kilometer Converter Programming Project
# COSC 1010
#
# Write a program that asks the user to enter a distance in
# kilometers, then converts that distance to miles. The
# conversion formula is as follows: *Miles = Kilometers x 0.6214*

# Declaring Variables
kilometers = 0
miles = 0
conversion = 0.6214

# Creating Main Function
def main():
    # Getting The Distace From User In Kilometers.
    kilometers = float(input("Enter a distance in kilometers: "))

    # Displaying Conversion To Miles
    show_miles(kilometers)

# Creating A Conversion Method
def show_miles(km):
    # Calculating Miles
    miles = km * conversion

    # Displaying Miles.
    print(km, "Kilometers Equals","%.2f" % miles, "Miles.")

# Calling Main Funtion
main()
