# expected value calculator: mean
# https://www.google.com/search?q=expected+value+calculator+probability+python+numpy&sxsrf=ALeKk00GFwY68lWZuvrZjUtFhbfa3qwbDQ%3A1621249001306&ei=6UuiYJqbEv-Sr7wPidubwAc&oq=expected+value+calculator+probability+python+numpy&gs_lcp=Cgdnd3Mtd2l6EAMyBwghEAoQoAE6BwgAEEcQsAM6CAghEBYQHRAeOgUIIRCgAVCvjQFYv5cBYMmYAWgBcAJ4AIAB2QGIAf4HkgEFMC41LjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwjas8KWx9DwAhV_yYsBHYntBngQ4dUDCA4&uact=5
import numpy as np
from statistics import mean, variance, stdev

arr = np.random.random_integers(1, 5, 10)
a = [14, 8, 11, 10, 7, 9, 10, 11, 10, 15, 5, 10]
# print(np.mean(a))
# print(mean(a))

# arr = np.array([4, 1, 3, 2, 1, 4, 3, 1, 4, 5])
# print(np.mean(arr))
# print(np.var(arr, ddof=1))
# print(np.std(arr, ddof=1))

# 2 cái này khác nhau --------------------
arr = list(arr)
# print(arr)
# arr = [4, 1, 3, 2, 1, 4, 3, 1, 4, 5]
# print(mean(arr))
# print(variance(arr))
# print(stdev(arr))
