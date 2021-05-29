# #######################################################
# -------------------------------------------------------
from alphautils import *
import usd as king
currency = 'jpy'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild: tai san tru an cung voi US bond
# https://www.investing.com/rates-bonds/japan-10-year-bond-yield
def calculate_bond(isReload=True):
    if isReload:
        get_bonds('Japan 2Y')
        get_bonds('Japan 5Y')
        get_bonds('Japan 10Y')
    else:
        pass


# compare
def calculate_bondspread(isReload=True):
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    if isReload:
        king.calculate_bond()
    pass


# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/
# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# Nikkei 225: https://www.investing.com/indices/japan-ni225
def get_nikkei225(isReload=True):
    if isReload:
        get_indices('Nikkei 225', 'japan')


# -------------------------------------------------------
# Jxy: đo lƣờng mức độ e ngại rủi ro
def get_jxy(isReload=True):
    if isReload:
        get_indices('PHLX Yen', 'united states')
    pass


# jpy major cross
def compare_major(isReload=True):
    if isReload:
        forward_quotes = ['XAU', 'EUR', 'CHF',
                          'GBP', 'CAD', 'USD', 'AUD', 'NZD']
        if isReload:
            for quote in forward_quotes:
                get_currency_cross(f"{quote}/JPY")
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
# EURJPY and NASDAQ Composite correlation
# https://www.investing.com/indices/nasdaq-composite
def cor_ej_nasdaq(isReload=True):
    if isReload:
        get_currency_cross('EUR/JPY')
        king.get_nasdaq_composite()
    pass


# -------------------------------------------------------
# COmpare with :
# Gold price: https://www.investing.com/commodities/gold
# Swiss Franc: https://www.investing.com/indices/phlx-swiss-franc
def cor_jpy_gold(isReload=True):
    if isReload:
        pass


# -------------------------------------------------------
# Economic calendar and predict index:
# GDP:
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'JPN_PPPPC')
        get_economic_quandl(currency, 'ODA', 'JPN_PPPSH')
    pass


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_JPN')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_JPN')


# ----------------------------
# Retail sales:
# ----------------------------
# PMI:
# ----------------------------
# PPI:
# -------------------------------------------------------
