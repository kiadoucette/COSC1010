#
# Kiara Doucette
# 11/11/2024
# Vowels and Consonants Programming Project
# COSC 1010 DNT
#
# Use comments liberally throughout the program. 

# Main Function
def main():
    # Getting String Input From The User
    user_str = input('Enter a string of characters: ')

    # Report the vowels and consonants.
    print('That string has', num_vowels(user_str), 'vowels and',
          num_consonants(user_str), 'consonants.')
    
    # The Vowels Function
    # Returns a number of vowels in an arguement
def num_vowels(s):
    vowels = ['a', 'e', 'i','o', 'u']
    v_count = 0
    # Counts the Vowels
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1
    # Return the consonant count.
    return v_count

# The Consonants Function
def num_consonants(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    c_count = 0
    # Counts the Consonants
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1
    return c_count

main()
