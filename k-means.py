import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

import os
import unittest

from sklearn import datasets


# https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1

sepal_data = datasets.load_iris()
# sepal_length =
# sepal_width =


def calculate_distances(point, centroids):
    # two features `sepal_length` and `sepal_width`

    # takes as input a the data to be clustered and the number of clusters you want to have at the end.
    """
    Calculate the Euclidean distances between a point and a list of centroids.

    Parameters:
    - point (numpy.ndarray): A numpy array representing the coordinates of a point.
    - centroids (numpy.ndarray): A numpy array representing the coordinates of the centroids.

    Returns:
    - distances (numpy.ndarray): A numpy array containing the Euclidean distances between the point and each centroid.

    This function computes the Euclidean distance between the given point and each centroid in the set of centroids.
    The Euclidean distance between two points in n-dimensional space is defined as the square root of the sum of the squared differences between the corresponding coordinates of the points.
    """
    # return np.sqrt((point - centroids) ** 2).sum(axis=1)

    # at the end the function should return the two variables `k_labels` represententing the cluster each point is assigned to. this means that this variable should have the same number of elements as the data and each element is one integer that represent one of the clusters. the second variable that should be returned by the function is `k_centroids` which represents the coordinates (locations) of the centers of the clusters. this means that we have K=3, then there will be 3 points each having two values representing the two features of sepal_length and sepal_width. to calculate the distance between a data point and each centroid you may (but you don't have to) use the function in the cell below.

    pass


class TestCases(unittest.TestCase):
    def test_1(self):
        self.assertTrue(True)


if __name__ == "__main__":
    # clear screen
    os.system("cls" if os.name == "nt" else "clear")
    os.system("uname -a") if os.name == "posix" else os.system("systeminfo")

    k = 3

    # forgy method: pick random data points as initial centroids

    # run unit tests
    unittest.main()
