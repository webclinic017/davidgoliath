# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *

currency = 'cad'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild
# https://www.investing.com/rates-bonds/canada-10-year-bond-yield
# https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield

# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/

# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# CA60: https://www.investing.com/indices/s-p-tsx-60

# -------------------------------------------------------
# Cxy: maybe using this for convesion
# https://pypi.org/project/forex-python/
def get_cxy():
    get_indices('PHLX Canadian Dollar', 'united states')
    pass


get_cxy()
# https://www.investing.com/indices/phlx-canadian-dollar
# CAD thường chạy song song vs USD (so với những cặp tiền khác)

# -------------------------------------------------------
# Overnight rate:
# https://www.quandl.com/data/BOC/CORRA-Canadian-Overnight-Repo-Rate-CORRA
# ----------------------------
# (carry trade) - nếu volatility nhỏ, CAD -> diễn viên chính
# https://www.investing.com/indices/volatility-s-p-500

# -------------------------------------------------------
# Motor vehicle (optional)
# https://www.quandl.com/data/FRED/DAUTONSA-Motor-Vehicle-Retail-Sales-Domestic-Autos
# -------------------------------------------------------
# ----------------------------IMPORTANT
# Gold price: https://www.investing.com/commodities/gold
# Copper: https://www.investing.com/commodities/copper

# -------------------------------------------------------
# ----------------------------IMPORTANT
# compare USDCAD vs
# xti oil price: https://www.investing.com/commodities/crude-oil

# -------------------------------------------------------
# Economic calendar and predict index:
# GDP:
# https://www.quandl.com/data/FRED/CANRGDPR-Real-GDP-in-Canada-DISCONTINUED
# ----------------------------
# Unemployment Rate:
# https://www.quandl.com/data/ODA/CAN_LUR-Canada-Unemployment-Rate-of-Total-Labor-Force
# https://www.quandl.com/data/OECD/STLABOUR_CAN_LRUNTTTT_ST_M-Canada-Unemployment-Rate-Aged-15-And-Over-All-Persons-Level-Rate-Or-Quantity-Series
# ----------------------------
# CPI: already code
# ----------------------------
# inflation: already code
# ----------------------------
# Employment Change:
# https://www.quandl.com/data/ODA/CAN_LE-Canada-Employment-Millions
# -------------------------------------------------------
