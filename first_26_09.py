# # 1. What's the frequency?

# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single letter counts.

# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} 

# # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included

#  There may also be a solution with Counter from standard Python library but this is definitely not necessary, although it is very elegant smile

def get_char_count(text):
    char_dictionary = {}
    for n in text:
        keys=char_dictionary.keys()
        if n in char_dictionary:
            char_dictionary[n] += 1
        else:
            char_dictionary[n] =1
    return char_dictionary

print(get_char_count("assdddfffgggg"))


