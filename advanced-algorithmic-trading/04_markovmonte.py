import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pymc3


if __name__ == '__main__':
    plt.style.use("ggplot")
    n = 50
    z = 10

    # what are these params
    alpha = 12
    beta = 12
    alpha_post = 22
    beta_post = 52

    # iterations = 100000
    iterations = 100
    basic_model = pymc3.Model()
    with basic_model:
        # Define "conjugate prior" belief about the fairness
        theta = pymc3.Beta("theta", alpha=alpha, beta=beta)

        # Define the Bernoulli likelihood function
        y = pymc3.Binomial("y", n=n, p=theta, observed=z)

        # Use Maximum A Posteriori optimisation as initial value for MCMC
        start = pymc3.find_MAP()    # ???

        # Use the Metropolis algorithm
        step = pymc3.Metropolis()

        # Calculate the trace
        trace = pymc3.sample(iterations, step, start,
                             random_seed=1, progressbar=True)

        # Plot the posterior histogram from MCMC analysis
        plt.hist(trace["theta"], bins=50, histtype="step",
                 density=True, label="Posterior (MCMC)", color="red")

        # Plot the analytic prior and posterior beta distributions
        x = np.linspace(0, 1, 100)

        plt.plot(x, stats.beta.pdf(x, alpha, beta),
                 "--", label="Prior", color="blue")

        plt.plot(x, stats.beta.pdf(x, alpha_post, beta_post),
                 label='Posterior(Analytic)', color="green")

        # Update the graph labels
        plt.legend(title="Parameters", loc="best")
        plt.xlabel("$\\theta$, Fairness")
        plt.ylabel("Density")
        # traceplot method to plot kernel density estimate (KDE) and trace
        pymc3.traceplot(trace)
        plt.show()
# -------------------------------------------------------------------------
# Markov Chain Monte Carlo (MCMC)

# suy luận tỉ lệ nhị thức dựa vào prior liên hợp
# tuy nhiên ko phải tất cả model có thể dùng liên hợp
# bây giờ tính phân phối posterior bằng sấp xỉ (posterior là output cuối cùng)

# MCMC giúp ta tính xấp xỉ dựa trên định lý bayes
# với các thuật toán: Metropolis Algorithm, Metropolis-Hastings,
# Gibbs Samplers, Hamiltonian Monte Carlo, No-U-Turn Sampler (NUTS)

# using PyMC3
# from Bayesian Statistics theory to quantitative trading strategies
# models derived from Bayesian

# MCMC use when conjugate priors are not applicable
# more sophisticated, more complex models
# build trading model

# không phải tất cả các mô hình đều có thể được
# phát biểu một cách ngắn gọn dưới dạng liên hợp
# Eg: mô hình phân cấp với hàng trăm tham số

# 1. calculate the evidence
# 2. evaluate integral (tích phân)
# 3. ko tính đc tích phân thì chơi xấp xỉ số
# 4. nhiều tham số hơn, prior distributions có thể có nhiều chiều hơn
# 5. dẫn tới posterior distributions cũng sẽ có nhiều chiều
# 6. khối lượng dữ liệu trong không gian phải phát triển theo cấp số nhân
# với số chiều.
# 7. MCMC kiếm soát đc vấn đề nhờ việc tìm kiếm thông minh trong
# không gian nhiều chiều
# 8. sample posterior distribution combining a "random search"
# 9. Search with intelligent jumps (memoryless searches) doesn’t depend
# on where we started
# 10. xấp xỉ đc tích phân nhiều chiều

# Markov Chain Monte Carlo là một nhóm các thuật toán
# 1. Begin the algorithm at the current position in parameter space (o)
# 2. "jump" to a new position in parameter space
# 3. Accept or reject the jump probabilistically using the prior
# information and available data
# 4. If the jump is accepted, move to the new position and return to step 1
# 5. If the jump is rejected, stay where you are and return to step 1
# 6. After a set number of jumps have occurred, return
# "all of the accepted positions"

# ??? how you jump as well as how you decide whether to jump (parameter space)
# using normal distribution to propose a jump
# normal distribution has u mean and "proposal width" std

# quick convergence, large width->jump more space in posterior distribution but
# might initially miss a region of higher probability

# smaller width will not cover much of the space and could take longer
#  to converge

# https://en.wikipedia.org/wiki/Continuous_or_discrete_variable

# proposal distribution, jump , new position, current position,
# probability of moving p

# tạo ra một số ngẫu nhiên trên khoảng [0, 1],  nếu nó nằm trong [1, p]
# -> accept moving

# sampling problem: áp cthuc Bayes vào để bỏ đi phần P evidence (page 58)

# closed-form solution???
