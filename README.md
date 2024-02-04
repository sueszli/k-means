_"k-means" clustering algorithm:_

- unsupervised learning: no labels
- partitioning clustering: each sample is assigned to one cluster, without overlapping
- dataset: scikit-learn's iris samples

_implementation:_

1. select the number of clusters, $k$.
2. place $k$ random vectors in the space of the data points, called "centroids".
3. calculate the distance between every data point and centroid.
4. assign each data point to the cluster of the closest centroid, forming $k$ clusters.
5. update the position of the centroids. set them to the average position of the data points in the cluster.
6. repeat until the centroids stop moving (or some other criteria).

```
┌──────────────────────────────────────––––───────–––––┐
| honestly, i still don't know what 'k' means ... hehe |
└────────────────────────────────────––──––───────–––––┘
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

<br>

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


<< ////
...
////
```
