from statistics import mean, median, stdev, mode, variance
import random
import numpy as np
from scipy.stats import iqr, norm, zscore
from statsmodels import robust
import pandas as pd
from math import ceil, floor
# import duka
# import subprocess

# # https://blog.darwinex.com/automated-tick-data-collection-r-metatrader/

# pairs = ['EURUSD', 'EURJPY', 'EURCAD', 'EURGBP', 'EURAUD', 'EURNZD',
#          'EURCHF', 'GBPUSD', 'GBPJPY', 'GBPCAD', 'GBPAUD', 'GBPNZD',
#          'GBPCHF', 'AUDUSD', 'AUDNZD', 'AUDJPY', 'AUDCAD', 'AUDCHF',
#          'NZDUSD', 'NZDJPY', 'NZDCAD', 'NZDCHF', 'XAUUSD',
#          'CHFJPY', 'USDJPY', 'USDCHF', 'USDCAD', 'XAGUSD']

# pairs = ['GBPUSD', 'XAUUSD', 'EURUSD']

# for pair in pairs:
#     cmdCommand = f"duka {pair}"  # -s 2021-07-01 -e 2021-08-04 -c H1  -f 0308
#     process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
#     output, error = process.communicate()
#     print(output)

'''
temp = [2.4, 2.8, 3.2]
# print(mean(temp))
# print(median(temp))

temp = [3.9]*4+[4.0]*5
# print(temp)
# print(mean(temp))
# print(median(temp))
# print(stdev(temp))

temp = [random.uniform(3.84, 3.88) for _ in range(13)]
# print(stdev(temp))

temp = [random.randint(113, 117) for _ in range(4)]
# print(mean(temp))
print(stdev(temp))

temp = [random.randint(113, 117) for _ in range(4)]
temp += [random.randint(95, 97) for _ in range(5)]
# print(median(temp))
# print(mean(temp))
print(stdev(temp))

#  for _ in range(2)
temp = [random.randint(113, 117)] + [random.randint(95, 97)]
# print(median(temp))
# print(mean(temp))
print(stdev(temp))
'''
# ---------------------------------------
'''
baylor = [12]*6+[0]*6
mary = [58]+[14]+[0]*10
dartmouth = [5]*4 + [6]*4 + [7]*4
print(mean(baylor), mean(mary), mean(dartmouth))
print(stdev(baylor), stdev(mary), stdev(dartmouth))
print(median(baylor), median(mary), median(dartmouth))
'''
# ---------------------------------------
'''
sam = [random.randint(113, 117) for _ in range(4)]

brook = [random.randint(113, 117) for _ in range(4)]
brook += [random.randint(95, 97) for _ in range(5)]

mary = [random.randint(113, 117)] + [random.randint(95, 97)]
mary2 = [random.randint(113, 117)]*2 + [random.randint(95, 97)]

print(mean(sam), mean(brook), mean(mary))
print(median(sam), median(brook), median(mary))
print(stdev(sam), stdev(brook), stdev(mary))

print(median(mary), median(mary2))
'''
# ---------------------------------------

'''
tmp1 = [0]*4+[1]*2+[2]+[3]*2+[4]*3+[5]*4
tmp2 = [0]+[1]+[2]*2+[3]*4+[4]*3+[5]*1
print(stdev(tmp1), stdev(tmp2))
print(stdev(tmp1)/mean(tmp1), stdev(tmp2)/mean(tmp2))
'''

# ---------------------------------------
'''
tmp = [6, 4, 1, 9, 3, 8, 3, 5, 10]
tmp = [8, 10, 10, 10, 6, 7, 8]
# print(mode(tmp))

tmp = [1, 2, 4, 6, 4]
print(mean(tmp))
tmp = [9, 10, 6, 5, 6]
print(median(tmp))

tmp = [5, 9, 5, 5, 7, 11]
# print(mean(tmp))

tmp = [13, 0, 14, 36, 18, 12]
# tmp.sort()
# print(tmp)
# print(mean(tmp))
# print(median(tmp))

tmp = [711, 533, 664]
# print(mean(tmp))

tmp = [47, 35, 32, 41, 30]
# print(mean(tmp))

tmp = [11, 14, 7, 2, 9, 6, 2]
# tmp.sort()
# print(tmp)

tmp = [1, 2, 2, 3, 5]
tmp = [10, 8, 6, 5, 3, 11]
tmp = [0, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8]
tmp = [3/8, 1, 1/2, 7/8, 3/4]

tmp = [3, 4, 4, 5, 5, 5, 5, 7, 7]
tmp = [8, 14, 18, 6, 8]
tmp = [3, 3, 5, 3]
tmp = [6, 6.8, 3.7, 8.1, 7, 6.6]
tmp = [20, 23, 23, 25, 25, 27, 27, 27, 28]
tmp = [13/3, 11/3, 5, 10/3, 6, 5/3]
tmp = [17, 8, 15, 21, 12]
print(median(tmp))
'''

