#
# Kiara Doucette
# 09/02/2024
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations
amount_Purchase = 0
total_Tax = 0
total_Sale = 0

# Constants for the state and county tax rates
state_Sales_Tax = 0.05
country_Sales_Tax = 0.025

# Get the amount of the purchase.
amount_Purchase = float(input('Enter the amount of a purchase: '))

# Calculate the state sales tax.
state_Sales_Tax = state_Sales_Tax * amount_Purchase

# Calculate the county sales tax.
country_Sales_Tax = country_Sales_Tax * amount_Purchase

# Calculate the total tax.
total_Tax = state_Sales_Tax + country_Sales_Tax

# Calculate the total of the sale.
total_Sale = amount_Purchase + total_Tax

# Print information about the sale.
print('Amount Purchase: ', amount_Purchase, '\nTotal Tax: ', total_Tax, '\nTotal Sale: ', total_Sale)
