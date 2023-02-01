#program to generate n random data points on a graph of range (-x,x) and (-y,y)

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
import random

#data point class
class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

#centroid inherits DataPoint
class Centroid(DataPoint):
    def __init__(self, x, y):
        DataPoint.__init__(self, x, y)
        self.cluster = []

    def recompute(self):
        cluster_x = []
        cluster_y = []
        for dp in self.cluster:
            cluster_x.append(dp.x)
            cluster_y.append(dp.y)
        self.x = np.mean(cluster_x)
        self.y = np.mean(cluster_y)

    def __str__(self):
        string_rep = f"Centroid: ({self.x}, {self.y}). Cluster: "
        for dp in self.cluster:
            string_rep += str(dp)
        return string_rep

    
def assign(centroids, dp):
    #find the closest centroid to the data point by comparing euclidean distances
    distances = []
    for centroid in centroids:     
        distances.append(math.sqrt((dp.x - centroid.x)**2 + (dp.y - centroid.y)**2))

    #assign data point to list contained in closest centroid
    closest = distances.index(min(distances))
    centroids[closest].cluster.append(dp)


#user input parameters
n = int(input("Enter an integer n to generate n points: "))
r = int(input("Enter an integer r to set range of x and y where x,y E (-r, r): "))
k = 3

#create data points:
x = []
y = []
i = 0
while i < n:
    x.append(random.randrange(-1 * r, r + 1))
    y.append(random.randrange(-1 * r, r + 1))
    i+=1
    
data_points = []
i = 0
while i < n:
    new_dp = DataPoint(x[i], y[i])
    data_points.append(new_dp)
    i += 1

#print data points
for dp in data_points:
    print(dp)
print(str(data_points))

#k-means clustering algorithm
#select the first k data points to act as "seeds" for the clusters to grow around
centroids = []
i = 0
while i < k:
    x1 = data_points[i].x
    y1 = data_points[i].y
    centroid = Centroid(x1, y1)
    centroids.append(centroid)
    i += 1

convergence = False
while not convergence:
    #reassignment: iterate through data points, assigning each point to the nearest centroid
    for dp in data_points:
        assign(centroids, dp)
    
    #recompution: "average" of data points
    for centroid in centroids:
        centroid.recompute()

    #check convergenve
    #for now, rig to have one iteration
    convergence = True

for centroid in centroids:
    print(centroid)

#create two sublots of equal size to display unclustered and clustered data
fig, (ax1, ax2) = plt.subplots(ncols=2)

ax1.scatter(x, y, c="k")

#plotting the clusters
colours = ["r", "g", "b"]
i = 0
for centroid in centroids:
    cx = []
    cy = []
    for dp in centroid.cluster:
        cx.append(dp.x)
        cy.append(dp.y)
    ax2.scatter(cx, cy, c=colours[i])
    i += 1

#plotting the centroids
for centroid in centroids:
    ax2.plot(centroid.x, centroid.y, "k+")

ax1.set_box_aspect(1)
ax2.set_box_aspect(1)
ax1.set_title("Unclustered Random Data Points")
ax2.set_title("Clustered Data Points")
plt.suptitle("K-MEANS CLUSTERING ALGORITHM")

plt.show()

#note: add an animation of second graph, like on the wikipedia page, refresh the graph with each iteration

#reference for continued use:
#https://matplotlib.org/stable/tutorials/introductory/quick_start.html

