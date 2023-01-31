# kmeans

#standard algorithm:
1. k initial "means" (chose an integer k, maybe start with a default of 3
but allow for it to be changed by the user if n is bigger than three i.e. 
pick a k that is less than n) are randomly generate within the data domain

2. k clusters are created by associating every observaition with the nearst mean. - calculate euclidean distance (?) between each point and the mean, then assign it to the mean with which it has the smallest distance

3. The centroid of each of the k clusters becomes the new mean

4. Steps 2 and 3 are repeated until convergence has been reached - the data points in each group don't change when chosing a new centroid

5. perhaps have an option to recompute data with different numbers of clusters, maybe export data points to a text file and list the clusters


references and sources:
https://towardsdatascience.com/a-practical-guide-on-k-means-clustering-ca3bef3c853d 
https://en.wikipedia.org/wiki/K-means%2B%2B
https://towardsdatascience.com/create-your-own-k-means-clustering-algorithm-in-python-d7d4c9077670
