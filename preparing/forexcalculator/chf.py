# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *
import usd as king
currency = 'chf'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild
# https://www.investing.com/rates-bonds/switzerland-10-year-bond-yield
def calculate_bond(isReload=True):
    if isReload:
        get_bonds('Switzerland 2Y')
        get_bonds('Switzerland 5Y')
        get_bonds('Switzerland 10Y')
    else:
        pass


# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/
# compare
def calculate_bondspread(isReload=True):
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    if isReload:
        king.calculate_bond()
    pass


# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# Switzerland 20: https://www.investing.com/indices/switzerland-20
def get_smi20(isReload=True):
    if isReload:
        get_indices('SMI', 'switzerland')


# -------------------------------------------------------
# Sxy
def get_sxy(isReload=True):
    get_indices('PHLX Swiss Franc', 'united states')
    pass


# jpy major cross
def compare_major(isReload=True):
    if isReload:
        forward_quotes = ['XAU', 'EUR', 'GBP',
                          'CAD', 'USD', 'AUD', 'NZD']
        backward_quotes = ['JPY']
        if isReload:
            for quote in forward_quotes:
                get_currency_cross(f"{quote}/CHF")
            for quote in backward_quotes:
                get_currency_cross(f"CHF/{quote}")
    else:
        pass


# -------------------------------------------------------
# (carry trade) AUD/NZD rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def corr_volatility(isReload=True):
    # chỉ số VIX luôn nằm dƣới 20%. ???
    if isReload:
        get_volatility()
    pass


# -------------------------------------------------------
# EURCHF and NASDAQ Composite correlation
# https://www.investing.com/indices/nasdaq-composite
def cor_echf_nasdaq(isReload=True):
    if isReload:
        get_currency_cross('EUR/CHF')
        king.get_nasdaq_composite()
    pass


# -------------------------------------------------------
# COmpare with :
# Gold price: https://www.investing.com/commodities/gold
# Yen: https://www.investing.com/indices/phlx-yen
def cor_chf_gold(isReload=True):
    if isReload:
        pass


# -------------------------------------------------------
# Economic calendar and predict index:
# GDP:
# https://www.quandl.com/data/ODA/CHE_NGDPDPC-Switzerland-GDP-per-Capita-at-Current-Prices-USD
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'CHE_NGDPDPC')
    pass


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_CHE')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_CHE')
# ----------------------------
# Retail sales:
# ----------------------------
# PMI:
# ----------------------------
# PPI:
# -------------------------------------------------------
