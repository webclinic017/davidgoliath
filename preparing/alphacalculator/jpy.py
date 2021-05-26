# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *

currency = 'jpy'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild

# tai san tru an cung voi US bond
# https://www.investing.com/rates-bonds/japan-10-year-bond-yield
# https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield

# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/

# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# Nikkei 225: https://www.investing.com/indices/japan-ni225
# -------------------------------------------------------
# Jxy
def get_jxy():
    get_indices('PHLX Yen', 'united states')
    pass


get_jxy()
# -------------------------------------------------------
# (carry trade) AUD/NZD rate: already code vs Volatility Index
# https://www.investing.com/indices/volatility-s-p-500

# -------------------------------------------------------
# EURJPY and NASDAQ Composite correlation
# https://www.investing.com/indices/nasdaq-composite

# -------------------------------------------------------
# COmpare with :
# Gold price: https://www.investing.com/commodities/gold
# Swiss Franc: https://www.investing.com/indices/phlx-swiss-franc

# -------------------------------------------------------
# Economic calendar and predict index:
# GDP: https://www.quandl.com/data/FRED/MKTGDPJPA646NWDB-Gross-Domestic-Product-for-Japan
# ----------------------------
# CPI: already code
# ----------------------------
# inflation: already code
# ----------------------------
# Retail sales:
# ----------------------------
# PMI:
# ----------------------------
# PPI:
# -------------------------------------------------------
