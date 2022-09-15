# The user enters a name.

# You print user name in reverse (should begin with capital letter)
#  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"

# Example:

# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

person_name = input("Enter your name, please.")
print(person_name[::-1].capitalize() + ", a thorough mess is it not " + person_name[0].capitalize() + "?")

# 2. Almost Hangman
# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***
# In principle, this is a good start to the game of hangman.

# game_word = input("Enter word, please.")
# print("*"*len(game_word))
# first_letter = input("Enter letter, please.")
# for c in game_word:

