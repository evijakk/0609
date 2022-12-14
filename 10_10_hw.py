# TODO
# put the imports first

# create a function that returns a list of random dice throws
# it should have two parameters
# - number of dice in each throw, default 4
# - number of throws, default 100


# even better would be a another function to which you give the list of dice throws and it 
# plots the histogram
# this function would have two parameters
# - the list of dice throws - no default
# - the name of the file to save the plot to - default - empty string
# if the file name is empty string, the plot should be shown on the screen

# use the first function to create a list of 1000 dice throws with 6 dice in each throw
# pass the result to 2nd function to plot the histogram and save it to a file
# BONUS: file name should have current date and time in it


# ideally you would then run them from main guard
# which means this file would be a module, that can be imported


import matplotlib.pyplot as plt
import numpy as np
import random

def dice_histogram(throws):
    y = []
    for n in range(throws):
        y.append(random.randrange(6)+1)
    # print(y)
    plt.hist(y, bins = 6)
    plt.show()


print(dice_histogram(1000))