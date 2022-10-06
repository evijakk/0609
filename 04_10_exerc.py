# Exercise
# read text from  sherlock_holmes_adventures.txt

# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file

# check file_line_len("sherlock_holmes_adventures.txt") -> 12305



# 1b -> write the function get_text_lines(fpath), which returns a list with only those lines that contain text.

# So we want to avoid/filter out those lines that contain whitespace

# PS preferably use encoding = "utf-8" when reading 



# 1c -> write the function save_lines(destpath, lines)

# This function will store all lines into destpath file 

# 1d -> call save_lines with destpath being "pure_sherlock.txt" and lines being the text lines we cleaned from 1b

# 1e -> write the function clean_punkts(srcpath, destpath)

# function will open the srcpath file, clear it from https://docs.python.org/3/library/string.html#string.punctuation

# then function will save the cleaned text into destpath
# clean_punkts("pure_sherlock.txt", "clean_sherlock.txt")


# 1f -> write the function get_word_usage(srcpath, destpath)

# The function opens the file and finds the most frequently used words

# recommendation to use Counter module!

# assume that the words are separated by either whitespace or newline (the good old split will come in handy)

# the saved list of words and frequency should be saved in destpath in the following form:

# word, count
# un, 3423
# es, 3242

# in effect you will be saving in standard csv format - https://docs.python.org/3/library/csv.html
# you can use csv module for this, but it is not necessary
# from pathlib import Path 

# with open('C:\Users\Latefekts\Desktop\github2\0609\sherlock_holmes_adventures.txt', encoding="utf-8") as f:  # create a file object
#     # filtered_lines = [line for line in f if needle in line]
# # # # # # # # # #     # so only get 3rd and 4th token from each line if they are actual tokens to be gotten
#     # filtered_lines = [line.split()[2:4] for line in f if len(line.split()) > 3]
#     # filtered_lines = [line.rstrip('\n')
#     #                   for line in f if line.startswith("And")]  # possible to use regex from re
#     # filtered_lines = [line for line in f if line[0] in string.digits] # so only lines which start with digits
# # # # # # # # # # #     #     # possible to use regex from re
# # # # # # # # # # #     #     filtered_lines = [line for line in f if line.startswith("And")]
# # # # # # # # # # #     # for more difficult filtering:
#     filtered_lines = []
#     for line in f:
#         if line.startswith("And"):
#             filtered_lines.append(line.rstrip())
# print(filtered_lines)
# # print(filtered_lines)
# # # # # # print(filtered_lines_num)
from pathlib import Path  

absolute_path = r"C:\Users\Latefekts\Desktop\github2\0609\sherlock_holmes_adventures.txt"
fstream = open(absolute_path, encoding="utf8")
text = fstream.read()
fstream.close() # crucial that we close the file when not using a context manager
print(text[:1])

def file_line_len(fstream):
    num_lines = sum(1 for _ in open('sherlock_holmes_adventures.txt'))
    return num_lines

print(file_line_len)