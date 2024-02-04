## k-means clustering algorithm

the K-means clustering algorithm is a simple unsupervised learning algorithm. it receives unlabeled data samples as input and its goal is to cluster them into K groups, based on their similarities / how close they are to each other.

the way the algorithm works is by first randomly assigning coordinats (locations) of the centers of clusters (called centroids). then the algorithm goes over each sample in the dataset and calculates distance between each sample to each centroid. each sample is assigned to the cluster of its closest centroid. then the coordinates of the clusters are updated based on the mean location of the data points that were assigned to the cluster. then we repeat the whole process until the cluster centroids become stable.

1. first choose an integer value and assign it to the variable K. this variable represent the number of clusters you want to have.
2. randomly choose initial coordinats for the K clusters.
3. for each data point calculate the distance between the data point and each centroid.
4. the data point gets assigned to the cluster of the closest centroid.
5. after each data point being assigned to a cluster we update the centroids to be now located at the mean position of the cluster that is associated with that centroid.
6. repeat until cluster centroids become stable (or other criteria).

## the task

your goal is the implement the K-means clustering algorithm and run it with three clusters (`K=3`) on the two features with `sepal_length` and `sepal_width`.

specifically, you task is to define a function called `kmeans_clustering` that takes as input a the data to be clustered and the number of clusters you want to have at the end. within the function you implement the algorithm described above. at the end the function should return the two variables `k_labels` represententing the cluster each point is assigned to. this means that this variable should have the same number of elements as the data and each element is one integer that represent one of the clusters. the second variable that should be returned by the function is `k_centroids` which represents the coordinates (locations) of the centers of the clusters. this means that we have K=3, then there will be 3 points each having two values representing the two features of sepal_length and sepal_width. to calculate the distance between a data point and each centroid you may (but you don't have to) use the function in the cell below.
