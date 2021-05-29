# ------------- import part ------------------------------
from alphautils import *
currency = 'usd'
country = 'united states'
# ------------------------------


def calculate_bond(isReload=True):
    # for investpy
    bonds = ['U.S. 2Y', 'U.S. 5Y', 'U.S. 10Y']
    bond_params = ['usbond', markets[3], bonds,
                   'united states', get_bonds, analysis_bond]
    make_market(bond_params, isReload)
    pass


# ---------------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
def get_stock_indices(isReload=True):
    indices = ['SmallCap 2000', 'Dow 30', 'S&P 500', 'Nasdaq']
    index_params = ['usindex', markets[0], indices,
                    'united states', get_indices, analysis_index]
    make_market(index_params, isReload)


# -------------------------------------------------------
# Dxy: update tick data for this
def get_dxy(isReload=True):
    # update real time from DXY_M1 ICmarkets
    pass


# usd major cross
def compare_major(isReload=True):
    quotes = ['XAU/USD', 'EUR/USD', 'GBP/USD', 'AUD/USD',
              'NZD/USD', 'USD/CHF', 'USD/JPY', 'USD/CAD']
    quote_params = ['quote', markets[1], quotes,
                    'united states', get_currency_cross, analysis_currency]
    make_market(quote_params, isReload)


# -------------------------------------------------------
# Chỉ số sợ hãi Volatility Index: JPY, CHF tăng giá
# dùng trong carry trade và stock predict
# < 20 -> ít sợ, > 40 -> sợ nhiều + các mô hình giá
# COMMON--------------------------------
def get_volatility(isReload=True):
    if isReload:
        get_indices('S&P 500 VIX', country)


# ---------------- Important gold index -------------------------
# ---- arca-gold-bugs: https://en.wikipedia.org/wiki/HUI_Gold_Index ------
def get_hui(isReload=True):
    if isReload:
        get_indices('ARCA Gold BUGS', country)


# ------- settle phlx-gold-silver -------
# https://en.wikipedia.org/wiki/Philadelphia_Gold_and_Silver_Index
def get_gss(isReload=True):
    if isReload:
        get_indices('PHLX Gold Silver Settlement', country)
# https://www.cmegroup.com/trading/why-futures/welcome-to-cme-fx-futures.html#
# cme_calling()


# -------------------------------------------------------
# Economic calendar and predict index:
# https://www.quandl.com/data/FRED-Federal-Reserve-Economic-Data/documentation
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'GDP')
    pass


# ----------------------------
# NFP: same direction Stock/ USD
def get_nfp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ACC', 'NFP')
    pass


# --------THE MOST IMPORTANT THINGS--------------------------------------
# FED fund rate:
def get_ffr(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'FEDFUNDS')


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_USA')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_USA')


# ----------------------------------------------------------------------
# Retail sales:
def get_retailsales(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'RSXFS')


# ----------------------------
# PMI: same direction Stock/ USD
def get_pmi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'NAPM')


# ----------------------------
# PPI:
def get_ppi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'PPIACO')


# ----------------------------
# Unemployment rate ngược với lãi suất...
def get_unemploymentrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'UNRATE')


# ----------------------------
# Trade Balance ngược với lãi suất...
def get_tradebalance(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'BOPGSTB')


# ----------------------------
# Industrial Production Index
def get_industrial(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'INDPRO')


# -------------------------------------------------------
# Housing Starts
def get_housing(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'HOUST')


# # -------------------------------------------------------
def get_debt_percent(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'GFDEGDQ188S')
