# #######################################################
# ----------------------------------------------------
# The Hunt for Alpha
''' # Reference
# https://www.tutorialspoint.com/forex_trading/index.htm
'''
# ----------------------
''' # FXCM test
import fxcmpy as fy
TOKEN = '4130e29f5b492db7fc81cad1f4602032cab7d2ad'
con = fy.fxcmpy(access_token=TOKEN, log_level='error',
                server='real', log_file='log.txt')
instruments = con.get_instruments()
print(instruments[:5])
'''
# ----------------------
'''
# Time Series Analysis
# https://github.com/topics/financial-analysis
'''

# ----------------------

# Machine Learning: T.B.D

# ---------------------- ----------------------

# global asset managers and quantitative hedge funds.

# ---------------------- ----------------------
'''
# financial data + develop testable systematic trading strategies
# https://campus.datacamp.com/courses/quantitative-risk-management-in-python/risk-and-return-recap?ex=1
# https://github.com/topics/financial-data-science
'''
# ---------------------- ----------------------
'''
# "big data" era.
# https://data-flair.training/blogs/data-science-project-ideas/
# https://learn.datacamp.com/projects
# https://github.com/veb-101/Data-Science-Projects
# https://github.com/firmai/financial-machine-learning

'''

# ---------------------- ----------------------
'''
# financial data: Yahoo Finance, Google Finance, Quandl and DTN IQ Feed
# https://www.datacamp.com/community/tutorials/finance-python-trading
'''

# ---------------------- ----------------------
'''
# quant traders.
# https://blog.quantinsti.com/tag/portfolio-risk-management/
'''
# ---------------------- ----------------------
'''
# risk management/ portfolio construction and algorithmic execution
# https://github.com/topics/financial-analysis?l=python
'''
# ---------------------- ----------------------
'''
# statistical analysis/ rigourous statistical analysis
# https://realpython.com/python-statistics/
# https://scipy-lectures.org/packages/statistics/index.html
# https://www.bigdatavietnam.org/2019/09/statistical-data-analysis-in-python.html
# https://www.datacamp.com/community/tutorials/python-statistics-data-science
'''
# ---------------------- ----------------------

# traditional "frequentist"

# ---------------------- ----------------------

# probability as a measure of belief

# ---------------------- ----------------------
'''
# probability distributions, Bayesian and quantitative trading problems
# https://www.datacamp.com/community/tutorials/probability-distributions-python
# https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
# https://data-flair.training/blogs/python-probability-distributions/
# https://www.kaggle.com/hamelg/python-for-data-22-probability-distributions
'''
# ---------------------- ----------------------
'''
# Time Series Analysis
# https://medium.com/@marcopeixeiro
# https://www.excelr.com/blog/data-science/forecasting/18-time-series-analysis-tactics-that-will-help-you-win-in-2020
'''
# serial correlation, how much of today’s asset prices are correlated to
# previous days’ prices ??? correlation
# interpret the data and predict future values
# R statistical programming environment

# ---------------------- ----------------------
'''
# "data science" and quant ecosystem
# https://www.google.com/search?q=quant+ecosystem&sxsrf=ALeKk02zlFgo8dd1CmafEKKY93qmCfAseA:1624039226097&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjaw7DJ4aHxAhUQCqYKHfvEDwkQ_AUoAXoECAEQAw&biw=960&bih=915
# https://qlib.readthedocs.io/en/latest/
# https://www.quantstart.com/articles/
'''
# ---------------------- ----------------------
'''
# https://machinelearningcoban.com/

# Machine Learning : "learn a model from data".

# ---------------------- ----------------------

# Supervised Learning: an algorithm to detect patterns in data.

# ---------------------- ----------------------

# Unsupervised: harder problem.

# ---------------------- ----------------------

# Reinforcement Learning: outside the scope of the book

# ---------------------- ----------------------

# Machine Learning techniques: SVM, Random Forests,
# complicated relationships between differing sets of financial data
'''

# ---------------------- ----------------------
'''
# Scikit-Learn and Pandas
# https://scikit-learn.org/stable/
# https://pandas.pydata.org/docs/
# https://awesomeopensource.com/projects/scikit-learn
# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# https://www.dataquest.io/blog/sci-kit-learn-tutorial/
'''
# ---------------------- ----------------------

# theoretical:  basics of Bayesian Statistics, Time Series Analysis
# and Machine Learning

# ---------------------- ----------------------

# backtesting of quantitative trading strategies using the QSTrader

# ---------------------- ----------------------

# Bayesian philosophy of statistics, binomial model, Markov Chain Monte Carlo

