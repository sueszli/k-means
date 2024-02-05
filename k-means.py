from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

import os
import unittest


def get_dataset():
    iris = datasets.load_iris()
    sepal_length = iris.data[:, 0]  # type: ignore
    sepal_width = iris.data[:, 1]  # type: ignore
    data = np.array(list(zip(sepal_length, sepal_width)))

    k = len(iris.target_names)  # type: ignore
    return data, k


def get_next_centroids(data: np.ndarray, centr: np.ndarray):
    # d2c[i]=j means data[i] is closest to centr[j]
    d2c = np.zeros(data.shape[0], dtype=int) - 1
    for i, d in enumerate(data):
        all_distances = np.linalg.norm(centr - d, axis=1)
        min_distance_index = np.argmin(all_distances)
        d2c[i] = min_distance_index

    # new_centr[j] is the real centroid for all data closest to centr[j]
    new_centr = np.zeros(centr.shape)
    for j in range(centr.shape[0]):
        group = data[d2c == j]
        if not len(group) > 0:
            continue
        new_centr[j] = np.mean(group, axis=0)

    return d2c, new_centr


class TestCases(unittest.TestCase):
    # https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1
    # run with: unittest.main()
    # compare against `sklearn.cluster.KMeans`
    def test_1(self):
        self.assertTrue(True)


if __name__ == "__main__":
    # clear screen
    os.system("cls" if os.name == "nt" else "clear")

    data, k = get_dataset()
    old_centr = data[np.random.choice(data.shape[0], k, replace=False)]  # forgy method for initialization

    d2c, new_centr = get_next_centroids(data, old_centr)

    # max_iterations = 1
    # for iter in range(max_iterations):
    #     new_centr = get_next_centroids(data, centr)
    #     has_converged = np.array_equal(centr, new_centr)
    #     if has_converged:
    #         break
    #     centr = new_centr
