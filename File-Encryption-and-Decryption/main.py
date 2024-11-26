#
# Kiara Doucette
# 11/25/2024
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Creating Main Function
def main():
    # Creating variables/ Calling functions
    # Initalizing encryption by referencing the code dictionary
    # (Where the text get's scambled by self created code)
    encryption = codeDictionary()

    # Grabs the content from the text file
    # Reads the file and initalizes the variable
    original_content = fileRead()

    # Initalizing encrypted content
    encrypted_content = encryptedMessage(original_content, encryption)
    # Saving it to encrypted.txt to grab later for decryption
    savingEncryptedMessage(encrypted_content)

    # Print statements
    print("Orginial: ", original_content)
    print("Encrypted Message: ", encrypted_content)

    # Reverses the code grabbing the opposite of what was assigned originally
    decryption = reverseCodeDictionary(encryption)

    # Reassigns the content back together
    decrypted_content = decryptedMessage(encrypted_content, decryption)

    # Prints original content back together after decryption
    print("Decrypted Message: ", decrypted_content)
  
  
# Creating A Code Dictionary Function As A Method
def codeDictionary():

    # initializing reassignments for words to make a code
    codes = {
        'A' : '~', 'a' : '!', 'B' : '@', 'b' : '#', 'C' : '$', 'c' : '%',
         'D' : '^', 'd' : '&', 'E' : '*', 'F' : '?', 'f' : '1', 'G' : '2',
         'g' : '3', 'H' : '4', 'h' : '5', 'I' : '6', 'i' : '7', 'J' : '8',
         'j' : '9', 'K' : '0', 'k' : '+', 'L' : '=', 'l' : '<', 'M' : '>',
         'm' : '_~_', 'N' : '_!_', 'n' : '_@_', 'O' : '_#_', 'o' : '_$_',
         'P' : '_%_', 'p' : '_^_', 'Q' : '_&_', 'q' : '_*_', 'R' : '_?_',
         'r' : '_?_', 'S' : '_1_', 's' : '_2_', 'T' : '_3_', 't' : '_4_',
         'U' : '_5_', 'u' : '_6_', 'V' : '_7_', 'v' : '_8_', 'W' : '_9_',
         'w' : '_10_', 'X' : '_11_', 'x' : '_12_', 'Y' : '_13_', 
         'y' : '_14_', 'Z' : '_15_', 'z' : '_16_'
    }

    # Returns List
    return codes

# Reads the Original Text file
def fileRead():
        # Opens the file
        with open('text.txt', 'r') as file:

            # Reads The Content's in The File
            content = file.read()

        # Returns the content of the file
        return content


# Creating ecryptedMessage Function.
# Grabs the original file and compares the words to the codes
def encryptedMessage(content, codes):
        
        #Created empty string to store list
        encrypted_content = ''

        # Compares each char in the original files words
        for char in content:

            # Default to the character itself if no code is found
            encrypted_content += codes.get(char, char) 

        # Returns Encrypted List
        return encrypted_content


# Creating Function to save to encrypted text file
def savingEncryptedMessage(encrypted_message):
        
        # Opens the file to be written 
        with open('encrypted.txt', 'w') as file:

            # Writes the encryption in he file
            file.write(encrypted_message)

        # Makes sure it is saved to make sure that the decryption works
        print("Encrypted message saved to 'encrypted.txt'")


# Reverses the code dictionary, to decode
def reverseCodeDictionary(codes):
        
        # Creates a new list to reverse their assignments
        reverse_codes = {v: k for k, v in codes.items()}

        # Returns the code dictionary reversed
        return reverse_codes


# Reads the encrypted file
def fileReadEncrypted():

    # Opens encrypted file
    with open('encrypted.txt', 'r') as file:

        # Reads it and stores the content
        content = file.read()

    # Returns encrypted content to be read
    return content


# Rewrites it back to original message
def decryptedMessage(content, reverse_codes):

    # Creating variable for the decrypted content
    decrypted_content = ''
    # Index variable
    i = 0
    while i < len(content):

        # checking each potential encrypted symbol in the content
        for code, char in reverse_codes.items():

            # Check if the current part of the content matches the code in the dictionary
            if content[i:i+len(code)] == code:
                decrypted_content += char

                # Move index past the decrypted symbol
                i += len(code) 
                break

        else:
            # If no match, just add the character (for things like spaces)
            decrypted_content += content[i]
            i += 1
            
    return decrypted_content

# Starts Main Function 
main()