# -------------------- default template ------------------
import itertools

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style
style.use('fivethirtyeight')
# import scipy as sp

if __name__ == "__main__":
    np.random.seed(1)
    samples = 100
    mu = [(7, 5), (8, 12), (1, 10)]
    cov = [
        [[0.5, 0], [0, 1.0]],
        [[2.0, 0], [0, 3.5]],
        [[3, 0], [0, 5]],
    ]

    norm_dists = [np.random.multivariate_normal(
        m, c, samples) for m, c in zip(mu, cov)]
    X = np.array(list(itertools.chain(*norm_dists)))

    km3 = KMeans(n_clusters=3)
    km3.fit(X)
    km3_labels = km3.labels_

    km4 = KMeans(n_clusters=4)
    km4.fit(X)
    km4_labels = km4.labels_

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    ax1.scatter(X[:, 0], X[:, 1], c=km3_labels.astype(np.float))
    ax1.set_xlabel("$x_1$")
    ax1.set_ylabel("$x_2$")
    ax1.set_title("K-Means with $k=3$")
    ax2.scatter(X[:, 0], X[:, 1], c=km4_labels.astype(np.float))
    ax2.set_xlabel("$x_1$")
    ax2.set_ylabel("$x_2$")
    ax2.set_title("K-Means with $k=4$")
    plt.show()
# ------------------ end default template -----------------
