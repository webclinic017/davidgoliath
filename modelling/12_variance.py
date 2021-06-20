# variance calculator python
# https://www.google.com/search?q=variance+calculator+python&oq=variance+calculator+py&aqs=chrome.1.69i57j0j0i22i30.3719j0j7&sourceid=chrome&ie=UTF-8

import numpy as np
from statistics import variance, stdev

results = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439,
           0.53459687, -1.34069996, -1.61042692, -4.03220519, -0.24332097]
# # way 1
# print(np.var(results, ddof=1))
# print(np.std(results, ddof=1))
a = np.array([[1, 2], [3, 4]])
# print(a)
# print(np.var(a))
# print(np.var(a, ddof=1))
# print(np.var(a, axis=0))
# print(np.var(a, axis=1))

# way 2
m = sum(results) / len(results)
var_res = sum((xi-m)**2 for xi in results)/(len(results)-1)
# print(var_res)

# way 3: not need ddof
# print(variance(results))
# print(stdev(results))
