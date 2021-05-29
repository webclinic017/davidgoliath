# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *
import usd as king
currency = 'cad'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild
def calculate_bond(isReload=True):
    if isReload:
        get_bonds('Australia 2Y')
        get_bonds('Australia 5Y')
        get_bonds('Australia 10Y')
    else:
        pass


# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/
def calculate_bondspread(isReload=True):
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    pass


# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# ASX 200 Futures: https://au.investing.com/indices/australia-200-futures
def get_asx200(isReload=True):
    if isReload:
        get_indices('S&P/ASX 200', 'australia')
    pass


# -------------------------------------------------------
# Axy
def get_axy(isReload=True):
    if isReload:
        get_indices('PHLX Australian Dollar', 'united states')
    pass


# aud pair ------------------------------
def compare_minor(isReload=True):
    if isReload:
        forward_quotes = ['XAU', 'EUR', 'GBP']
        backward_quotes = ['CHF', 'JPY', 'CAD', 'USD', 'NZD']
        if isReload:
            for quote in forward_quotes:
                get_currency_cross(f"{quote}/AUD")
            for quote in backward_quotes:
                get_currency_cross(f"AUD/{quote}")
    else:
        pass


# -------------------------------------------------------
# Compare:
# Cash rate: already have ---- MOST IMPORTANT ----
# FED fund rate: https://fred.stlouisfed.org/series/DFF
def get_cashrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RBA', 'F13_FOOIRATCR')
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
# ----------------------------IMPORTANT
def cor_metals(isReload=True):
    if isReload:
        # cor_audusd_gold

        # Gold price: https://www.investing.com/commodities/gold
        get_gold()
        # Copper: https://www.investing.com/commodities/copper
        get_copper()
        # others
        calculate_metals()
        # china policy
    pass


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
