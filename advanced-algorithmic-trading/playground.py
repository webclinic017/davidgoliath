import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


if __name__ == "__main__":
    number_of_trails = [0, 10, 20, 40, 80, 160, 320, 640]
    data = stats.bernoulli.rvs(0.5, size=number_of_trails[-1])
    # print(data)
    x = np.linspace(0, 1, 100)

    for i, N in enumerate(number_of_trails):
        heads = data[:N].sum()
        ax = plt.subplot(len(number_of_trails) / 2, 2, i + 1)
        ax.set_title("%s trials, %s heads" % (N, heads))

        plt.xlabel("$P(H)$, Probability of Heads")
        plt.ylabel("Density")
        if i == 0:
            plt.ylim([0.0, 2.0])
        plt.setp(ax.get_yticklabels(), visible=False)
        y = stats.beta.pdf(x, 1 + heads, 1 + N - heads)
        plt.plot(x, y, label="observe %d tosses,\n %d heads" % (N, heads))
        plt.fill_between(x, 0, y, color="#aaaadd", alpha=0.5)
    plt.tight_layout()
    plt.show()
