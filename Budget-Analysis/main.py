#
# Kiara Doucette
# 09/21/2024
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Write a proram that asks the user to enter the amount
# that he or she has budgeted for a month. A loop should
# then prompt the user to enter each of his or her expenses
# for the month and keep a running total. When the loop 
# finishes, the program should display the amount that the user
# is over or under budget.

# Declaring Variables Used In Program
total = 0
buget = 0
answer = "y"
expense = 0
difference = 0

# Asking User What Their Budge Is For The Month
budget = float(input("What Is Your Budget For A Month?: "))

# Enter While Loop Until User Says No More Expenses To Add For The Month
while answer == "y": 

    # User Enters The Expense Total And Adds 
    # It Stores It In The Total Variable
    expense = float(input("Enter An Expense: "))
    total += expense

    # Asks User And User Enters If They Have Anymore Expenses To Add
    answer = input("Do You Have Any More Expenses To Add? (Y/N): ")
    if answer == "Y":
        answer = "y"
    if answer == "N":
        answer = "n"
    # If User Enters Y Then While Loop Continues
    # If User Says N Then The While Loop
    #  Will End Giving Us The Total For The Month.

# Calculation For Under Or Over Budget
difference = budget - total

# If Statement To See If The Difference Between The Budget is Over or Under
# Or If User Has Met Their Expectations Of The Budget For The Month
if difference > 0:
    print("You Are Under Budget By $",format(difference,".2f") )
elif difference < 0:
    print("You Are Over Budget By $",format(difference,".2f") )
else:
    print("You Have Exactly Met Your Budget For The Month!!!")

