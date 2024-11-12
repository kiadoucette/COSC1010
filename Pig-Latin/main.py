#
# Kiara Doucette
# 11/11/2024
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Write a program that reads a sentence as input and converts each word to 
# “Pig Latin.” In one version, to convert a word to Pig Latin, you remove 
# the first letter and place that letter at the end of the word. Then you 
# append the string “ay” to the word. Here is an example:
#English: I SLEPT MOST OF THE NIGHT 
#Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY


# Creating Main Function
def main():

    # Welcoming User
    # Prompt User To Enter The Sentence They Wish To Turn Into Pig Latin
    print("Welcome User!")
    print("*************************************************")
    english = str(input("Type a sentence you wish to turn into pig latin: "))

    # Calls pigLatin Function + Print Statement Conversion
    print("Pig Latin: ", pigLatin(english))

# Creating Pig Latin Function
def pigLatin(sentence):

    # Splits The Sentences To Look At Each Word
    words = sentence.split()
    # Creating Variable To Store Newly Created Words
    pig_latin_words = []

    # Checks The Words And Does Conversions To Pig Latin
    for word in words:
        if len(word) == 1:
            pig_latin_word = word + "ay"
        else:
            pig_latin_word = word[1:] + word[0] + "ay"
        pig_latin_words.append(pig_latin_word)

    # Returning Final Result
    return ' '.join(pig_latin_words)

# Calling Main Function To Work
main()