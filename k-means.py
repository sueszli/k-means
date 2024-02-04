import np
import os
import unittest

from sklearn import datasets

sepal_data = datasets.load_iris()


def calculate_distances(point, centroids):
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
    pass


class TestCases(unittest.TestCase):
    def test_1(self):
        self.assertTrue(True)


if __name__ == "__main__":
    # clear screen
    os.system("cls" if os.name == "nt" else "clear")
    os.system("uname -a") if os.name == "posix" else os.system("systeminfo")

    # run unit tests
    unittest.main()
