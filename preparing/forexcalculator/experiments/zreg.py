import pandas as pd
import numpy as np
# import warnings
import matplotlib.pyplot as plt

from matplotlib import style
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm, neighbors


from pickle import load, dump
from collections import Counter
from datetime import date

style.use('fivethirtyeight')

if __name__ == "__main__":
    tmp = [1, 2, 2, 3, 4, 5, 6, 7]
    print(tmp[:-2])  # shift df tuong tu
