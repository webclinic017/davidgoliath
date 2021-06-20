'''
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
'''
# -----------------------------------------------
'''
# Start gpu_test.py
# From http://deeplearning.net/software/theano/tutorial/using_gpu.html#using-gpu
from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

rng = numpy.random.RandomState(22)
x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
f = function([], T.exp(x))
print(f.maker.fgraph.toposort())
t0 = time.time()
for i in range(iters):
    r = f()
t1 = time.time()
print("Looping %d times took %f seconds" % (iters, t1 - t0))
print("Result is %s" % (r,))
if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print('Used the cpu')
else:
    print('Used the gpu')
# End gpu_test.py
'''
# -----------------------------------------------
