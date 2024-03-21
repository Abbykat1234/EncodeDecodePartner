"""this is the encode function"""


def encode(pass_to_encode):
    """ since in python, individual items in an ordered set of data can be accessed
    directly using a numeric index, I am using indexing to access the individual
    characters of the string number"""
    """initializing the string variable joined_string_encoded to empty"""
    joined_string_encoded = " "
    """I use a for loop to iterate through each of the characters in the string"""
    for word in pass_to_encode:
        int_word = int(word)
        """adds three to the initial value of the individual string character after converting 
           the string in pass_to_encode into an integer data type"""
        encoded_word = int_word + 3
        """converts the endcoded individual integers into individual strings"""
        encodedword_as_string = str(encoded_word)
        joined_string_encoded = joined_string_encoded + encodedword_as_string
    print(joined_string_encoded)

    return joined_string_encoded

    """prints a space between asking the user to input the number they want encoded & the
    message that their password has been encoded & stored"""
    print()
    """tells the user that their password has now been encoded and stored"""
    print("Your password has been encoded and stored!")
    print()


""" this is the decode function that my partner writes """


def decode():
        pass


""" the if name == main statement so that it runs with zybooks"""
if __name__ == '__main__':

    """ while loop that prompts the user to pick an input repeatedly until they choose option 3 - quit"""
    while True:
        """ the menu itself"""
        print("Menu")
        """prints a space between Menu and the lines"""
        print()
        print("-------------")
        print()
        """prints a space between the lines and the beginning of the menu options"""
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        """printing two empty spaces"""
        print()
        print()
        """ prompts the user to enter a menu choice from 1 -3 & stores it in the variable menu_option"""
        menu_option = int(input("Please enter an option: "))
        """ printing space between asking the user for the two different inputs"""
        print()
        """ if logic to help process the different input cases"""
        """logic for the first menu_option"""
        """calls the function that encodes the user's input."""
        if menu_option == 1:
            """prompts the user to enter the password that they want encoded and stores the value 
               that they have given in the string variable pass_to_encode"""
            pass_to_encode = input("Please enter your password to encode: ")
            encode(pass_to_encode)
        """logic for the second menu_option"""
        """calls the function decode to decode the password that the user entered"""
        if menu_option == 2:
            decode()
        """logic for the third menu_option"""
        """exits the program using the control statement break"""
        if menu_option == 3:
            break



