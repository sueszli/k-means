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

<br><br>

_k-means:_

- unsupervised learning: no labels.
- partitioning clustering: each sample is assigned to one cluster, without overlapping.
- np-hard problem: no known polynomial time algorithm, but we try to approximate it through iterative refinement.
- dataset: scikit-learn's iris dataset with 3 species (therefore $k=3$).

  beware: a naive k3 implementation with this dataset [usually fails](https://en.m.wikipedia.org/wiki/K-means_clustering#:~:text=the%20result%20often%20fails) but we're doing it anyway out of tradition.

- test: we compare the results with scikit-learn's default k-means implementation.

<br><br>

_algorithm:_

1. select the number of clusters, $k$.

2. place $k$ random vectors in the space of the data points, called "centroids".

   k-means is sensitive to the initial placement of the centroids. the ["forgy method"](https://people.csail.mit.edu/tieu/notebook/kmeans/15_p600-hamerly.pdf) is simple and effective but ["k-means++"](https://en.m.wikipedia.org/wiki/K-means%2B%2B) is the more sophisticated approach.

3. calculate the distance between every data point and centroid (i.e. euclidean distance).

4. assign each data point to the cluster of the closest centroid, forming $k$ clusters.

5. update the position of the centroids. set them to the average position of the data points in the cluster.

6. repeat until the centroids stop moving (or some other criteria).

   avoid local minima by running the algorithm multiple times with different initializations.

<br><br>

_quick install:_

```bash
# clone
git clone https://github.com/sueszli/k-means
cd k-means

# install dependencies
if ! command -v python3 &>/dev/null; then echo "python3 is not installed."; return; fi
if ! command -v pip3 &>/dev/null; then echo "pip3 is not installed."; return; fi
python3 -m pip install --upgrade pip
pip3 install pipreqs && rm -rf requirements.txt && pipreqs .
pip3 install -r requirements.txt

# run
python3 k-means.py
```
