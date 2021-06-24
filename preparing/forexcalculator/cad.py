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
# -------------------------------------------------------
# bonds:
# ----------------------------
def calculate_bond(isReload=True):
    data = ['Canada 2Y', 'Canada 5Y', 'Canada 10Y']
    info = [[markets[3], 'canada', get_bonds]]*len(data)
    params = ['cabond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices:
# ----------------------------
# CA60: https://www.investing.com/indices/s-p-tsx-60
def get_tsx(isReload=True):
    data = ['S&P/TSX 60', 'S&P/TSX MidCap', 'S&P/TSX Small Cap', 'S&P/TSX']
    info = [[markets[0], 'canada', get_indices]]*len(data)
    params = ['caindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# currencies:
# ----------------------------
# cad major cross:
def compare_major(isReload=True):
    data = ['XAU/CAD', 'EUR/CAD', 'USD/CAD', 'GBP/CAD',
            'AUD/CAD', 'NZD/CAD', 'CAD/JPY', 'CAD/CHF']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['camajor', data, info, analysis_currency]
    make_market(params, isReload)


# -------------------------------------------------------
# (carry trade)-JPY/CHF rate: nếu volatility nhỏ, CAD strong
# https://www.investing.com/indices/volatility-s-p-500
def corr_cavolatility(isReload=True):
    # more detail with rate diff
    data = ['CAD/JPY', 'CAD/CHF', 'S&P 500 VIX']
    info = [[markets[1], 'united states', get_forex]] * \
        2 + [[markets[0], 'united states', get_indices]]
    params = ['capair_vix', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# ----------------------------IMPORTANT
# Oil corr : https://www.investing.com/commodities/crude-oil
def cor_uc_xti(isReload=True):
    data = ['USD/CAD', 'Crude Oil WTI']
    info = [[markets[1], 'united states', get_forex],
            [markets[2], 'united states', get_commodities]]
    params = ['corr_caoil', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# Overnight rate:
# https://www.quandl.com/data/BOC/CORRA-Canadian-Overnight-Repo-Rate-CORRA
def get_cashrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BOC', 'CORRA')


# -------------------------------------------------------
# Motor vehicle (optional)
# https://www.quandl.com/data/FRED/DAUTONSA-Motor-Vehicle-Retail-Sales-Domestic-Autos
def get_motor(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'DAUTONSA')


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


def get_all():
    calculate_bond()
    get_tsx()
    compare_major()
    corr_cavolatility()
    cor_uc_xti()
    '''
    # combine economic params
    '''
    # get_cashrate()
    # get_motor()
    # get_gdp()
    # get_unemploymentrate()
    # get_cpi()
    # get_inflation()
    # get_export()


# get_all()
