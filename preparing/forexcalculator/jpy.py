# #######################################################
# -------------------------------------------------------
from alphautils import *
import usd as king
currency = 'jpy'


# -------------------------------------------------------
# bonds:
# ----------------------------
# https://www.investing.com/rates-bonds/japan-10-year-bond-yield
def calculate_bond(isReload=True):
    data = ['Japan 2Y', 'Japan 5Y', 'Japan 10Y']
    info = [[markets[3], 'japan', get_bonds]]*len(data)
    params = ['jpbond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices:
# ----------------------------
# Nikkei 225: https://www.investing.com/indices/japan-ni225
def get_nikkei225(isReload=True):
    # can get more indices
    data = ['Nikkei 225', 'Nikkei Volatility']
    info = [[markets[0], 'japan', get_indices]]*len(data)
    params = ['jpindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# currencies:
# ----------------------------
# jpy major cross
def compare_major(isReload=True):
    data = ['XAU/JPY', 'EUR/JPY', 'USD/JPY', 'GBP/JPY',
            'AUD/JPY', 'NZD/JPY', 'CAD/JPY', 'CHF/JPY']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['jpymajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# (carry trade) AUD/NZD/CAD rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def corr_jpvolatility(isReload=True):
    # more detail with rate diff
    data = ['AUD/JPY', 'NZD/JPY', 'CAD/JPY', 'S&P 500 VIX']
    info = [[markets[1], 'united states', get_forex]] * \
        3 + [[markets[0], 'united states', get_indices]]
    params = ['jpypair_vix', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# EURJPY and NASDAQ Composite correlation
# https://www.investing.com/indices/nasdaq-composite
def cor_ej_nasdaq(isReload=True):
    data = ['EUR/JPY', 'Nasdaq']
    info = [[markets[1], 'united states', get_forex],
            [markets[0], 'united states', get_indices]]
    params = ['ej_nasdaq', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# COmpare with :
# Gold price: https://www.investing.com/commodities/gold
# Swiss Franc: https://www.investing.com/indices/phlx-yen
def cor_jpy_gold(isReload=True):
    data = ['Gold', 'PHLX Yen']
    info = [[markets[2], 'united states', get_commodities],
            [markets[0], 'united states', get_indices]]
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
    get_gdp()
    get_cpi()
    get_inflation()


# get_all()
