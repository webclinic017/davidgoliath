# -------------------- default template ------------------
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

style.use('fivethirtyeight')
# import scipy as sp

# ------------------ Cointegration --------------
if __name__ == "__main__":
    # cointegrated -> spread converge (hội tụ)
    # co-movements -  co-integrated
    # stationary time series with  a zero mean??? set up a threshold

    # --------------------------
    '''
    # https://machinelearningmastery.com/time-series-data-stationary-python/
    '''
    # # mean not zero
    # df = pd.DataFrame(np.random.randint(0, 100, size=(100, 1)))
    # print(df.describe())

    # --------------------------
    # # mean zero
    # df = pd.DataFrame([-1, -1, 0, 0, 1, 1], columns=['Numbers'])
    # # df = pd.DataFrame([1, 1, 2, 2, 3, -9], columns=['Numbers'])
    # # print(df.describe())
    # df.plot()
    # plt.show()

    # --------------------------
    # set up a threshold T for long/ short position
    # verify I(1)
    '''
    # https://www.pluralsight.com/guides/advanced-time-series-modeling-(arima)-models-in-python
    '''
    # --------------------------
    # Compute the cointegration relationship using OLS, saving residuals
    '''
    # https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.coint.html
    '''
    # --------------------------
    # Augmented Dickey-Fuller test
    '''
    # https://arch.readthedocs.io/en/latest/unitroot/unitroot_examples.html
    '''
    # --------------------------
    # if above test fail, construct a model containing only first differences
    '''
    # https://www.youtube.com/watch?v=m_8AsmtxKqs&ab_channel=BenLambert
    '''

    # --------------------------
    # Descriptive statistics
    # 9 most important exchange rates in the world:
    '''
    EUR, JPY, GBP, CHF, SEK, NOK, AUD, NZD, MXN
    natural logarithm:
    # https://stats.stackexchange.com/questions/439386/modelling-exchange-rates-how-to-log-transform-percentage-changes
    '''
    # Unit Root Tests
    '''
    apply to all exchange rates and in first difference.
    '''
    # Test in real pair: USD/EUR vs USD/GBP
    '''
    # check regime crisis period
    # Estimate Equation using Least Square method: [log]
    # calculate Residuals
    # https://quantcorner.wordpress.com/2015/10/05/reading-eviews-workfiles-with-python/
    # potential mean reversion: compare ADF test with 5% critical value
    deviations from 'equilibrium value'
    plot the spreads (or residuals) and define entry/exit levels
    define the time series of the residuals formula (alpha & beta)
    '''
    # Engle-Granger
    '''
    # https://www.youtube.com/watch?v=b4oQfwZ2SNU&ab_channel=AnEcCenterforEconometricsResearch
    # 'static or stochastic signal'/ stochastic/time-varying or static bands
    # long/ short spread ~ long/ short pair
    '''
    # Johansen test:
    '''
    1. Trace
    2. Maximum Eigenvalue
    3. Critical Value and Prob
    '''

    # Hurst exponent
    '''
    1. compare H exponent to 0.5 -> mean reverting or trending
    2. speed of diffusion
    3. log(prices) vs time lag (arbitrary) - Brownian Motion
    4. When exit the trade (read Half life of Mean Reversion)
    '''

    pass
# ------------------ end Cointegration ----------
# ------------------ end default template -----------------
