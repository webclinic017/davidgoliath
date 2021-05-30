# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *
import usd as king
currency = 'aud'


# -------------------------------------------------------
# bonds:
# ----------------------------
def calculate_bond(isReload=True):
    # for investpy
    data = ['Australia 2Y', 'Australia 5Y', 'Australia 10Y']
    info = [[markets[3], 'australia', get_bonds]]*len(data)
    params = ['aubond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices:
# ----------------------------
# ASX 200 Futures: https://investing.com/indices/australia-200-futures
def get_asx200(isReload=True):
    data = ['S&P/ASX 200', 'S&P/ASX Midcap 50']
    info = [[markets[0], 'australia', get_indices]]*len(data)
    params = ['auindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# currencies:
# ----------------------------
# aud pair ------------------------------
def compare_minor(isReload=True):
    data = ['XAU/AUD', 'EUR/AUD', 'GBP/AUD', 'AUD/NZD',
            'AUD/JPY', 'AUD/CAD', 'AUD/USD', 'AUD/CHF']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['audmajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# (carry trade) JPY/CHF rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def corr_nzvolatility(isReload=True):
    # more detail with rate diff
    data = ['AUD/JPY', 'AUD/CHF', 'S&P 500 VIX']
    info = [[markets[1], 'united states', get_forex]] * \
        2 + [[markets[0], 'united states', get_indices]]
    params = ['aupair_vix', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# ----------------------------IMPORTANT
def cor_audcomodity(isReload=True):
    data = ['AUD/USD', 'USD/CNH', 'CNH/JPY', 'Crude Oil WTI', 'Gold', 'Copper']
    info = [[markets[1], 'united states', get_forex]] * \
        3 + [[markets[2], 'united states', get_commodities]] * 3
    params = ['cor_audcomodity', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# Compare:
# Cash rate: already have ---- MOST IMPORTANT ----
# FED fund rate: https://fred.stlouisfed.org/series/DFF
def get_cashrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RBA', 'F13_FOOIRATCR')
    # get_ffr()


# -------------------------------------------------------
# Economic calendar and predict index:
# GDP:
# https://www.quandl.com/data/ODA/AUS_NGDPD-Australia-GDP-at-Current-Prices-USD-Billions
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'AUS_NGDPD')


# ----------------------------
# Unemployment Rate:
# https://www.quandl.com/data/ODA/AUS_LUR-Australia-Unemployment-Rate-of-Total-Labor-Force
def get_unemploymentrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'AUS_LUR')


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_AUS')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_AUS')


# ----------------------------
# Employment Change:
# https://www.quandl.com/data/RBA/H05-Labour-Force
def get_employmentchange(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RBA', 'H05')
# -------------------------------------------------------
