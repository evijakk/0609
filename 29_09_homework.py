# write a function of 3 arguments all strings
# function should return lexigraphically ordered string of unique characters
# these unique characters must be present in BOTH  of the first two strings 
# BUT not in the third "badstring"

# example:
# "abcf", "fab", "boo"  returns -> "af" 
# because "a" is in both "abc" and "fab" but not in "boo"
# same goes for "f" it is present in both "good strings" but not in "badstring"
# notice "b" is not in the result because it is in the badstring.

# slightly harder way would be to use loops and if statements to check each character
# the easy way is to use sets and set operations 😊

# either approach is acceptable

def good_and_bad_strings (a,b,c):
    first_string = set(a)
    second_string = set(b)
    third_string = set(c)
    both_string = first_string&second_string 
    resultats = both_string - third_string
    sorted(resultats)
    return(resultats)

print(good_and_bad_strings("zkabcf", "zkfab", "boo"))