#
# Kiara Doucette
# 11/04/2024
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# 8_ball_responses.txt
import random

def main():
    # Declaring variables
    count = 0
    listOfAnswerRandomNumber = []
    toContinue = True

    while toContinue:
        # Prompting User To Ask A Question
        question = str(input("What Is Your Question?: "))

        # Opening Text File
        myFile = open('8_ball_responses.txt', 'r')

        # Reading File While Appending It To A List
        for line in myFile:

            # Counting For the Random Range To Make Sure
            # Of File Integrity
            count = count + 1

            # Populating List
            listOfAnswerRandomNumber.append(line.strip())

        # Randomizing Number & Response
        randomResponse = random.randrange(count)

        # Printing Response
        print(listOfAnswerRandomNumber[randomResponse])

        # Asking User If They Would Like To Ask Another Question
        computerQuestion = str(input("Would You Like To Ask Another Question? (Hit 0 To Quit):"))
        
        # Either Quitting While Loop Or Continuing To Ask Questions
        if computerQuestion != '0':
            toContinue = True
        else:
            toContinue = False
    
    # A Little Message From The 8 Ball
    print("Come Again Back Soon, If You'd Like Me To Answer Anymore Questions :)")


    myFile.close()


main()