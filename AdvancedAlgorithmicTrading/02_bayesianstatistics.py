import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from randintpr import *

if __name__ == "__main__":
    # # 6 charts
    # trial_num = [0, 2, 10, 20, 50, 500]
    # # 0 present tail, 1 present head
    # data = stats.bernoulli.rvs(0.5, size=trial_num[-1])
    # x = np.linspace(0, 1, 100)
    # for i, N in enumerate(trial_num):
    #     head = data[:N].sum()
    #     ax = plt.subplot(len(trial_num)/2, 2, i+1)
    #     ax.set_title(f'{N} trials, {head} heads')
    #     plt.xlabel('$P(H)$, Probability of heads')
    #     plt.ylabel('Density')
    #     # ?? purpose
    #     if i == 0:
    #         plt.ylim([0.0, 2.0])
    #     plt.setp(ax.get_yticklabels(), visible=False)
    #     y = stats.beta.pdf(x, 1+head, 1+N-head)
    #     plt.plot(x, y, label=f'observe {N} tosses,\n{head} heads')
    #     plt.fill_between(x, 0, y, color="#aaaadd", alpha=0.8)
    # plt.tight_layout()
    # plt.show()
    # pass
    # ------------------------------------------------------------
    # data = generate_list(7, 20)
    # mean, var, std = stats.bayes_mvs(list(data))

    # generate new input data
    n_samples = 100000
    data = stats.norm.rvs(size=n_samples)
    # data = stats.bernoulli.rvs(0.75, size=n_samples)

    res_mean, res_var, res_std = stats.bayes_mvs(data, alpha=0.95)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # bins càng lớn histogram càng dày, density -> phải có, label for legend
    ax.hist(data, bins=100, density=True, label='Histogram of data')
    # Plot vertical lines: (0, 0.5) len from ... to
    ax.vlines(res_mean.statistic, 0, 0.5, color='r', label='Estimated mean')
    ax.axvspan(res_mean.minmax[0], res_mean.minmax[1], facecolor='r',
               alpha=0.2)  # , label=r'Estimated mean (95% limits)'
    ax.vlines(res_std.statistic, 0, 0.5, colors='g', label='Estimated scale')
    ax.axvspan(res_std.minmax[0], res_std.minmax[1], facecolor='g',
               alpha=0.2)  # , label=r'Estimated scale (95% limits)'
    ax.legend(fontsize=10)
    ax.set_xlim([-4, 4])
    ax.set_ylim([0, 0.5])
    plt.show()
