# #######################################################
# reference:
# https://github.com/bank-of-england/Shapley_regressions

# -------------------------------------------------------
# #######################################################
from alphautils import *
import usd as king
currency = 'gbp'


# 10Y treasury bond yeild
# https://www.investing.com/rates-bonds/uk-10-year-bond-yield
def calculate_bond(isReload=True):
    if isReload:
        get_bonds('U.K. 2Y')
        get_bonds('U.K. 5Y')
        get_bonds('U.K. 10Y')
    else:
        pass


# compare
def calculate_bondspread(isReload=True):
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    king.calculate_bond()
    pass
# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/


# -------------------------------------------------------
# stock indices:
# ----------------------------
# FTSE 100 : https://www.investing.com/indices/uk-100
def get_ftse100(isReload=True):
    get_indices('FTSE 100', 'united kingdom')


# -------------------------------------------------------
# Bxy
def get_bxy():
    get_indices('PHLX British Pound', 'united states')
    pass


# gbp major cross
def compare_major(isReload=True):
    if isReload:
        forward_quotes = ['XAU', 'EUR']
        backward_quotes = ['CHF', 'JPY', 'CAD', 'USD', 'AUD', 'NZD']
        if isReload:
            for quote in forward_quotes:
                get_currency_cross(f"{quote}/GBP")
            for quote in backward_quotes:
                get_currency_cross(f"GBP/{quote}")
    else:
        pass


# -------------------------------------------------------
# BOE repo rate: (LIBOR rate relate CHF rate)
# https://www.quandl.com/data/BOE/IUDBEDR-Official-Bank-Rate
def get_boe_rate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BOE', 'IUDBEDR')
        # # CHF/USD rate (optional)
        # get_economic_quandl(currency, 'FED', 'RXI_N_A_SZ')


# -------------------------------------------------------
# brent oil price: (read data)
# https://www.investing.com/commodities/brent-oil
def get_brent():
    # read data
    pass


# -------------------------------------------------------
# Economic calendar and predict index:
# GDP:
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'GBR_PPPGDP')
    pass


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_GBR')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
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
# Unemployment rate ngược với lãi suất...
# https://www.quandl.com/data/ODA/GBR_LUR-United-Kingdom-Unemployment-Rate-of-Total-Labor-Force
def get_unemploymentrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'GBR_LUR')
# -------------------------------------------------------
