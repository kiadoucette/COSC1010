#
# Kiara Doucette
# 11/18/2024
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Import random function
import random
# Capping Quiz To Ask User 5 Questions
NUM_STATES = 5
def main():
   # Intizalizing stateDictionary() function to initalize stateCapitals variables
   stateCapitals = stateDictionary()

   # Stores how much a user gets incorrectly or correct
   correct = 0
   incorrect = 0

    # Repeats 5 Times To Ask Random States and prompting the user to answer the correct Capital
   for count in range(NUM_STATES):
        # Finds the item in the list
        state, capital = stateCapitals.popitem()
        # Asks user what the capital of the state is
        print("What is the capital of", state, "?", end='')
        # Stores users input
        userInput = input()

        # Compares to the list to see if user wrote the right answer
        if userInput.lower() == capital.lower():
             correct += 1
             print('You are correct!!!')
        else:
             incorrect += 1
             print('You are incorrect :(')

    # Print statements to provide the user of how many they got incorrectly or correct.
   print('How many you got correct: ', correct)
   print('How many you got incorrectly: ', incorrect)
    
   

def stateDictionary():
      # Initializing Capital Dictionary
      capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South       Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
      return capitals
# Call the main function.
main()
