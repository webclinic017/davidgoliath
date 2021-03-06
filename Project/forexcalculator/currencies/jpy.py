# #######################################################
# -------------------------------------------------------
from alphautils import *
currency = 'jpy'


# -------------------------------------------------------
# bonds:
# ----------------------------
# https://www.investing.com/rates-bonds/japan-10-year-bond-yield
def calculate_bond(isReload=True):
    data = ['Japan 2Y', 'Japan 5Y', 'Japan 10Y']
    info = [[markets[3], 'japan', get_bond]]*len(data)
    params = ['jpbond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices:
# ----------------------------
# Nikkei 225: https://www.investing.com/indices/japan-ni225
def get_nikkei225(isReload=True):
    # can get more indices
    data = ['Nikkei 225', 'Nikkei Volatility', 'PHLX Yen', 'Japan 10Y']
    info = [[markets[0], 'japan', get_index]] * \
        2 + [[markets[0], 'united states', get_index]] + \
            [[markets[3], 'japan', get_bond]]
    params = ['jpindex', data, info, analysis_index]
    make_market(params, isReload)

# -------------------------------------------------------
# currencies:
# ----------------------------
# jpy major cross


def compare_major(isReload=True):
    data = ['XAU/JPY', 'EUR/JPY', 'USD/JPY', 'GBP/JPY',
            'AUD/JPY', 'NZD/JPY', 'CAD/JPY', 'CHF/JPY',
            'PHLX Yen', 'Japan 10Y']
    info = [[markets[1], 'united states', get_forex]] *\
        8 + [[markets[0], 'united states', get_index]]\
        + [[markets[3], 'japan', get_bond]]
    params = ['jpymajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# (carry trade) AUD/NZD/CAD rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500


def corr_jpvolatility(isReload=True):
    # more detail with rate diff
    data = ['AUD/JPY', 'NZD/JPY', 'CAD/JPY', 'PHLX Yen', 'S&P 500 VIX']
    info = [[markets[1], 'united states', get_forex]] * \
        3 + [[markets[0], 'united states', get_index]] * 2
    params = ['jpypair_vix', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# EURJPY and NASDAQ Composite correlation
# https://www.investing.com/indices/nasdaq-composite


def cor_ej_nasdaq(isReload=True):
    data = ['EUR/JPY', 'PHLX Yen', 'Nasdaq']
    info = [[markets[1], 'united states', get_forex]] + \
        [[markets[0], 'united states', get_index]]*2
    params = ['ej_nasdaq', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# COmpare with :
# Gold price: https://www.investing.com/commodities/gold
# Swiss Franc: https://www.investing.com/indices/phlx-yen


def cor_jpy_gold(isReload=True):
    data = ['Gold', 'PHLX Yen']
    info = [[markets[2], 'united states', get_commodities],
            [markets[0], 'united states', get_index]]
    params = ['gold_jpy', data, info, analysis_intermarket]
    make_market(params, isReload)


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
# ng?????c v???i stock/ bond v?? yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_JPN')


# ----------------------------
# inflation: already code - c??ng chi???u v???i yeild
# c??ng chi???u v???i l??i su???t
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

def get_all():
    calculate_bond()
    get_nikkei225()
    compare_major()
    corr_jpvolatility()
    cor_ej_nasdaq()
    cor_jpy_gold()
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
    quotes = {'jpbond', 'gold_jpy', 'ej_nasdaq',
              'jpypair_vix', 'jpindex', 'jpymajor'}
    # improve by zip: T.B.D
    for quote in quotes:
        for k, v in times.items():
            correlation_one(periods=k, quotes=quote, interval=v)


return_stats()
