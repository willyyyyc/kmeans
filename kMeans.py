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

class Centroid:
    def __init__(self, x, y, cluster):
        self.x = x
        self.y = y
        self.cluster = cluster
    

#user input parameters
n = int(input("Enter an integer n to generate n points: "))
r = int(input("Enter an integer r to set range of x and y where x,y E (-r, r): "))
k = 3

#create data points:
x = []
y = []
i = 0
while i <= n:
    x.append(random.randrange(-1 * r, r + 1))
    y.append(random.randrange(-1 * r, r + 1))
    i+=1
    
data_points = []
i = 0
while i <= n:
    new_dp = DataPoint(x[i], y[i])
    data_points.append(new_dp)
    i += 1

#print data points
for dp in data_points:
    print(dp)
print(data_points)

#k-means clustering algorithm
#select the first k data points to act as "seeds" for the clusters to grow around
centroids = []
i = 0
while i < k:
    centroid = Centroid[data_points[i].x, data_points[i].y, list]
    centroids.append(centroid)
    i += 1


#plot initial data points (twice for now)
fig, (ax1, ax2) = plt.subplots(1,2)
ax1.scatter(x, y)
ax2.scatter(x, y)
plt.show()


#note: add an animation of second graph, like on the wikipedia page, refresh the graph with each iteration

#reference for continued use:
#https://matplotlib.org/stable/tutorials/introductory/quick_start.html

