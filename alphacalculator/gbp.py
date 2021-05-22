# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/

# reference:
# https://github.com/bank-of-england/Shapley_regressions

# -------------------------------------------------------
# #######################################################
from alphautils import *

currency = 'gbp'


# 10Y treasury bond yeild
# https://www.investing.com/rates-bonds/uk-10-year-bond-yield
# https://www.quandl.com/data/BOE-Bank-of-England-Official-Statistics

# compare
# https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield

# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/

# -------------------------------------------------------
# stock indices:
# ----------------------------
# FTSE 100 : https://www.investing.com/indices/uk-100

# -------------------------------------------------------
# Bxy
def get_bxy():
    get_indices('PHLX British Pound', 'united states')
    pass


get_bxy()
# -------------------------------------------------------
# BOE repo rate: (LIBOR rate relate CHF rate)
# https://www.quandl.com/data/FRED/LIOR3M-3-month-London-Interbank-Offered-Rate-LIBOR

# https://www.quandl.com/data/BOE/IUMAGRON-Monthly-Average-Of-Gilt-Repo-Interest-Rate-Overnight
# https://fred.stlouisfed.org/series/CADONTD156N

# -------------------------------------------------------
# brent oil price:
# https://www.investing.com/commodities/brent-oil

# -------------------------------------------------------
# Economic calendar and predict index:
# GDP: https://www.quandl.com/data/ODA/GBR_NGDPD-United-Kingdom-GDP-at-Current-Prices-USD-Billions

# ----------------------------
# CPI: already code
# https://fred.stlouisfed.org/series/GBRCPIALLMINMEI
# ----------------------------
# Retail sales:
# https://fred.stlouisfed.org/series/SLRTTO02GBA661S
# ----------------------------
# PMI:
# ----------------------------
# PPI:
# ----------------------------
# inflation: already code
# ----------------------------
# Unemployment Rate:
# https://www.quandl.com/data/ODA/GBR_LUR-United-Kingdom-Unemployment-Rate-of-Total-Labor-Force
# -------------------------------------------------------
