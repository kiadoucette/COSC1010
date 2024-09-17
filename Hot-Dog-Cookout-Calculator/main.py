#
# Kiara Doucette
# 09/09/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
# Write a program that calculates the number of packages of hot dogs 
# and the number of packages of hot dog buns needed for a cookout, 
# with the minimum amount of leftovers. 


# The program should ask the user for the number of people 
# attending the cookout and the number of hot dogs each 
# person will be given. The program should display the following details:

# - The minimum number of packages of hot dogs required
# - The minimum number of packages of hot dog buns required
# - The number of hot dogs that will be left over
# - The number of hot dog buns that will be left over

# Declaring Variables
hot_Dogs = 10
hot_Dog_Buns = 8
number_Of_People = 0
hot_Dogs_Leftover = 0
hot_Dog_Buns_Leftover = 0
total_Hot_Dogs_Needed = 0
total_Hot_Dog_Buns_Needed = 0
hot_Dog_Packages = 0
hot_Dog_Bun_Packages = 0


# Asking User How Many People Will Be Attending Cookout
number_Of_People = int(input("How many people will be attending the cookout?: "))

# Asking Limit Of How Many Hot Dogs Each Person Will Be Given
number_Per_Person = int(input("Enter the number of hot dogs each person will be given: "))

#Calculations
#######################

# Total Hot Dogs & Hot Dog Buns Needed
total_Hot_Dogs_Needed = number_Of_People * number_Per_Person
total_Hot_Dog_Buns_Needed = number_Of_People * number_Per_Person

# Setting Hot Dog Bun Packages Base Equation 
hot_Dog_Bun_Packages = int(total_Hot_Dog_Buns_Needed / hot_Dog_Buns)

# Setting Hot Dog Packages Base Equation
hot_Dog_Packages = int(total_Hot_Dogs_Needed / hot_Dogs)

# If Statement Seeing If There Is A Remainder To Add Another Package For Hot Dogs
if total_Hot_Dogs_Needed % hot_Dogs != 0:

    # Adding Additional Package, If The Remainder Isn't Zero
    hot_Dog_Packages += 1

    # Finds How Different The Total Hot Dogs Are
    hot_Dogs_Leftover = total_Hot_Dogs_Needed - (total_Hot_Dogs_Needed % hot_Dogs)

    # Finds The Number Of Leftovers Will Be Left Once Done
    hot_Dogs_Leftover = total_Hot_Dogs_Needed - hot_Dogs_Leftover

# If Statement Seeing If There Is A Remainder To Add Another Package For Hot Dog Buns
if total_Hot_Dog_Buns_Needed % hot_Dog_Buns != 0:

    # Adding Additional Package, If The Remainder Isn't Zero
    hot_Dog_Bun_Packages += 1

    # Finds How Different The Total Hot Dogs Are
    hot_Dog_Buns_Leftover = total_Hot_Dog_Buns_Needed - (total_Hot_Dog_Buns_Needed % hot_Dog_Buns)

    # Fids The Number Of Leftovers Will Be Left Once Done
    hot_Dog_Buns_Leftover = total_Hot_Dog_Buns_Needed - hot_Dog_Buns_Leftover

# Printing Results Of Cookout
print("Minimum number of packages of hot dogs required: ", hot_Dog_Packages)
print("\nMinimum number of packages of hot dog buns required: ", hot_Dog_Bun_Packages)
print("\nNumber of hot dogs left over: ", hot_Dogs_Leftover)
print("\nNumber of hot dog buns left over: ", hot_Dog_Buns_Leftover)















