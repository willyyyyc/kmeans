# William Carmichael
# @willyyyyc
# Last modification: 02-15-23
# Project description: The goal of this project was to create a 
# k-means clustering algorithm from scratch. The user would generate a random
# dataset which would then be grouped into k clusters (for now, k = 3)

import matplotlib.pyplot as plt
import numpy as np
import math
import random
import copy

# data point class: each data point object has an x and y value
class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# centroid class
# inherits datapoint; a centroid is a data point (has an x and a y)
# but has additional functions
class Centroid(DataPoint):
    def __init__(self, x, y):
        DataPoint.__init__(self, x, y)
        self.cluster = []

    # recompute function computes a new x and y value based on 
    # the median in its cluster
    def recompute(self):
        cluster_x = []
        cluster_y = []
        for dp in self.cluster:
            cluster_x.append(dp.x)
            cluster_y.append(dp.y)
        self.x = np.mean(cluster_x)
        self.y = np.mean(cluster_y)

    # printing the centroid prints the datapoints as well
    def __str__(self):
        string_rep = f"Centroid: ({self.x}, {self.y}). Cluster: "
        for dp in self.cluster:
            string_rep += str(dp)
        return string_rep
    
    def cluster_length(self):
        return len(self.cluster)

# this function assigns data points to a centroids cluster based on proximity
def assign(centroids, dp):
    # find the closest centroid to the data point by comparing euclidean distances
    distances = []
    for centroid in centroids:   
        distances.append(math.sqrt((dp.x - centroid.x)**2 + (dp.y - centroid.y)**2))

    # assign data point to list contained in closest centroid
    closest = distances.index(min(distances))
    centroids[closest].cluster.append(dp)

# creates a deep copy of the centroid objects to compare clusters after
# recomputing and reassigning
def make_copy(centroids):
    copied_centroids = []
    for centroid in centroids:
        copied_centroid = copy.deepcopy(centroid)
        copied_centroids.append(copied_centroid)
    return copied_centroids

# function that tests for convergence by comparing the clusters of new centroids and
# the most recent copy. returns true if the clusters are the same - convergence has 
# been reached. 
def convergence(centroids, copied_centroids):
    i = 0
    # loop through centroids, return false if lengths do not match (not equal)
    # otherwise compare data points in cluster. return false at an inequality
    while i < len(centroids):
        if centroids[i].cluster_length() != copied_centroids[i].cluster_length():
            return False
        else:
            j = 0
            while j < centroids[i].cluster_length():
                if centroids[i].cluster[j] != copied_centroids[i].cluster[j]:
                    return False
                j += 1
        i += 1
    print()
    print("Converged.")
    return True

# user inputs number of data points and the range of x and y values
n = int(input("Enter an integer n to generate n points: "))
r = int(input("Enter an integer r to set range of x and y where x,y E (-r, r): "))

# temporarly, k is a constant
k = 3                                   # would like to allow user to input k

# create data points with random x and y in range
x = []
y = []
i = 0
while i < n:
    x.append(random.randrange(-1 * r, r + 1))
    y.append(random.randrange(-1 * r, r + 1))
    i+=1

# append data points to list    
data_points = []
i = 0
while i < n:
    new_dp = DataPoint(x[i], y[i])
    data_points.append(new_dp)
    i += 1

# k-means clustering algorithm
# select the first k data points to act as "seeds" for the clusters to grow around
# and append to centroid list
centroids = []
i = 0
while i < k:
    x1 = data_points[i].x
    y1 = data_points[i].y
    centroid = Centroid(x1, y1)
    centroids.append(centroid)
    i += 1

# iterate through algorithm until convergence has been achieved
iterations = 0
while True:
    # make deep copy of centroid objects
    if iterations > 0:
        copied_centroids = make_copy(centroids)
        

    # reassignment: iterate through data points, assigning each point to the nearest centroid
    for centroid in centroids:
        centroid.cluster.clear()

    for dp in data_points:
        assign(centroids, dp)

    # compare clusters of copied centroid objects to new clusters to test for convergence
    if iterations > 0 and convergence(centroids, copied_centroids):
        break

    # recompution: mean of data points becomes new centroid
    for centroid in centroids:
        centroid.recompute()

    # in the event that convergence has not been reached in a reasonable time break
    # after 100 iterations
    if iterations > 100:                    # may not be needed, have not tested a data set large enough to even approach this many iterations
        break

    iterations += 1

print()
print("Final centroids and their clusters:")
print()

for centroid in centroids:
    print(centroid)
    print()

print(f"Convergence was achieved after {iterations} iterations.")

# create two sublots of equal size to display unclustered and clustered data
fig, (ax1, ax2) = plt.subplots(ncols=2)

# display unclustered data
ax1.scatter(x, y, c="k")

# plotting the clusters by iterating through the centroid array and 
# accessing the x and y values of data points
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

# plotting the centroids as plus signs
for centroid in centroids:
    ax2.plot(centroid.x, centroid.y, "k+")

# formating figures and adding titles
ax1.set_box_aspect(1)
ax2.set_box_aspect(1)
ax1.set_title("Unclustered Random Data Points")
ax2.set_title(f"Clustered Data Points (i = {iterations})")
plt.suptitle("K-MEANS CLUSTERING ALGORITHM")

plt.show()