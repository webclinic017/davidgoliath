# ------------- import part ------------------------------
from alphautils import *

currency = 'usd'
# ------------------------------


def calculate_usbond(isReload=True, useQuandl=True):
    # https://www.quandl.com/data/USTREASURY-US-Treasury
    if isReload:
        if useQuandl:
            ustreasury = {'USTREASURY': ['YIELD', 'REALYIELD',
                                         'BILLRATES', 'HQMYC',
                                         'MATDIS', 'AVMAT',
                                         'TNMBOR', 'TMBOR',
                                         'MKTDM', 'BRDNM']}
            main_key = list(ustreasury.keys())[0]
            get_bondyeild_quandl(currency, ustreasury, main_key)
        else:
            # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
            get_bonds('U.S. 10Y')
            pass
    else:
        # processing data
        # https://pypi.org/project/nelson-siegel-svensson/0.1.0/
        # https://pypi.org/project/yield-curve-dynamics/

        pass
    pass


calculate_usbond(isReload=True, useQuandl=True)


# ---------------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# russell-2000: get column 2 in csv source data
def get_russell():
    get_indices('SmallCap 2000', 'united states')
    pass


# ----------------------------
# Dow Jones
def get_dowjones():
    get_indices('Dow 30', 'united states')
    pass


# ----------------------------
# S&P 500
def get_spx():
    get_indices('S&P 500', 'united states')
    pass


# ----------------------------
# NASDAQ Composite
def get_nasdaq_composite():
    get_indices('Nasdaq', 'united states')
    pass


# -------------------------------------------------------
# Dxy:
def get_dxy():
    get_indices('US Dollar Index', 'united states')
    pass


# major cross
def compare_major(isReload=True):
    forward_quotes = ['EUR', 'GBP', 'AUD', 'NZD']
    backward_quotes = ['CHF', 'JPY', 'CAD']
    if isReload:
        for quote in forward_quotes:
            get_currency_cross(f"{quote}/USD")
        for quote in backward_quotes:
            get_currency_cross(f"USD/{quote}")


# compare_major(isReload=True)
# https://www.cmegroup.com/trading/why-futures/welcome-to-cme-fx-futures.html#
# cme_calling()


# -------------------------------------------------------
# Economic calendar and predict index:
# https://www.quandl.com/data/FRED-Federal-Reserve-Economic-Data/documentation
def get_gdp():
    get_economic_quandl(currency, 'FRED', 'GDP')
    pass


# ----------------------------
# NFP: same direction Stock/ USD
def get_nfp():
    get_economic_quandl(currency, 'ACC', 'NFP')
    pass


# --------THE MOST IMPORTANT THINGS--------------------------------------
# FED fund rate:
def get_ffr():
    get_economic_quandl(currency, 'FRED', 'FEDFUNDS')


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi():
    get_economic_quandl(currency, 'RATEINF', 'CPI_USA')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation():
    get_economic_quandl(currency, 'RATEINF', 'INFLATION_USA')


# ----------------------------------------------------------------------
# Retail sales:
def get_retailsales():
    get_economic_quandl(currency, 'FRED', 'RSXFS')


# ----------------------------
# PMI: same direction Stock/ USD
def get_pmi():
    get_economic_quandl(currency, 'FRED', 'NAPM')


# ----------------------------
# PPI:
def get_ppi():
    get_economic_quandl(currency, 'FRED', 'PPIACO')


# ----------------------------
# Unemployment rate ngược với lãi suất...
def get_unemploymentrate():
    get_economic_quandl(currency, 'FRED', 'UNRATE')


# ----------------------------
# Trade Balance ngược với lãi suất...
def get_tradebalance():
    get_economic_quandl(currency, 'FRED', 'BOPGSTB')


# ----------------------------
# Industrial Production Index
def get_industrial():
    get_economic_quandl(currency, 'FRED', 'INDPRO')


# -------------------------------------------------------
# Housing Starts
def get_housing():
    get_economic_quandl(currency, 'FRED', 'HOUST')
# # -------------------------------------------------------
