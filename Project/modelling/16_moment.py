# moment statistics python  'IMPORTANT'
# https://www.google.com/search?q=moment+statistics+python&sxsrf=ALeKk03IR29YXksd2BrmuqG_1yKbLknFXQ%3A1621251343715&ei=D1WiYJT0Ko2ImAWc-6uwBg&oq=moment+statistics+python&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjoHCAAQRxCwAzoHCAAQsAMQQzoCCABQxDhYv0JgjERoAXACeACAAZ8CiAGsC5IBBTAuNi4ymAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwjUt7vzz9DwAhUNBKYKHZz9CmYQ4dUDCA4&uact=5
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.moment.html
# https://math.stackexchange.com/questions/190531/what-is-the-use-of-moments-in-statistics

'''
What do moments represent?
Moments [of a statistical distribution]

1. The mean, which indicates the central tendency of a distribution.

2. The second moment is the variance, which indicates the width or deviation.

3. The third moment is the skewness, which indicates any asymmetric 'leaning'
to either left or right.
'''
from scipy import stats
import numpy as np

arr = np.random.randint(1, 10, 10)
arr = list(arr)
print(arr)
print(stats.moment(arr, moment=1))  # ???
print(stats.moment(arr, moment=2))

# print(stats.moment(arr, moment=3))
# print(stats.skew(arr))
