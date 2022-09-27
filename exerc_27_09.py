# 1. Min, Avg, Max

# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, 
# and the largest value in the string, respectively.

# Example:

# get_min_avg_max ([0,10,1,9]) -> (0,5,10)

# the incoming sequence can be a tuple or a list with numeric values.
###############################
from statistics import mean #python put this in the code itself :D

def get_min_avg_max(from_string):
    smallest_value = min(tuple(from_string))
    aritmetic_mean = mean(tuple(from_string))
    biggest_value = max(tuple(from_string))
    return(smallest_value, aritmetic_mean, biggest_value)

print(get_min_avg_max([7,8,4,99,23456,9]))


# 3. Is there a pangram?
# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')
# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise
# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram
# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a
# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False
# Bonus: test it also on Latvian alphabet:
# a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
# print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv)) -> True
# Bonus: test it also on Lithuanian alphabet:
# a_lt = 'aąbcčdeęėfghiįyjklmnoprsštuųūvzž' # see if this correct
# some languages have perfect pangrams, some do not
# perfect pangram - a pangram that uses every letter of the alphabet at just once

def is_pangram(your_text):
    alphabet=set('abcdefghijklmnopqrstuvwxyz')
    
    return set(your_text.lower().replace(" ", "")) == alphabet

print(is_pangram("abcdefghijk lmnaoph buAGFvhqrstuvwxyz"))


# Latviešu:
def is_pangram(your_text):
    alfabēts=set('aābcčdeēfgģhiījkķlļmnņoprsštuūvzž')
    
    return set(your_text.lower().replace(" ", "")) == alfabēts

print(is_pangram("Tfū čeh džungļos blīkšķ zvaņģim jācērp"))