# Machine Learning

In this project your goal is to program a basic unsupervised learning algorithm called **K-means clustering**.

The K-means clustering algorithm is a simple unsupervised learning algorithm that receives unlabeled data samples as input and its goal is to cluster them into groups, specifically K-number of groups based on their similarities.

This means, in the end result samples within a cluster are close to each other and samples between clusters are distant from each other.

The way the algorithm works is by first randomly assigning coordinats (locations) of the centers of clusters (called centroids). Then the algorithm goes over each sample in the dataset and calculates distance between each sample to each centroid. Each sample is assigned to the cluster of its closest centroid. Then the coordinats of the clusters are updated based on the mean location of the data points that were assigned to the cluster. Then repeat the whole processe until the cluster centroids become stable.

Here is a high-level description of how the K-means clustering algorithm works:

- First choose an integer value and assign it to the variable K. This variable represent the number of clusters you want to have.
- Randomly choose initial coordinats for the K clusters.
- For each data point calculate the distance between the data point and each centroid.
- The data point gets assigned to the cluster of the closest centroid.
- After each data point being assigned to a cluster we update the centroids to be now located at the mean position of the cluster that is associated with that centroid.
- Repeat until cluster centroids become stable (or other criteria).

Your goal is the implement the K-means clustering algorithm and run it with three clusters (`K=3`) on the two features with `sepal_length` and `sepal_width`. At the end you should get something similar to the middle figure above.

Specifically, you task is to define a function called `kmeans_clustering` that takes as input a the data to be clustered and the number of clusters you want to have at the end. Within the function you implement the algorithm described above. At the end the function should return the two variables `k_labels` represententing the cluster each point is assigned to. This means that this variable should have the same number of elements as the data and each element is one integer that represent one of the clusters. The second variable that should be returned by the function is `k_centroids` which represents the coordinates (locations) of the centers of the clusters. This means that we have K=3, then there will be 3 points each having two values representing the two features of sepal_length and sepal_width. To calculate the distance between a data point and each centroid you may (but you don't have to) use the function in the cell below.
