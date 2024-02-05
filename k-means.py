from sklearn import datasets
from sklearn import cluster

import numpy as np
import matplotlib.pyplot as plt

import os


def get_dataset() -> tuple[np.ndarray, int]:
    iris = datasets.load_iris()
    sepal_length = iris.data[:, 0]  # type: ignore
    sepal_width = iris.data[:, 1]  # type: ignore
    data = np.array(list(zip(sepal_length, sepal_width)))

    k = len(iris.target_names)  # type: ignore
    return data, k


def get_initial_centroids(data: np.ndarray, k: int) -> np.ndarray:
    # forgy method: choose k random data points
    return data[np.random.choice(data.shape[0], k, replace=False)]


def update_centroids(data: np.ndarray, centroids: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # d2c[i]=j means data[i] is closest to centroids[j]
    d2c = np.zeros(data.shape[0], dtype=int) - 1
    for i, d in enumerate(data):
        all_dists = np.linalg.norm(centroids - d, axis=1)
        d2c[i] = np.argmin(all_dists)

    # for each cluster, find their new centroid
    new_centroids = np.zeros(centroids.shape)
    for j in range(centroids.shape[0]):
        data_close_to_j = data[d2c == j]
        if not len(data_close_to_j) > 0:
            continue
        new_centroids[j] = np.mean(data_close_to_j, axis=0)

    return d2c, new_centroids


def log(iter: int, centroids: np.ndarray, new_centroids: np.ndarray) -> None:
    out = f"\033[92miteration {str(iter+1).zfill(2)}:\033[0m "
    centroids_str = ",".join([f"({x:.2f},{y:.2f})" for x, y in centroids])
    new_centroids_str = ",".join([f"({x:.2f},{y:.2f})" for x, y in new_centroids])
    out += f"old=[{centroids_str}], new=[{new_centroids_str}]"
    print(out)


def plot_result(data: np.ndarray, d2c: np.ndarray, centroids: np.ndarray):
    colors = ["r", "g", "b", "y", "c", "m"]
    for i, d in enumerate(data):
        plt.scatter(d[0], d[1], c=colors[d2c[i]])
    for c in centroids:
        plt.scatter(c[0], c[1], c="black", marker="x")
    plt.show()


def run(data: np.ndarray, k: int, max_iterations: int, log_steps=False, plot_res=False):
    # update centroids until convergence
    centroids = get_initial_centroids(data, k)
    d2c = np.zeros(data.shape[0], dtype=int) - 1

    for iter in range(max_iterations):
        d2c, new_centroids = update_centroids(data, centroids)
        has_converged = np.array_equal(centroids, new_centroids)

        log(iter, centroids, new_centroids) if log_steps else None
        if has_converged:
            print(f"converged in {iter+1} iterations") if log_steps else None
            break

        centroids = new_centroids

    plot_result(data, d2c, centroids) if plot_res else None
    return d2c, centroids


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    c_diff = 0
    d_diff = 0

    num_benchmarks = 10
    for _ in range(num_benchmarks):

        # 1. get dataset
        data, k = get_dataset()

        # 2. run lib
        lib = cluster.KMeans(n_clusters=k).fit(data)
        lib_centroids = lib.cluster_centers_
        lib_d2c = lib.labels_
        lib_d2c_grouped = {i: len(lib_d2c[lib_d2c == i]) for i in range(k)}

        # 3. run our implementation
        d2c, centroids = run(data, k, max_iterations=100, log_steps=False, plot_res=False)
        d2c_grouped = {i: len(d2c[d2c == i]) for i in range(k)}

        # 4. compare results
        assert len(lib_centroids) == len(centroids)
        diff = np.linalg.norm(lib_centroids - centroids).round(4)
        print(f"centroid difference: {diff}")
        c_diff += float(diff)

        assert len(lib_d2c) == len(d2c)
        d2c_diff = 0
        for i in range(len(d2c)):
            if d2c[i] != lib_d2c[i]:
                d2c_diff += 1
        print(f"d2c difference: {d2c_diff}\n")
        d_diff += d2c_diff

    print(f"results averaged over {num_benchmarks} benchmarks")
    print(f"\t- \033[92mcentroid difference:\033[0m {c_diff/num_benchmarks}")
    print(f"\t- \033[92md2c difference:\033[0m {d_diff/num_benchmarks}")
