import unittest

class TestAllFunctions(unittest.TestCase):
    """
    def test_set_character(self):
        with self.subTest():
            self.assertEqual(set_character_number(), 1)
        with self.subTest():
            self.assertEqual(set_character_number(), 2)
        with self.subTest():
            self.assertEqual(set_character_number(), 3)
        with self.subTest():
            self.assertEqual(set_character_number(), 4)
        with self.subTest():
            self.assertEqual(set_character_number(), 5)
    """
    """
    def test_manual(self):
        self.assertEqual(set_names_manual(2), ['WOOI KING', 'HUI XUAN'])
        self.assertEqual(set_names_manual(3), ['HOMELANDER', 'DORAEMON', 'TERMINATOR'])
        self.assertEqual(set_names_manual(3), ['JOEL', 'STEVEN', 'TOMMY'])
    """
    """
    def test_div(self):
        with self.subTest():
            self.assertEqual(set_divided_by_integer(), 1)
        with self.subTest():
            self.assertEqual(set_divided_by_integer(), 2)
        with self.subTest():
            self.assertEqual(set_divided_by_integer(), 3)
        with self.subTest():
            self.assertEqual(set_divided_by_integer(), 4)
        with self.subTest():
            self.assertEqual(set_divided_by_integer(), 5)
        with self.subTest():
            self.assertEqual(set_divided_by_integer(), 6)
    """
    def test_auto(self):
        self.assertEqual(set_names_automatic(DEFAULT_CHARACTER_LIST, 4, 5), ['LELO MUSK', 'SUPERMARIO', 'MICHONNE', 'WOLVERINE'])
        self.assertEqual(set_names_automatic(DEFAULT_CHARACTER_LIST, 5, 3), ['HOMELANDER', 'TERMINATOR', 'MR. MONASH', 'HERMIONE GRANGER', 'SUNFLOWER'])
    
    
DEFAULT_CHARACTER_LIST = ['HOMELANDER', 'IMAN', 'TERMINATOR', 'LELO MUSK', 'MR. MONASH', 
'FYP STUDENT 2', 'HERMIONE GRANGER', 'SUPERMARIO', 'SUNFLOWER', 'THANOS',
'LUIGI', 'CHATGPT5', 'PATRICK STAR', 'GARY THE SNAIL', 'MICHONNE',
'VENOM','SPONGEBOB', 'DORAEMON', 'WOLVERINE', 'DORAEMON 2.0', 'BUMBLEBEE']

def set_character_number() -> str:
    """
    Asks the user for how many characters they want, and then print an appropriate string in the end.
    
    @return: A string with an appropriate sentence. (see the output for example)
    """
    # asking the number of characters they want.
    numOfCharacters = int(input("How many characters do you want?\n"))

    # code repeats until the user enters the number of characters between 1 to 5 (inclusive) only.
    while(numOfCharacters < 1 or numOfCharacters > 5):
        # reprompts the user to enter the appropriate number again.
        numOfCharacters = int(input("You may choose 1-5 characters only!\nHow many characters do you want?\n"))

    # manipulates the string if there are multiple characters.
    isMultipleCharacters = "characters" if numOfCharacters > 1 else "character"

    # final output.
    print ("There will be {0} {1} attempting to Rise from the (Mon)Ashes!".format(numOfCharacters, isMultipleCharacters))
    return numOfCharacters

def set_names_manual(number_of_characters: int) -> list[str]:
    """
    Returns a list of manually entered names for the characters.
    
    @param int number_of_characters: The number of characters that the user wants to name.
    @return: A list of names that the user manually entered, given that each name is unique.
    """
    
    names = [] # names list to store the names.
    
    for i in range(number_of_characters):
        nameToAppend = input("Set character {0} name:\n".format(i+1)).upper() # converts the string all to uppercase.
        
        # repeatedly reprompts the user to enter unique names only.
        while (nameToAppend in names):
            print("{0} is a duplicate, try again!".format(nameToAppend))
            nameToAppend = input("Set character {0} name:\n".format(i+1)).upper()
            
        names.append(nameToAppend)
        
        # stopping the loop if the number of character limit has been reached.
        if len(names) == number_of_characters:
            break
    return names

def set_divided_by_integer() -> int:
    """
    Asks the user to enter an integer between 1 and 6 (inclusive), and returns the value needed for naming characters automatically.
    
    @return: An integer that will be used in automatic naming algorithm.
    """
    divisible_by = int(input("Pick a number between 1-6 (inclusive):\n"))
    
    # reprompts the user to enter the correct value within the range 1-6.    
    while(divisible_by < 1 or divisible_by > 6):
        print("You may choose a number between 1-6 (inclusive) only!")
        divisible_by = int(input("Pick a number between 1-6 (inclusive):\n"))
    
    return divisible_by

def set_names_automatic(character_list: list[str], number_of_characters: int, divisible_by: int) -> list[str]:
    """
    Automatically appends names of the characters in a list that depends on the divisible_by integer the user has provided.
    
    @param list[str] character_list: A list of character names the characters can possibly have.
    @param int number_of_characters: The number of characters the user wants to create.
    @param int divisible_by: The integer that the user chose as part of automatically choosing a name for each of the characters.
    @return: A list of names that have been automatically assigned.
    """
    names = [] # keeps a list of names.
    
    for i in range(len(character_list)):
        
        # finding the number of consonants in each name.
        count = 0
        vowels = ['A', 'E', 'I', 'O', 'U']
        for character in character_list[i]:
            if character >= 'A' and character <= 'Z' and character not in vowels: # only is a consonant if it is not a number, a vowel or any special character.
                count += 1
        
        if (count % divisible_by == 0) and (character_list[i] not in names): # only append name if the number of consonants is divisible by divisible_by
            names.append(character_list[i])
        
        if len(names) == number_of_characters: # break the loop if the number of character limit has been reached.
            break
    
    return names
            
def return_welcome_message(names: list[str]) -> str:
    """
    Prints a welcome message for the characters.
    
    @param list[str] names: A list of names of the characters that the welcome message will be printed for.
    @return: A string that consists of the welcome message.
    """
    if len(names) == 1: # if len() == 1
        return ("It is the year 3045. Sentient Artificial Intelligence Bots have now taken over.\n{0} must rise from the (Mon)ashes!\nThey are BERYL's only hope!".format(names[0]))
    else: # if len() > 1
        return ("It is the year 3045. Sentient Artificial Intelligence Bots have now taken over.\n{0} and {1} must rise from the (Mon)ashes!\nOnly one character may survive!".format(", ".join(names[:-1]), names[-1]))

#for debugging purpose only, please delete during final submission
if __name__ == "__main__":
    unittest.main()
    """
    print(set_character_number())
    print(set_names_manual(2))
    print(set_divided_by_integer())
    print(set_names_automatic(DEFAULT_CHARACTER_LIST, 4, 5))
    print(return_welcome_message(['GARY THE SNAIL', 'MICHONNE']))
    """