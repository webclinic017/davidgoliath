# #######################################################
from alphautils import *
currency = 'chf'


# -------------------------------------------------------
# bonds:
# ----------------------------
# https://www.investing.com/rates-bonds/switzerland-10-year-bond-yield
def calculate_bond(isReload=True):
    data = ['Switzerland 2Y', 'Switzerland 5Y', 'Switzerland 10Y']
    info = [[markets[3], 'switzerland', get_bond]]*len(data)
    params = ['swbond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices
# ----------------------------
# Switzerland 20: https://www.investing.com/indices/switzerland-20
def get_smi20(isReload=True):
    data = ['SMI', 'FTSE Switzerland', 'PHLX Swiss Franc', 'Switzerland 10Y']
    info = [[markets[0], 'switzerland', get_index]] *\
        2 + [[markets[0], 'united states', get_index]] + \
            [[markets[3], 'switzerland', get_bond]]
    params = ['swindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# currencies:
# ----------------------------
# chf major cross:
def compare_major(isReload=True):
    data = ['XAU/CHF', 'EUR/CHF', 'USD/CHF', 'GBP/CHF',
            'AUD/CHF', 'NZD/CHF', 'CAD/CHF', 'CHF/JPY',
            'PHLX Swiss Franc', 'Switzerland 10Y']
    info = [[markets[1], 'united states', get_forex]] *\
        8 + [[markets[0], 'united states', get_index]]\
        + [[markets[3], 'switzerland', get_bond]]
    params = ['chfmajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# (carry trade) AUD/NZD/CAD rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def corr_swvolatility(isReload=True):
    # more detail with rate diff
    data = ['AUD/CHF', 'NZD/CHF', 'CAD/CHF', 'PHLX Swiss Franc', 'S&P 500 VIX']
    info = [[markets[1], 'united states', get_forex]] * \
        3 + [[markets[0], 'united states', get_index]]*2
    params = ['chfpair_vix', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# EURCHF and NASDAQ Composite correlation
# https://www.investing.com/indices/nasdaq-composite
def cor_echf_nasdaq(isReload=True):
    data = ['EUR/CHF', 'PHLX Swiss Franc', 'Nasdaq']
    info = [[markets[1], 'united states', get_forex]] + \
        [[markets[0], 'united states', get_index]]*2
    params = ['echf_nasdaq', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# COmpare with :
# Gold price: https://www.investing.com/commodities/gold
# Swiss Franc: https://www.investing.com/indices/phlx-swiss-franc
def cor_chf_gold(isReload=True):
    data = ['Gold', 'PHLX Swiss Franc']
    info = [[markets[2], 'united states', get_commodities],
            [markets[0], 'united states', get_index]]
    params = ['gold_chf', data, info, analysis_intermarket]
    make_market(params, isReload)


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
# ng?????c v???i stock/ bond v?? yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_CHE')


# ----------------------------
# inflation: already code - c??ng chi???u v???i yeild
# c??ng chi???u v???i l??i su???t
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


def get_all():
    calculate_bond()
    get_smi20()
    compare_major()
    corr_swvolatility()
    cor_echf_nasdaq()
    cor_chf_gold()
    '''
    # combine economic params
    '''
    # get_gdp()
    # get_cpi()
    # get_inflation()


# get_all()


def return_stats():
    times = {2: 'Monthly', 3: 'Weekly', 5: 'Daily'}
    # jpbond
    quotes = {'swbond', 'swindex', 'chfmajor',
              'chfpair_vix', 'echf_nasdaq', 'gold_chf'}
    # improve by zip: T.B.D
    for quote in quotes:
        for k, v in times.items():
            correlation_one(periods=k, quotes=quote, interval=v)


# return_stats()
