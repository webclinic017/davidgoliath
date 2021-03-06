# #######################################################
# reference:
# https://github.com/bank-of-england/Shapley_regressions

# -------------------------------------------------------
# #######################################################
from alphautils import *
currency = 'gbp'


# -------------------------------------------------------
# bonds:
# ----------------------------
# https://www.investing.com/rates-bonds/uk-10-year-bond-yield
def calculate_bond(isReload=True):
    data = ['U.K. 2Y', 'U.K. 5Y', 'U.K. 10Y']
    info = [[markets[3], 'united kingdom', get_bond]]*len(data)
    params = ['ukbond', data, info]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices:
# ----------------------------
# FTSE 100 : https://www.investing.com/indices/uk-100
def get_ftse(isReload=True):
    data = ['FTSE 100', 'FTSE 250', 'FTSE 350', 'UK 100',
            'PHLX British Pound', 'U.K. 10Y']
    info = [[markets[0], 'united kingdom', get_index]] *\
        4 + [[markets[0], 'united states', get_index]]\
        + [[markets[3], 'united kingdom', get_bond]]
    params = ['ukindex', data, info]
    make_market(params, isReload)


# -------------------------------------------------------
# currencies:
# ----------------------------
# gbp major cross
def compare_major(isReload=True):
    data = ['XAU/GBP', 'EUR/GBP', 'GBP/JPY', 'GBP/CAD',
            'GBP/USD', 'GBP/AUD', 'GBP/NZD', 'GBP/CHF',
            'PHLX British Pound', 'U.K. 10Y']
    info = [[markets[1], 'united states', get_forex]] *\
        8 + [[markets[0], 'united states', get_index]]\
        + [[markets[3], 'united kingdom', get_bond]]
    params = ['gbpmajor', data, info]
    make_market(params, isReload)


# -------------------------------------------------------
# Brent Oil corr ----- MOST IMPORTANT THINGS -----
# https://www.investing.com/commodities/brent-oil
def corr_ukoil(isReload=True):
    data = ['GBP/USD', 'GBP/CHF', 'GBP/JPY', 'EUR/GBP',
            'PHLX British Pound', 'Brent Oil']
    info = [[markets[1], 'united states', get_forex]] * \
        4 + [[markets[0], 'united states', get_index]]\
        + [[markets[2], 'united kingdom', get_commodities]]
    params = ['corr_ukoil', data, info]
    make_market(params, isReload)


# -------------------------------------------------------
# BOE repo rate: (LIBOR rate relate CHF rate)
# https://www.quandl.com/data/BOE/IUDBEDR-Official-Bank-Rate
def get_boe_rate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BOE', 'IUDBEDR')
        # # CHF/USD rate (optional)
        # get_economic_quandl(currency, 'FED', 'RXI_N_A_SZ')


# -------------------------------------------------------
# Economic calendar and predict index:
# GDP:
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'GBR_PPPGDP')
    pass


# ----------------------------
# CPI: already code
# ng?????c v???i stock/ bond v?? yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_GBR')


# ----------------------------
# inflation: already code - c??ng chi???u v???i yeild
# c??ng chi???u v???i l??i su???t
def get_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_GBR')


# ----------------------------
# Retail sales:
# https://fred.stlouisfed.org/series/SLRTTO02GBA661S
# ----------------------------
# PMI:
# ----------------------------
# PPI:
def get_ppi(isReload=True):
    if isReload:
        get_economic_quandl(
            currency, 'OECD', 'MEI_PRICES_PPI_PIEAMI01_GBR_IXOB_M')


# ----------------------------
# Unemployment rate ng?????c v???i l??i su???t...
# https://www.quandl.com/data/ODA/GBR_LUR-United-Kingdom-Unemployment-Rate-of-Total-Labor-Force
def get_unemploymentrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'GBR_LUR')
# -------------------------------------------------------


def get_all():
    calculate_bond()
    get_ftse()
    corr_ukoil()
    compare_major()
    '''
    # combine economic params
    '''
    # get_boe_rate()
    # get_gdp()
    # get_cpi()
    # get_inflation()
    # get_ppi()
    # get_unemploymentrate()


get_all()


def return_stats():
    times = {2: 'Monthly', 3: 'Weekly', 5: 'Daily'}
    quotes = {'ukbond', 'ukindex', 'gbpmajor', 'corr_ukoil'}
    # improve by zip: T.B.D
    for quote in quotes:
        for k, v in times.items():
            correlation_one(periods=k, quotes=quote, interval=v)


# return_stats()
