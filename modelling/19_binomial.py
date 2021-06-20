# binomial distribution python 'IMPORTANT'
# https://www.google.com/search?q=binomial+distribution+python&oq=Binomial+distribution+python&aqs=chrome.0.0i67j0l4j0i22i30l5.1894j0j4&sourceid=chrome&ie=UTF-8

''' Discrete Distribution
binary scenarios, e.g. toss of a coin, it will either be head or tails

It has three parameters:
n - number of trials.

p - probability of occurence of each trial
(e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.
'''
# w3schools part -----------------------------------
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom
import numpy as np

# x = random.binomial(n=100, p=0.5, size=1000)

# # what param purpose
# y = random.normal(loc=50, scale=5, size=1000)
# # sns.distplot(x, hist=True, kde=False, label='binomial')
# sns.distplot(x, hist=False, label='binomial')
# # Between Normal and Binomial Distribution
# sns.distplot(y, hist=False, label='normal')
# plt.show()

# numpy part -----------------------------------
n, p = 10, .5
# # Draw samples from a binomial distribution
# print(random.binomial(n, p, 1000))
'''
A real world example. A company drills 9 wild-cat
oil exploration wells, each with an estimated probability
of success of 0.1. All nine wells fail. What is the probability
of that happening?

Let’s do 20,000 trials of the model, and count the number that
generate zero positive results.
'''
n, p, t = 9, 0.1, 20000
# p = sum(random.binomial(n, p, t) == 0)/20000
# print(f'The probability is around {p*100} %')

# geeksforgeeks part -----------------------------------
'''
a probability distribution

variable will take one of two independent values

distribution is obtained by Bernoulli trials:
    Only 2 possible outcomes
    Each outcome has a fixed probability of occurring
    Each trial is completely independent of all others
    This distribution has a mean equal to np and a variance of np(1-p)

obtain the probability mass function

'''
# for dice rolling Eg:
n = 6
p = 0.5
r_values = list(range(n+1))
mean, var = binom.stats(n, p)
dist = [binom.pmf(r, n, p) for r in r_values]

# # printing values ---------------------
# print('r\tp(r)')
# for i in range(n+1):
#     print(str(r_values[i])+'\t'+str(dist[i]))
# print(f'mean: {mean}')
# print(f'variance: {var}')

# # ploting values ---------------------
# plt.bar(r_values, dist)
# plt.show()

# scipy part -----------------------------------
fig, ax = plt.subplots(1, 1)

# Calculate
n, p = 5, 0.4
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
''' PPF vs CDF:
https://stackoverflow.com/questions/65468026/norm-ppf-vs-norm-cdf-in-pythons-scipy-stats

PPF (percent point func): find the median of a distribution
(which the random variable X can take any value is continuous
random variable)

CDF (cumulative distribution function):
(variable takes a value less than or equal to x)

PMF (probability mass function):
'''

# Display the pmf
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)

# freeze the distribution and display the frozen pmf
rv = binom(n, p)  # rv = Random variates
ax.vlines(x, 0, rv.pmf(x), colors='k',
          linestyles='-', lw=1, label='frozen pmf')
ax.legend(loc='best', frameon=False)

# Check accuracy
prob = binom.cdf(x, n, p)
# print(np.allclose(x, binom.ppf(prob, n, p)))
# print(binom.rvs(n, p, size=100))

# plotting
plt.show()
