# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *
import usd as king
currency = 'nzd'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild
# https://www.investing.com/rates-bonds/new-zealand-10-years-bond-yield
def calculate_bond(isReload=True):
    if isReload:
        get_bonds('New Zealand 2Y')
        get_bonds('New Zealand 5Y')
        get_bonds('New Zealand 10Y')
    else:
        pass


def calculate_bondspread(isReload=True):
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    pass
# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/


# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# NZX 50: https://www.investing.com/indices/nzx-50
def get_nzx50(isReload=True):
    if isReload:
        get_indices('NZX 50', 'new zealand')
    pass


# -------------------------------------------------------
# Zxy
# https://www.investing.com/indices/phlx-new-zealand-dollar
def get_zxy(isReload=True):
    # read data instead then analysis
    pass


# nzd pair ------------------------------
def compare_minor(isReload=True):
    if isReload:
        forward_quotes = ['XAU', 'EUR', 'GBP', 'AUD']
        backward_quotes = ['CHF', 'JPY', 'CAD', 'USD']
        if isReload:
            for quote in forward_quotes:
                get_currency_cross(f"{quote}/NZD")
            for quote in backward_quotes:
                get_currency_cross(f"NZD/{quote}")
    else:
        pass


# -------------------------------------------------------
# Compare with another interest rate:
# Official cash rate: already have ---- MOST IMPORTANT ----
# FED fund rate: https://fred.stlouisfed.org/series/DFF
def get_cashrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'OECD', 'KEI_IR3TIB01_NZL_ST_Q')
    # get_ffr()


# -------------------------------------------------------
# (carry trade) AUD/NZD rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def get_carrytradeindex(isReload=True):
    if isReload:
        get_volatility()
    # combine data -> calculate spread ...
    pass


# -------------------------------------------------------
# https://commodity.com/data/new-zealand/
# project to get data from macrotrends
# https://pypi.org/project/finpie/
# -------------------------------------------------------
def cor_agris():
    calculate_agri()
# Milk
# butter
# https://futures.tradingcharts.com/chart/BD_/W


# -------------------------------------------------------
def estimate_oil_corr(isReload=True):
    if isReload:
        # combine data
        # predict
        pass


# -------------------------------------------------------
# AUD vs NZD cùng chạy (correlation)

# -------------------------------------------------------
# Economic calendar and predict index:
# GDP: predict, not real time
# https://www.quandl.com/data/ODA/NZL_NGDPRPC-New-Zealand-GDP-per-Capita-at-Constant-Prices-LCU
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'NZL_NGDPRPC')
        get_economic_quandl(currency, 'AMECO', 'NZL_1_0_310_0_UBCABOP')


# ----------------------------
# Unemployment Rate:
# https://www.quandl.com/data/ODA/NZL_LUR-New-Zealand-Unemployment-Rate-of-Total-Labor-Force
def get_unemploymentrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'NZL_LUR')


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_NZL')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_NZL')


# ----------------------------
# Employment Change:
# https://fred.stlouisfed.org/series/LREM64TTNZQ156S
def get_employmentchange(isReload=True):
    if isReload:
        get_economic_fred(currency, 'LREM64TTNZQ156S')


# ----------------------------
# Retail sales:
# https://fred.stlouisfed.org/series/SLRTTO01NZQ189N
def get_retailsales(isReload=True):
    if isReload:
        get_economic_fred(currency, 'SLRTTO01NZQ189N')

# ----------------------------
# GDT
# -------------------------------------------------------
