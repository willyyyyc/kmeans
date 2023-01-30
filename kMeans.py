#program to generate n random points on a graph of range (-x,x) and (-y,y)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import random

class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

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

#print data points; a list of DataPoint objects containing an x and y (representing a coordinate on the plot)
data_points = []
i = 0
while i <= n:
    new_dp = DataPoint(x[i], y[i])
    data_points.append(new_dp)
    i += 1

for dp in data_points:
    print(dp)
    
fig, ax = plt.subplots()
plt.scatter(x, y)
plt.show()




#reference for continued use:
#https://matplotlib.org/stable/tutorials/introductory/quick_start.html

