#
# Kiara Doucette
# 09/02/2024
# Sales Prediction Programming Project
# COSC 1010 
#

# Variables to hold the sales total and the profit
total_Sales = 0
profit = 0

# Get the amount of projected sales.
total_Sales = float(input ('Enter the projected sales: '))

# Calculate the projected profit.
profit = total_Sales * 0.23

# Print the projected profit.
print('The profit is $' , format(profit, ',.2f'))
