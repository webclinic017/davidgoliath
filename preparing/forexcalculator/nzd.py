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
# bonds:
# ----------------------------
# https://www.investing.com/rates-bonds/new-zealand-10-years-bond-yield
def calculate_bond(isReload=True):
    # for investpy
    data = ['New Zealand 2Y', 'New Zealand 5Y', 'New Zealand 10Y']
    info = [[markets[3], 'new zealand', get_bonds]]*len(data)
    params = ['nzbond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices:
# ----------------------------
# NZX 50: https://www.investing.com/indices/nzx-50
def get_nzx(isReload=True):
    data = ['NZX 50', 'NZX MidCap']
    info = [[markets[0], 'new zealand', get_indices]]*len(data)
    params = ['nzindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# currencies:
# ----------------------------
# nzd pair ------------------------------
def compare_minor(isReload=True):
    data = ['XAU/NZD', 'EUR/NZD', 'GBP/NZD', 'AUD/NZD',
            'NZD/JPY', 'NZD/CAD', 'NZD/USD', 'NZD/CHF']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['nzdmajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# (carry trade) JPY/CHF rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def corr_nzvolatility(isReload=True):
    # more detail with rate diff
    data = ['NZD/JPY', 'NZD/CHF', 'S&P 500 VIX']
    info = [[markets[1], 'united states', get_forex]] * \
        2 + [[markets[0], 'united states', get_indices]]
    params = ['nzpair_vix', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# https://commodity.com/data/new-zealand/
# -------------------------------------------------------
def cor_nzagri(isReload=True):
    # need define priority for each param
    data = ['Rough Rice', 'US Soybean Oil',
            'US Soybean Meal', 'US Soybeans',
            'US Wheat', 'US Corn', 'Oats', 'London Wheat',
            'US Coffee C', 'US Cotton #2',
            'US Sugar #11', 'Orange Juice',
            'US Cocoa', 'Lumber', 'London Cocoa',
            'London Coffee', 'London Sugar',
            'Live Cattle', 'Lean Hogs', 'Feeder Cattle']
    info = [[markets[2], 'united states', get_commodities]]*len(data)
    params = ['cor_nzagri', data, info, analysis_commodity]
    make_market(params, isReload)


# -------------------------------------------------------
# Oil correlation
def cor_nzoil(isReload=True):
    data = ['NZD/CHF', 'NZD/USD', 'NZD/JPY', 'EUR/NZD', 'Crude Oil WTI']
    info = [[markets[1], 'united states', get_forex]] * \
        4 + [[markets[2], 'united states', get_commodities]]
    params = ['cor_nzoil', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# Compare with another interest rate:
# Official cash rate: already have ---- MOST IMPORTANT ----
# FED fund rate: https://fred.stlouisfed.org/series/DFF
def get_cashrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'OECD', 'KEI_IR3TIB01_NZL_ST_Q')
    # get_ffr()


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