# ---------------------- ----------------------
'''
# stochastic volatility model: sự biến động ngẫu nhiên
# https://www.google.com/search?q=stochastic+volatility+model&oq=stochastic+volatility&aqs=chrome.1.69i57j0l2j46j0l6.1752j0j7&sourceid=chrome&ie=UTF-8
'''
# ---------------------- ----------------------
'''
# White Noise and the Random Walk
# serial correlation: Autoregressive Integrated Moving Average (ARIMA) models:
# https://www.google.com/search?q=ARIMA+models&sxsrf=ALeKk028xGsr-DoUpqq0mhBSdng_W2WMWg:1621787613081&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj_lNDUneDwAhWLPXAKHZ-wD_kQ_AUoAXoECAEQAw&biw=960&bih=915
'''
# ---------------------- ----------------------
'''
# volatility clustering: phân nhóm biến động
# conditional heteroskedasticity: phương sai thay đổi có điều kiện
# Generalised Autoregressive Conditional Heteroskedastic (GARCH) models:
# https://www.google.com/search?q=garch+model&sxsrf=ALeKk03m2JPGAgoNbrVPLrhH0C-foDA3ng:1621787576568&source=lnms&tbm=isch&sa=X&ved=2ahUKEwigr5vDneDwAhXJ-GEKHUF4DLMQ_AUoAXoECAEQAw&biw=960&bih=915
'''
# ---------------------- ----------------------
'''
# Decision Trees
# https://www.hackerearth.com/practice/machine-learning/machine-learning-algorithms/ml-decision-tree/tutorial/
# https://towardsai.net/p/programming/decision-trees-explained-with-a-practical-example-fe47872d3b53
# https://blog.quantinsti.com/decision-tree/
# https://www.datacamp.com/community/tutorials/decision-tree-classification-python

# Support Vector Machines
# https://www.google.com/search?q=support+vector+machine+financial+forecasting&oq=Support+Vector+Machines+fina&aqs=chrome.2.69i57j0i22i30l4.8469j0j4&sourceid=chrome&ie=UTF-8

# Random Forests:
# https://machinelearningmastery.com/random-forest-for-time-series-forecasting/
# https://www.researchgate.net/publication/328238263_Forecasting_of_Realised_Volatility_with_the_Random_Forests_Algorithm
# https://towardsdatascience.com/example-of-random-forest-application-in-finance-option-pricing-d6ee06356c6e

# K-Means Clustering:
# https://www.quantstart.com/articles/k-means-clustering-of-daily-ohlc-bar-data/
# https://medium.datadriveninvestor.com/stock-market-clustering-with-k-means-clustering-in-python-4bf6bd5bd685
# https://alexandrenesovic.com/2019/11/23/k-means-clustering-an-example-with-financial-data-python/

'''
# ---------------------- ----------------------
'''
# NLP
# https://towardsdatascience.com/nlp-in-the-stock-market-8760d062eb92
# https://github.com/Coldog2333/Financial-NLP

# sentiment analysis then backtesting
# https://algotrading101.com/learn/sentiment-analysis-python-guide/
# https://nickmccullum.com/stock-market-sentiment-analysis-python/
# https://medium.com/voice-tech-podcast/creating-alternative-datasets-for-finance-with-python-scraping-text-mining-and-sentiment-1c505b778ac9
# https://www.kaggle.com/mmmarchetti/sentiment-analysis-on-financial-news
# https://medium.com/analytics-vidhya/using-sentiment-analysis-to-predict-the-stock-market-77100295d753

'''

# ---------------------- ----------------------
'''
# Non-Linear Time Series Methods
# https://www.google.com/search?q=Non-Linear+Time+Series+Methods&sxsrf=ALeKk00G8SSbapGn2tUPJcpBLWns-1YHeA:1621788271641&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjvwtOOoODwAhWLCIgKHU6YBCMQ_AUoAXoECAEQAw&biw=960&bih=915#imgrc=q6NjnKgktUPUWM
# https://stackoverflow.com/questions/51120555/fitting-a-non-linear-univariate-regression-to-time-series-data-in-python
# https://github.com/topics/nonlinear-time-series
# https://towardsdatascience.com/removing-non-linear-trends-from-timeseries-data-b21f7567ed51
# https://www.kaggle.com/philipchan/ws02-non-linear-trend-in-time-series-regression
'''
# ---------------------- ----------------------
'''
# Mathematical Foundations, Calculus, Linear Algebra and Probability
# https://docs.sympy.org/latest/tutorial/calculus.html
# https://numpy.org/doc/stable/reference/routines.linalg.html
'''

# ---------------------- ----------------------
'''

# https://www.khanacademy.org/math/linear-algebra
# https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/
# https://www.khanacademy.org/math/multivariable-calculus
# https://www.khanacademy.org/math/statistics-probability/probability-library
'''

# ---------------------- ----------------------

# Python or R programming
# https://www.youtube.com/watch?v=_V8eKsto3Ug&t=1s

# ---------------------- ----------------------

# backtesting / storing financial data / measuring performance
# how to think in a quantitative fashion /  trading strategies

# ---------------------- ----------------------

# research / improvement

# ---------------------- ----------------------
