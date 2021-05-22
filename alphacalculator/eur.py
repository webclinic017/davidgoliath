# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *

currency = 'eur'


# -------------------------------------------------------
# #######################################################
# DE bond yeild
# https://www.investing.com/rates-bonds/germany-10-year-bond-yield
# https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield

# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/

# -------------------------------------------------------
# stock indices:
# ----------------------------
# Euro Stoxx 50: https://www.investing.com/indices/eu-stoxx50
# ----------------------------
# DAX: https://www.investing.com/indices/germany-30
# -------------------------------------------------------
# Exy : prefer Weekly, Monthly data
def get_exy():
    get_indices('PHLX Euro', 'united states')
    pass


get_exy()


# -------------------------------------------------------
# ECB bid rate:
# taylor equation
# https://stackoverflow.com/questions/59380645/taylor-expansion-in-python
# https://www.quandl.com/data/BUNDESBANK/BBK01_SU0202-Ecb-Interest-Rates-For-Main-Refinancing-Operations-End-Of-Month
# -------------------------------------------------------
# Debt (optional):
# https://www.quandl.com/data/FRED/DEBTTLDEA188A-Central-government-debt-total-of-GDP-for-Germany
# -------------------------------------------------------
# Gold price: https://www.investing.com/commodities/gold
# EURUSD and Gold price correlation
# -------------------------------------------------------
# Economic calendar and predict index:
# ----------------------------
# GDP: https://www.quandl.com/data/FRED/MKTGDPEZA646NWDB-Gross-Domestic-Product-for-Euro-Area
# Ger GDP: https://www.quandl.com/data/FRED/MKTGDPDEA646NWDB-Gross-Domestic-Product-for-Germany
# ----------------------------
# Ger industrial:
# https://www.quandl.com/data/BCB/3778-Industrial-production-index-Germany
# ----------------------------
# CPI: already code
# ----------------------------
# inflation: already code
# ----------------------------
# Unemployment rate, Germany:
# https://www.quandl.com/data/BCB/3785-Unemployment-rate-Germany
# -------------------------------------------------------

