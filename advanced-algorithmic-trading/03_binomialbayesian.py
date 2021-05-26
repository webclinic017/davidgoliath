# ------------------ Theorem --------------------------
# update beliefs about uncertainty as new evidence
# giai thich co so cua - binomial proportion
# probabilistic situations with two outcomes (coin-flip)
# estimate/ predictions the proportion of events. Eg: heads

# ---------------------- ----------------------
# probability rat quan trong
# bird’s eye view
# estimate fairness of a coin

# ---------------------- ----------------------
# 5 techniques:

# 1. Assumptions: two outcomes, randomly, independent trial,
# fairness stationary (fixed)

# 2. Prior Beliefs: quantify fairness -> probability distribution
# and a more flexible distribution named beta distribution

# 3. Experimental Data: hard data, outcomes counting, determining
# the probability, discuss Bernoulli "likelihood function"

# 4. Posterior Beliefs: calculate fairness of the coin and update beliefs
# with the collected data

# 5. Inference: estimate the coin’s fairness(origin=0.5), predict probability
# model comparison, results depend upon choices of prior beliefs

# ---------------------- Assumptions ----------------------
# head or tail
# Matplotlib Seaborn
# independent and identically distributed
# (Các biến ngẫu nhiên độc lập và phân phối giống hệt nhau)

# ---------------------- Bayes’ Rule ----------------------
# calcute the "posterior" from "likelihood", the "prior" and the "evidence"

# ----------------------
# Bernoulli Distribution:
# Bernoulli Likelihood Function for o

# P(k|o) = (o^k)((1 - o)^(1-k))

# ----------------------
# Multiple Flips of the Coin: N flips, z heads

# P(z, N|o) = (o^k)((1 - o)^(N-z)) with o is fairness parameter

# ---------------------- Quantifying our Prior Beliefs ----------------------
# prior beliefs, quantifying =
#       prior beliefs on parameters -> probability distribution

# prior beliefs on the fairness of the coin vs quantify uncertainty biased
# understand the range of values and how each values occur
# o = 0 tail, o = 1 head, fair coin o = 0.5
# probability distribution [0; 1]

# ---------------------- Beta Distribution as prior? ---------------
# Beta Distribution and probability density function(PDF):
# P(o|a, b) = (o^(a-1))((1 - o)^(b-1))/B(a, b)

# --------------- beta distribution ploting ------------------
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # ???
    sns.set_palette("deep", desat=.6)
    sns.set_context(rc={"figure.figsize": (8, 4)})

    x = np.linspace(0, 1, 100)

    # P(o|a, b) = (o^(a-1))((1 - o)^(b-1))/B(a, b)
    # larger a -> probability distribution move to 1, heads more often
    # larger b -> probability distribution move to 0, tails more often
    # both a and b increase -> narrow distribution
    # distribution peak when a and b increase equally

    params = [(0.5, 0.5), (1, 1), (4, 3), (2, 5), (6, 6)]
    for p in params:
        y = beta.pdf(x, p[0], p[1])
        plt.plot(x, y, label=f"$\\alpha={p}$, $\\beta={p}$")
    plt.xlabel("$\\theta$, Fairness")
    plt.ylabel("Density")
    plt.legend(title="Parameters")
    plt.show()
