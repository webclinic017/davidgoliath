import numpy as np
import scipy as sp
from scipy import stats
from matplotlib import pyplot as plt
from randintpr import *

# # -----------------------------------------------------
# # # ----------- it sample -----------
# # data = [6, 9, 12, 7, 8, 8, 13]
# # mean, var, std = stats.bayes_mvs(data)

# # print(f'mean: {mean} | var: {var} | std: {std}')


# # ----------- nhieu samples -----------
# n_samples = 100000
# data = stats.norm.rvs(size=n_samples)
# # print(data)

# # 95% confidence intervals : Khoảng tin cậy
# res_mean, res_var, res_std = stats.bayes_mvs(data, alpha=0.95)
# # print(f'mean: {res_mean} | var: {res_var} | std: {res_std}')
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.hist(data, bins=100, density=True, label='Histogram of data')
# ax.vlines(res_mean.statistic, 0, 0.5, colors='r', label='Estimated mean')
# ax.axvspan(res_mean.minmax[0], res_mean.minmax[1], facecolor='r',
#            alpha=0.2, label=r'Estimated mean (95% limits)')
# ax.vlines(res_std.statistic, 0, 0.5, colors='g', label='Estimated scale')
# ax.axvspan(res_std.minmax[0], res_std.minmax[1], facecolor='g',
#            alpha=0.2, label=r'Estimated scale (95% limits)')
# ax.legend(fontsize=10)
# ax.set_xlim([-4, 4])
# ax.set_ylim([0, 0.5])
# plt.show()
# -------------------------- Coding beta_binomial
'''

if __name__ == "__main__":
    # Create a list of the number of coin tosses ("Bernoulli trials")
    number_of_trial = [0, 2, 10, 20, 50, 500]
    # Conduct 500 coin tosses and output into a list of 0s and 1s
    # where 0 represents a tail and 1 represents a head

    # what the fuck?? [-1]
    # print(number_of_trial[-1])
    # Generate random variates: SAMPLING
    data = stats.bernoulli.rvs(0.75, size=number_of_trial[-1])
    # <class 'numpy.ndarray'>
    # print(type(data))

    # Discretise the x-axis into 100 separate plotting points
    x = np.linspace(0, 1, 100)

    for i, N in enumerate(number_of_trial):
        # print(str(i) + " " + str(N))
        # sum all element
        heads = data[:N].sum()

        # print(data[:N])
        # print(heads)

        ax = plt.subplot(len(number_of_trial)/2, 2, i+1)
        ax.set_title(f'{N} trials, {heads} heads')

        plt.xlabel('$P(H)$, Probability of heads')
        plt.ylabel('Density')
        if i == 0:
            plt.ylim([0.0, 2.0])
        # what the fuck
        plt.setp(ax.get_yticklabels(), visible=False)

        # likelihood function
        y = stats.beta.pdf(x, 1+heads, 1+N-heads)
        plt.plot(x, y, label=f'observe {N} tosses,\n{heads} heads')
        # fill color area
        plt.fill_between(x, 0, y, color="#aaaadd", alpha=0.8)
    plt.tight_layout()
    plt.show()
'''
# ------------------------------ Code
data = generate_intlist(7, 20)
mean, var, std = stats.bayes_mvs(data)
# a tuple
# print(stats.bayes_mvs(data))

# generate new input data
n_samples = 100000
data = stats.norm.rvs(size=n_samples)
# data = stats.bernoulli.rvs(0.75, size=n_samples)
# print(len(data))

res_mean, res_var, res_std = stats.bayes_mvs(data, alpha=0.95)
# print(stats.bayes_mvs(data, alpha=0.95))
fig = plt.figure()
ax = fig.add_subplot(111)
# bins càng lớn histogram càng dày, density -> phải có, label dành cho legend
ax.hist(data, bins=100, density=True, label='Histogram of data')
# Plot vertical lines: (0, 0.5) len from ... to
ax.vlines(res_mean.statistic, 0, 0.5, color='r', label='Estimated mean')
ax.axvspan(res_mean.minmax[0], res_mean.minmax[1], facecolor='r',
           alpha=0.2, label=r'Estimated mean (95% limits)')
ax.vlines(res_std.statistic, 0, 0.5, colors='g', label='Estimated scale')
ax.axvspan(res_std.minmax[0], res_std.minmax[1], facecolor='g',
           alpha=0.2, label=r'Estimated scale (95% limits)')
ax.legend(fontsize=10)
ax.set_xlim([-4, 4])
ax.set_ylim([0, 0.5])
plt.show()
# ------------------------------------------------------------------
# Coin-Flipping Example ...
# prior. posterior. likelihood. evidence.
