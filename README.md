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
