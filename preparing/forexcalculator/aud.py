# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *
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
    data = ['S&P/ASX 200', 'S&P/ASX 50', 'S&P/ASX 20',
            'PHLX Australian Dollar', 'Australia 10Y']
    info = [[markets[0], 'australia', get_indices]] *\
        3+[[markets[0], 'united states', get_indices]]\
        + [[markets[3], 'australia', get_bonds]]
    params = ['auindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# currencies:
# ----------------------------
# aud pair ------------------------------
def compare_minor(isReload=True):
    data = ['XAU/AUD', 'EUR/AUD', 'GBP/AUD', 'AUD/NZD',
            'AUD/JPY', 'AUD/CAD', 'AUD/USD', 'AUD/CHF',
            'PHLX Australian Dollar', 'Australia 10Y']
    info = [[markets[1], 'united states', get_forex]] *\
        8 + [[markets[0], 'united states', get_indices]]\
        + [[markets[3], 'australia', get_bonds]]
    params = ['audmajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# (carry trade) JPY/CHF rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500
def corr_auvolatility(isReload=True):
    # more detail with rate diff
    data = ['AUD/JPY', 'AUD/CHF', 'PHLX Australian Dollar', 'S&P 500 VIX']
    info = [[markets[1], 'united states', get_forex]] * \
        2 + [[markets[0], 'united states', get_indices]]*2
    params = ['aupair_vix', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# ----------------------------IMPORTANT
def cor_audcomodity(isReload=True):
    data = ['AUD/USD', 'USD/CNH', 'PHLX Australian Dollar',
            'Crude Oil WTI', 'Gold', 'Copper']
    info = [[markets[1], 'united states', get_forex]] * \
        2 + [[markets[0], 'united states', get_indices]] + \
        [[markets[2], 'united states', get_commodities]] * 3
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


def nlp_cashrate():
    pass


# -------------------------------------------------------
# Economic calendar and predict index:
def fx_factscraper():
    # clipboard... (handy way)
    pass


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


# get_employmentchange()
# -------------------------------------------------------


def get_all():
    calculate_bond()
    get_asx200()
    compare_minor()
    corr_auvolatility()
    cor_audcomodity()
    '''
    # combine economic params
    '''
    # get_cashrate()
    # get_gdp()
    # get_unemploymentrate()
    # get_cpi()
    # get_inflation()
    # get_employmentchange()


# get_all()


def return_stats():
    times = {2: 'Monthly', 3: 'Weekly', 5: 'Daily'}
    quotes = {'aubond', 'auindex', 'audmajor', 'aupair_vix', 'cor_audcomodity'}
    # improve by zip: T.B.D
    for quote in quotes:
        for k, v in times.items():
            correlation_one(periods=k, quotes=quote, interval=v)


# return_stats()
'''
Common correlations (automatic analysis - not human action)
1. Copper, AUDUSD, Australian Dollar Index (all timeframe)
2. USDCNH, Gold, Copper (Week, Month)
3. Australian Dollar Index, S&P 500 VIX (in Short term)
4. Australian Dollar Index, S&P ASX 200 ((Week, Month))
'''
