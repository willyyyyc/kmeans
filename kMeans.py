#program to generate n random points on a graph of range (-x,x) and (-y,y)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random

#input n, the number of randomly generated points
n = int(input("Enter an integer n to generate n points: "))
r = int(input("Enter an integer r to set range of x and y where x,y E (-r, r): "))

x = []
y = []
i = 0
while i <= n:
    x.append(random.randrange(-1 * r, r + 1))
    y.append(random.randrange(-1 * r, r + 1))
    i+=1

print(x)
print(y)

fig, ax = plt.subplots()
plt.scatter(x, y)
plt.show()




#reference for continued use:
#https://matplotlib.org/stable/tutorials/introductory/quick_start.html

