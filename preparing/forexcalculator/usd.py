# ------------- import part ------------------------------
from alphautils import *
currency = 'usd'
country = 'united states'
# ------------------------------


# -------------------------------------------------------
# bonds:
# ----------------------------
def calculate_bond(isReload=True):
    # for investpy
    data = ['U.S. 2Y', 'U.S. 5Y', 'U.S. 10Y']
    info = [[markets[3], 'united states', get_bonds]]*len(data)
    params = ['usbond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices
# ----------------------------
def get_stock_indices(isReload=True):
    # f(o): priority number list -> 1 main index
    data = ['SmallCap 2000', 'Dow 30', 'S&P 500', 'Nasdaq']
    info = [[markets[0], 'united states', get_indices]]*len(data)
    params = ['usindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# Dxy: update tick data for this
def cor_dxygo(isReload=True):
    # update real time from DXY_M1 ICmarkets
    pass


# -------------------------------------------------------
# currencies:
# ----------------------------
# usd major cross
def compare_major(isReload=True):
    data = ['XAU/USD', 'EUR/USD', 'GBP/USD', 'AUD/USD',
            'NZD/USD', 'USD/CHF', 'USD/JPY', 'USD/CAD']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['usdmajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# Chỉ số sợ hãi Volatility Index: JPY, CHF tăng giá
# dùng trong carry trade và stock predict
# < 20 -> ít sợ, > 40 -> sợ nhiều + các mô hình giá
# COMMON--------------------------------


def cor_usmain(isReload=True):
    data = ['S&P 500 VIX', 'US Dollar Index',
            'U.S. 10Y', 'Gold', 'Crude Oil WTI']
    info = [[markets[0], 'united states', get_indices]] \
        * 2 + [[markets[3], 'united states', get_bonds]] \
            + [[markets[2], 'united states', get_commodities]] * 2
    params = ['cor_usmain', data, info, analysis_intermarket]
    make_market(params, isReload)


# Oil corr --------------------------------


def corr_usoil(isReload=True):
    data = ['AUD/USD', 'NZD/USD', 'GBP/USD', 'USD/CAD', 'Crude Oil WTI']
    info = [[markets[1], 'united states', get_forex]] * \
        4 + [[markets[2], 'united states', get_commodities]]
    params = ['corr_usoil', data, info, analysis_intermarket]
    make_market(params, isReload)

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


def get_all():
    calculate_bond()
    get_stock_indices()
    compare_major()
    cor_usmain()
    corr_usoil()
    '''
    # combine economic params
    '''
    get_ffr()
    get_gdp()
    get_nfp()
    get_cpi()
    get_inflation()
    get_retailsales()
    get_ppi()
    get_pmi()
    get_unemploymentrate()
    get_tradebalance()
    get_industrial()
    get_housing()
    get_debt_percent()


# get_all()
