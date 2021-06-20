# Mode (statistics) python 'IMPORTANT', ứng với xác suất
# lớn nhất hoặc hàm mật độ đạt max
# https://www.google.com/search?q=Mode+(statistics)+python&oq=Mode+(statistics)+python&aqs=chrome..69i57j0i22i30j0i10i22i30j0i22i30l2.1901j0j4&sourceid=chrome&ie=UTF-8
import numpy as np
# from statistics import mode

arr = np.random.randint(1, 50, 100)
arr = list(arr)
# print(arr)
print(max(set(arr), key=arr.count))
# print(mode(arr))
