# TODO
# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course

import matplotlib.pyplot as plt
import numpy as np

x = list(range(-10, 10))
y = []
for n in x:
    y.append((x[n]+5)**3)

plt.plot(x,y)
plt.show()
