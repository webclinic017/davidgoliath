# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *

currency = 'nzd'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild
def calculate_nzbond():
    pass
# https://www.investing.com/rates-bonds/new-zealand-10-years-bond-yield
# https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield

# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/


# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# NZX 50: https://www.investing.com/indices/nzx-50
def get_nzx50():
    pass


# -------------------------------------------------------
# Zxy
# https://www.investing.com/indices/phlx-new-zealand-dollar
def get_zxy():
    get_indices('PHLX New Zealand Dollar', 'united states')
    pass


get_zxy()


# -------------------------------------------------------
# Compare with another interest rate:
# Official cash rate: already have ---- MOST IMPORTANT ----
# FED fund rate: https://fred.stlouisfed.org/series/DFF

# -------------------------------------------------------
# (carry trade) AUD/NZD rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def get_carrytradeindex():
    get_volatility()
    # combine data -> calculate spread ...
    pass


# -------------------------------------------------------
# https://commodity.com/data/new-zealand/
# project to get data from macrotrends
# https://pypi.org/project/finpie/
# -------------------------------------------------------
# ----------------------------IMPORTANT- Nông sản---
# https://www.investing.com/commodities/grains
# https://www.investing.com/commodities/softs
# https://www.investing.com/commodities/meats
# Milk
# butter
# https://futures.tradingcharts.com/chart/BD_/W
# ----------------------------OPTIONAL 1
# Gold price:
def gold_corr():
    pass


# -------------------------------------------------------
def estimate_oil_corr():
    get_wti()
    get_brent()
    # combine data
    # predict
    pass


# -------------------------------------------------------
# AUD vs NZD cùng chạy (correlation)

# -------------------------------------------------------
# Economic calendar and predict index:
# GDP: predict, not real time
# https://www.quandl.com/data/ODA/NZL_NGDPRPC-New-Zealand-GDP-per-Capita-at-Constant-Prices-LCU
def get_gdp():
    get_economic_quandl(currency, 'ODA', 'NZL_NGDPRPC')


# ----------------------------
# Unemployment Rate:
# https://www.quandl.com/data/ODA/NZL_LUR-New-Zealand-Unemployment-Rate-of-Total-Labor-Force
def get_unemploymentrate():
    get_economic_quandl(currency, 'ODA', 'NZL_LUR')


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi():
    get_economic_quandl(currency, 'RATEINF', 'CPI_NZL')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation():
    get_economic_quandl(currency, 'RATEINF', 'INFLATION_NZL')


# ----------------------------
# Employment Change:
# https://fred.stlouisfed.org/series/LREM64TTNZQ156S

# ----------------------------
# Retail sales:
# https://fred.stlouisfed.org/series/SLRTTO01NZQ189N
# ----------------------------
# GDT
# -------------------------------------------------------