# ---------------------------------------
'''
cats = [random.randint(147, 159) for _ in range(3)] + [57]
print(median(cats), mean(cats))
cats = [random.randint(147, 159) for _ in range(3)]
print(median(cats), mean(cats))

fixed = [random.randint(30, 40) for _ in range(6)]
cats = fixed + [100]
print(median(cats), mean(cats))
cats = fixed
print(median(cats), mean(cats))

fixed = [random.randint(180, 220) for _ in range(3)]
cats = fixed + [250]
print(median(cats), mean(cats))
cats = fixed + [290]
print(median(cats), mean(cats))

fixed = [random.randint(50, 60) for _ in range(4)]
cats = fixed + [10]
print(median(cats), mean(cats))
cats = fixed
print(median(cats), mean(cats))
'''
# ---------------------------------------


'''
def calc(temp, ret, ran):
    num = 0
    for i in ran:
        tmp = temp + [i]
        if mean(tmp) == ret:
            num = i
            break
    return num


temp = [5, 8, 11, 7]
print(calc(temp, 8, range(20)))
'''
# ---------------------------------------


def calc_iqr(tmp):
    num = int(len(tmp)/2)
    temp1 = tmp[0:num]
    if len(tmp) % 2 == 0:
        temp2 = tmp[num:len(tmp)]
    else:
        temp2 = tmp[num+1:len(tmp)]
    return (median(tmp), median(temp2), median(temp1),
            median(temp2) - median(temp1))


'''

# temp = [0, 1, 1, 3, 3, 3, 4, 5, 7]
# temp = [2.6, 3, 4.9, 5, 5, 6, 6, 7.9, 8, 8.2]
# temp = [0, 0, 0, 1, 2, 2, 2, 2, 2, 3, 4]
# temp = [0, 3/2, 5/2, 3, 4, 4, 4, 7, 15/2]
# temp = [81, 82, 83, 83, 84, 84, 84, 85]
# temp = [0, 0, 0, 1, 2, 2, 4, 5, 7, 8, 10]
# temp = [7, 9, 9, 10, 10, 10, 11, 12, 12, 14]
# temp = [32, 34, 35, 35, 39, 40, 44, 47]
# temp = [43, 44, 44, 44, 45, 45, 47, 48, 48]
# temp = [4, 5, 6, 8, 9, 10, 11, 13]
# temp = [1, 2, 3, 3, 4, 4, 4, 6]
# temp = [1, 1, 3, 4, 4, 5, 5, 5, 6, 7, 9]

# temp = [2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7]
# temp = [25, 28, 29, 29, 30, 34, 35, 35, 37, 38]
# temp = [41, 42, 43, 43, 43, 45, 47, 48, 50, 50]
temp = [0, 0, 0, 1, 1, 3, 3, 4, 7, 7]
print(calc_iqr(temp))
'''
# ---------------------------------------
'''
# temp = [6, 2, 3, 1]
# temp = [31, 33, 36, 41, 34]
# temp = [3, 2, 4, 7]
# temp = [4, 21, 11, 6, 8]
# print(np.std(temp)) # std calc by numpy
'''
# ---------------------------------------
'''
# temp = [22, 13, 18, 16]
# temp = [1, 2, 2, 1, 3, 3]
# temp = [5, 4, 6, 39]
# temp = [7, 10, 15, 21]
# temp = [14, 15, 9, 1]
# temp = [16, 10, 5, 7, 13]
temp = [8, 11, 17, 7, 19]

# "were randomly selected from a small sample"
# Because we only have data for a small sample
# we are only able to "estimate" the population mean and std

# variance
print(np.mean(temp), np.var(temp), np.std(temp))   # var calc by numpy

# "estimated variance"
print(mean(temp), variance(temp), stdev(temp))   # var calc by var
'''
# ---------------------------------------


'''
def mad(data, axis=None):
    return np.mean(np.absolute(data - np.mean(data, axis)), axis)


# temp = [5, 8, 11, 7, 9]
# temp = [0.4, 0.4, 0.2, 0.6]
# temp = [35, 39, 40, 40, 42, 44]
# temp = [3, 7, 4, 2]
temp = [22, 23, 23, 25, 27]

df = pd.Series(temp)
# print(mad(temp))
print(df.mad())
'''
# ---------------------------------------
'''
fixed = [random.randint(50, 60) for _ in range(4)]

fixed = [2, 3, 5, 7, 27, 36, 45, 160]

cats = fixed
print(median(cats), mean(cats))
cats = fixed + [900]
print(median(cats), mean(cats))
'''
# print(median([5, 6, 5, 6, 9]))
# ---------------------------------------


def test(interval, mean_, std_):
    value = mean_ + norm.ppf(interval)*std_
    print(value)


def test2(point, mean_, std_):
    z_score = (point - mean_)/std_
    print(z_score)
    if z_score < -1:
        print(norm.ppf(z_score+1))
    else:
        print(norm.ppf(z_score-1))


#  = 0.4, 80, 9
# test2(45.2, 50.0, 4.0)


# # Probability to z-score and vice versa
# print(norm.cdf(-2.35))   # cumulative distribution below
# print(1-norm.cdf(0.75))   # cumulative distribution above

# # Normal distribution: Area between two points
# print(norm.cdf(1.5) - norm.cdf(-1.5))

# # z-score reverse
# mean_, std_ = 221, 36
# print(mean_ + norm.ppf(0.5)*std_)
