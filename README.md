the K-means clustering algorithm is a simple unsupervised learning algorithm. it receives unlabeled data samples as input and its goal is to cluster them into K groups, based on their similarities / how close they are to each other.

it works by first randomly assigning coordinates (locations) of the centers of clusters (called centroids). then the algorithm goes over each sample in the dataset and calculates the distance between each sample to each centroid. each sample is assigned to the cluster of its closest centroid. then the coordinates of the clusters are updated based on the mean location of the data points that were assigned to the cluster. then we repeat the whole process until the cluster centroids become stable.

1. first, choose an integer value and assign it to the variable K. this variable represents the number of clusters you want to have.
2. randomly choose initial coordinates for the K clusters.
3. for each data point calculate the distance between the data point and each centroid.
4. the data point gets assigned to the cluster of the closest centroid.
5. after each data point is assigned to a cluster we update the centroids to be now located at the mean position of the cluster that is associated with that centroid.
6. repeat until cluster centroids become stable (or other criteria).

```
┌───────────────────────────────────────────────┐
| honestly, i still don't know what k means ... |
└───────────────────────────────────────────────┘
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
