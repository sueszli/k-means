```
┌─────────────────────────────────────────────┐
| can someone please tell me what 'k' means?  |
└─────────────────────────────────────────────┘
    \
     \
      \       _.-.
         __.-' ,  \
        '--'-'._   \
                '.  \
                 )-- \ __.--._
                /   .'        '--.
               .               _/-._
               :       ____._/   _-'
               '._          _.'-'
                  '-._    _.'
                      \_|/
                     __|||
                     >__/'
```

k-means clustering is an unsupervised learning algorithm, meaning it works with unlabeled data. it's a partitioning clustering method where each data point definitively belongs to a single cluster. finding the optimal solution in k-means is an np-hard problem, so we use iterative refinement to get a good approximation. for this example, we'll use the classic iris dataset, even though naive implementations of k-means often fail due to the dataset's characteristics. since the iris dataset has three flower species, we'll aim for three clusters (k=3). finally, we'll compare our results to the standard k-means implementation in scikit-learn.

_algorithm:_

1. select the number of clusters, $k$.

2. place $k$ random vectors in the space of the data points, called "centroids".

   k-means is sensitive to the initial placement of the centroids. the ["forgy method"](https://people.csail.mit.edu/tieu/notebook/kmeans/15_p600-hamerly.pdf) is simple and effective but ["k-means++"](https://en.m.wikipedia.org/wiki/K-means%2B%2B) is the more sophisticated approach.

3. calculate the distance between every data point and centroid (i.e. euclidean distance).

4. assign each data point to the cluster of the closest centroid, forming $k$ clusters.

5. update the position of the centroids. set them to the average position of the data points in the cluster.

6. repeat until the centroids stop moving (or some other criteria).

   avoid local minima by running the algorithm multiple times with different initializations.
