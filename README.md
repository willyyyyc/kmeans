# K-Means clustering algorithm written from scratch

## Description

The K-Means clustering algorithm groups a dataset into k "clusters" by assigning each datapoint to a cluster based off of its proximity to the mean. The goal of this project was to write a K-Means clustering algorithm from scratch that grouped random user generated data points across a user generated range into k clusters.

For this project I used Python 3 and Matplotlib. I chose Python because of how well it caters to machine learning projects - Python has several built in machine learning libraries, and among them is a K-Means algorithm. However, I challenged myself to create this without referencing the library at all.

I was inspired to try and write this algorithm from scratch after learning about it briefly in my undergraduate class.

### Example Output - Graph displaying unclustered and clustered data:

    ![figure generated with matplotlib representing output](/kmeans/Screenshot_2023-02-15_19-59-34.png)

## Standard Algorithm:

1. **Initialization:** K initial "centroids" are randomly generate within the data domain, and act as seeds from which the clusters grow from. There are different ways of generating these initial centroids, such as picking k data points at random from the dataset, but for simplicity I chose the first k data points in the set.

2. **Reassignment:** K clusters are populated by associating every data point with the nearst centroid - the euclidean distance is computed between the data point and each centroid, then the data point is assigned to the centroid with which it is closest to.

3. **Recomputation:** The mean of each cluster is calculated and this mean becomes the new centroid.

4. **Convergence:** Steps 2 and 3 are repeated until convergence has been reached. This is when the data points contained in each cluster remain the same even after recomputing the centroids.

### Additional Steps:

- The user first defines the size and range of the dataset.
- Two graphs are displayed, one with the plotted and unclustered data and one with the data after the K-Means algorithm has been applied.
- The number of iterations is displayed. This represents the number of recomputations before convergence was achieved.

## Instructions:

1. Enter an integer "n" to generate n data points. Enter an integer "r" to set the magnitude of the largest and smallest x and y; i.e. define a range where x is in [-r, r] and y is in [-r, r].

2. Observe the two graphs that are displayed!

## Notes:

- At the moment, "k" is set to 3. This means that regardless of the data size, there will always be three clusters. In the future, I plan on allowing the user to define k but I set it at some arbitrary constant value while I was trying to figure out the rest of the algorithm.
- In the event that convergence does not occur fast enough (a potential problem with this algorithm if the starting centroids are not optomized) there is a breakpoint set after 20 iterations. It has yet to take 20 iterations, but that is likely due to the size of the dataset.
- I would like to compare this to the K-Means algorithm in the Python library some day. It would be very interesting to see what happens with the same dataset!

## References and Sources:

The folowing sites were very helpful in understanding what this algorithm was:

- https://towardsdatascience.com/a-practical-guide-on-k-means-clustering-ca3bef3c853d 
- https://en.wikipedia.org/wiki/K-means%2B%2B
- https://towardsdatascience.com/create-your-own-k-means-clustering-algorithm-in-python-d7d4c9077670
