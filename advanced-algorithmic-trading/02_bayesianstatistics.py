"""
# import numba as nb
# import numpy as np
# import scipy as sp
# -----------------------------------------------------
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.bayes_mvs.html
from scipy import stats
import matplotlib.pyplot as plt

# # ----------- it sample -----------
# data = [6, 9, 12, 7, 8, 8, 13]
# mean, var, std = stats.bayes_mvs(data)

# print(f'mean: {mean} | var: {var} | std: {std}')


# ----------- nhieu samples -----------
n_samples = 100000
data = stats.norm.rvs(size=n_samples)
# print(data)

# 95% confidence intervals : Khoảng tin cậy
res_mean, res_var, res_std = stats.bayes_mvs(data, alpha=0.95)
# print(f'mean: {res_mean} | var: {res_var} | std: {res_std}')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(data, bins=100, density=True, label='Histogram of data')
ax.vlines(res_mean.statistic, 0, 0.5, colors='r', label='Estimated mean')
ax.axvspan(res_mean.minmax[0], res_mean.minmax[1], facecolor='r',
           alpha=0.2, label=r'Estimated mean (95% limits)')
ax.vlines(res_std.statistic, 0, 0.5, colors='g', label='Estimated scale')
ax.axvspan(res_std.minmax[0], res_std.minmax[1], facecolor='g',
           alpha=0.2, label=r'Estimated scale (95% limits)')
ax.legend(fontsize=10)
ax.set_xlim([-4, 4])
ax.set_ylim([0, 0.5])
plt.show()
"""
# ------------------ Theorem --------------------------
# Classical, or Frequentist vs Bayesian

# Bayesian : applying probability to statistical problems
# Bayesian : new data or evidence / hypothesis

# Frequentist statistics assumes that probabilities are the
# long-run frequency of random
# events in repeated trials.

# Coin flips (Frequentist) vs Election of a particular candidate
#  for UK Prime Minister (Bayesian)

# different opinions and  separate differing prior BELIEFS (Bayesian)

# weighted (0-1) / no chance (0) / always occuring (1)

# biases / impossible or merely very difficult: Black swan -
# Barings Bank - Long-Term Capital Management - Lehman Brothers
# -> very low probability vs zero("impossible" chances)

# --------------------------
# conditional probability: What is the probability of rain (A)
# occuring given that there are clouds in the sky (B) -> P(A|B)

# probability of A occuring given that B has occured =
# probability that they have both occured / probability that B has occured

# What is the probability of seeing clouds, given that it is raining? P(B|A)

# P(A|B) = P(A^B)/P(B) and P(B|A) = P(B^A)/P(A)
# P(A^B) = P(B^A) -> P(B)*P(A|B) = P(A)*P(B|A)
# -> P(A|B) = (P(A)*P(B|A)) / P(B) = (P(A)*P(B|A)) / SUM sigma((P(A)*P(B|A)))

# -------------------------- Bayesian IDEA
# continually update our prior beliefs when new data/ evidence  occur
# Bernoulli Trial: random experiment with only two outcomes: success vs failure

# o : prior. strength in belief without considering the evidence(D)
# Our prior view on the probability of how fair the coin is (1/2)

# o|D : posterior. (refined) strength of our belief when evidence(D) occur
# After seeing 4 heads out of 8 flips, say, this is our updated
# view on the fairness of the coin (1/3)

# D|o : likelihood. probability of seeing the data D. If we knew the coin
# was fair (1/2), this tells us the "probability" of seeing
# a number of "heads" ..(AFTER).. in a particular number of "flips.""

# D : evidence. probability of the data. summing all possible values

# P(o|D) = P(D|o)*P(o) / P(D)
# -> update posterior from beliefs, evidence
# -> repeatedly adjust beliefs under new data

# -------------------------- Coin-Flipping Example
# multiple coin-flips of a coin with unknown fairness.

# uniform distribution: Phân phối đồng đều
# khac vs Beta distribution: binomial model - mô hình nhị thức -
# flexible in modelling beliefs.

# probability density function: hàm mật độ xác suất

# -------------------------- Coding beta_binomial

"""
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt


if __name__ == "__main__":
    # Create a list of the number of coin tosses ("Bernoulli trials")
    number_of_trial = [0, 2, 10, 20, 50, 500]
    # Conduct 500 coin tosses and output into a list of 0s and 1s
    # where 0 represents a tail and 1 represents a head

    # what the fuck?? [-1]
    # print(number_of_trial[-1])
    data = stats.bernoulli.rvs(0.5, size=number_of_trial[-1])

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

        # what the fuck
        y = stats.beta.pdf(x, 1+heads, 1+N-heads)
        plt.plot(x, y, label=f'observe {N} tosses,\n{heads} heads')
        # what the fuck
        plt.fill_between(x, 0, y, color="#aaaadd", alpha=0.5)
    plt.tight_layout()
    plt.show()
"""
# ------------------------------------------------------------------
'''
# remember: Bayesian confidence intervals for the mean, var, and std
# Input data Requires data points and Probability

# mean, var, and std : mean, variance, and standard deviation
# mean of pdf: Probability distribution function,

# mvsdist: mean, var, and std distribution
from scipy import stats
from randintpr import *
import matplotlib.pyplot as plt


data = generate_intlist(7, 20)
mean, var, std = stats.bayes_mvs(data)
# a tuple
# print(stats.bayes_mvs(data))

# generate new input data
n_samples = 100000
data = stats.norm.rvs(size=n_samples)
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
'''
# ------------------------------------------------------------------
# Coin-Flipping Example ...
# prior. posterior. likelihood. evidence.
