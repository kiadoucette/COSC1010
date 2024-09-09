#
# Kiara Doucette
# 09/09/2024
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
length_A = 0
width_A = 0
length_B = 0
width_B = 0

# Get length A
length_A = int(input('Enter the length of rectangle A: '))

# Get width A
width_A = int(input("Enter the width of rectangle A: "))

# Get length B
length_B = int(input("Enter the length of rectangle B: "))
# Get width B
width_B = int(input("Enter the width of rectangle B: "))
# Calculate area A
area_A = length_A * width_A
# Calculate area B
area_B = length_B * width_B
# Print area comparison using if-elif-else statements
if area_A > area_B :
    print("Rectangle A has the greater area.")
elif area_B > area_A :
    print("Rectangle B has the greater area")
else:
    print("Both have the same area.")