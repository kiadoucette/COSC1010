#
# Kiara Doucette
# 09/20/2024
# Bug Collector Programming Project
# COSC 1010
#

# Initialize variables for bugs and total number of bugs collected.
total = 0
bugs = 0

# Get number of bugs collected each day using a for loop.
for day in range(1,8):
    print("Enter The Bugs Collected Each Day:", day)
    bugs = int(input())
    total += bugs
    
# Display the total number of bugs collected.
print("You Collected A Total Of", total, "Bugs.")
