# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
from alphautils import *
import usd as king
currency = 'cad'


# -------------------------------------------------------
# #######################################################
# 10Y treasury bond yeild
def calculate_bond(isReload=True):
    if isReload:
        get_bonds('Canada 2Y')
        get_bonds('Canada 5Y')
        get_bonds('Canada 10Y')
    else:
        pass


def calculate_bondspread(isReload=True):
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    if isReload:
        king.calculate_bond()
    pass
# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/


# -------------------------------------------------------
# stock indices: https://www.investing.com/indices/major-indices
# ----------------------------
# CA60: https://www.investing.com/indices/s-p-tsx-60
def get_tsx60(isReload=True):
    if isReload:
        get_indices('S&P/TSX 60', 'canada')


# -------------------------------------------------------
# Cxy: https://www.investing.com/indices/phlx-canadian-dollar
def get_cxy(isReload=True):
    if isReload:
        get_indices('PHLX Canadian Dollar', 'united states')
    pass


# cad major cross:
def compare_major(isReload=True):
    if isReload:
        forward_quotes = ['XAU', 'EUR', 'USD', 'GBP', 'AUD', 'NZD']
        backward_quotes = ['JPY', 'CHF']
        if isReload:
            for quote in forward_quotes:
                get_currency_cross(f"{quote}/CAD")
            for quote in backward_quotes:
                get_currency_cross(f"CAD/{quote}")
    else:
        pass


# CAD thường chạy song song vs USD (so với những cặp tiền khác)
def cor_cxy_dxy(isReload=True):
    if isReload:
        pass


# -------------------------------------------------------
# Overnight rate:
# https://www.quandl.com/data/BOC/CORRA-Canadian-Overnight-Repo-Rate-CORRA
def get_cashrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BOC', 'CORRA')


# ----------------------------
# (carry trade) - nếu volatility nhỏ, CAD -> diễn viên chính
# https://www.investing.com/indices/volatility-s-p-500
def get_carrytradeindex(isReload=True):
    if isReload:
        get_volatility()
    # combine data -> calculate spread ...
    pass


# -------------------------------------------------------
# Motor vehicle (optional)
# https://www.quandl.com/data/FRED/DAUTONSA-Motor-Vehicle-Retail-Sales-Domestic-Autos
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'DAUTONSA')


# -------------------------------------------------------
# ----------------------------IMPORTANT
def cor_metals(isReload=True):
    if isReload:
        # cor_audusd_gold

        # Gold price: https://www.investing.com/commodities/gold
        get_gold()
        # Copper: https://www.investing.com/commodities/copper
        get_copper()
        # others
        calculate_metals()
        # china policy
    pass


# -------------------------------------------------------
# ----------------------------IMPORTANT
# compare USDCAD vs
# xti oil price: https://www.investing.com/commodities/crude-oil
def cor_uc_xti(isReload=True):
    if isReload:
        get_currency_cross('USD/CAD')
        get_commodities('Crude Oil WTI')
        pass


# -------------------------------------------------------
# Economic calendar and predict index:
# GDP:
def get_gdp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'CAN_NGDP')
        # # optional
        # get_economic_quandl(currency, 'ODA', 'CAN_NGDP_RPCH')
        # get_economic_quandl(currency, 'ODA', 'CAN_NGDP_R')


# ----------------------------
# Unemployment Rate:
# https://www.quandl.com/data/ODA/CAN_LUR-Canada-Unemployment-Rate-of-Total-Labor-Force
def get_unemploymentrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'CAN_LUR')
        # # optional
        # get_economic_quandl(currency, 'OECD', 'STLABOUR_CAN_LRUNTTTT_ST_M')


# ----------------------------
# CPI: already code
# ngược với stock/ bond và yeild
def get_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_CAN')


# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất
def get_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_CAN')


# ----------------------------
# Employment Change:
# https://www.quandl.com/data/ODA/CAN_LE-Canada-Employment-Millions
# -------------------------------------------------------
# Exports of Goods:
# https://www.quandl.com/data/ODA/CAN_TX_RPCH-Canada-Exports-of-Goods-and-services-change
# https://www.quandl.com/data/ODA/CAN_TXG_RPCH-Canada-Exports-of-Goods-change
# -------------------------------------------------------
def get_export(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'ODA', 'CAN_TX_RPCH')
        get_economic_quandl(currency, 'ODA', 'CAN_TXG_RPCH')
