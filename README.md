# kmeans

#standard algorithm:
1. k initial "means" (chose an integer k, maybe start with a default of 3
but allow for it to be changed by the user if n is bigger than three i.e. 
pick a k that is less than n) are randomly generate within the data domain

2. k clusters are created by associating every observaition with the nearst mean. - calculate euclidean distance (?) between each point and the mean, then assign it to the mean with which it has the smallest distance

3. The centroid of each of the k clusters becomes the new mean

4. Steps 2 and 3 are repeated until convergence has been reached - the data points in each group don't change when chosing a new centroid