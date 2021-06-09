# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc
from alphautils import *
import usd as king
currency = 'eur'
country = 'euro zone'


# -------------------------------------------------------
# bonds:
# ----------------------------
def calculate_bond(isReload=True):
    # for investpy
    data = ['Germany 2Y', 'Germany 5Y', 'Germany 10Y']
    info = [[markets[3], 'germany', get_bonds]]*len(data)
    params = ['eubond', data, info, analysis_bond]
    make_market(params, isReload)


# -------------------------------------------------------
# stock indices
# ----------------------------
def get_estoxx(isReload=True):
    data = ['Euro Stoxx 50', 'DAX', 'TecDAX',
            'CAC 40', 'IBEX 35', 'Italy 40']
    info = [[markets[0], 'germany', get_indices]]\
        * 3 + [[markets[0], 'france', get_indices]]\
        + [[markets[0], 'spain', get_indices]]\
        + [[markets[0], 'italy', get_indices]]
    params = ['euindex', data, info, analysis_index]
    make_market(params, isReload)


# -------------------------------------------------------
# Exy : prefer Weekly, Monthly data
def get_exy(isReload=True):
    # read data instead then analysis
    pass


# -------------------------------------------------------
# currencies:
# ----------------------------
# eur major cross: (EURUSD vs Gold)
def compare_major(isReload=True):
    data = ['XAU/EUR', 'EUR/USD', 'EUR/JPY',
            'EUR/CAD', 'EUR/GBP', 'EUR/AUD', 'EUR/NZD', 'EUR/CHF']
    info = [[markets[1], 'united states', get_forex]]*len(data)
    params = ['eurmajor', data, info, analysis_currency]
    make_market(params, isReload)


def compare_eugold(isReload=True):
    data = ['EUR/USD', 'Gold']
    info = [[markets[1], 'united states', get_forex],
            [markets[2], 'united states', get_commodities]]
    params = ['eugold', data, info, analysis_intermarket]
    make_market(params, isReload)


# -------------------------------------------------------
# ECB bid rate:
# taylor equation
# https://stackoverflow.com/questions/59380645/taylor-expansion-in-python
# https://www.quandl.com/data/BUNDESBANK/BBK01_SU0202-Ecb-Interest-Rates-For-Main-Refinancing-Operations-End-Of-Month
def get_ecb_bidrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BUNDESBANK', 'BBK01_SU0202')


def get_ger_rate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'OECD', 'KEI_IR3TIB01_DEU_ST_M')


# -------------------------------------------------------
# Debt (optional):
# https://www.quandl.com/data/FRED/DEBTTLDEA188A-Central-government-debt-total-of-GDP-for-Germany
def get_ger_debt(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'FRED', 'DEBTTLDEA188A')


# -------------------------------------------------------
# Economic calendar and predict index:
# ----------------------------
def get_ger_gdp(isReload=True):
    if isReload:
        get_economic_fred(currency, 'DEULORSGPNOSTSAM')


# ----------------------------
# Ger industrial:
# https://www.quandl.com/data/BCB/3778-Industrial-production-index-Germany
def get_ger_industrial(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BCB', '3778')


# ----------------------------
# CPI: already code
def get_ger_cpi(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'CPI_DEU')
        get_economic_quandl(currency, 'RATEINF', 'CPI_EUR')


# ----------------------------
# inflation: already code
def get_ger_inflation(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_EUR')
        get_economic_quandl(currency, 'RATEINF', 'INFLATION_DEU')


# ----------------------------
# Unemployment rate, Germany:
# https://www.quandl.com/data/BCB/3785-Unemployment-rate-Germany
def get_ger_unemploymentrate(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BCB', '3785')


# -------------------------------------------------------
# Money supply M3
def get_eurm3(isReload=True):
    if isReload:
        get_economic_quandl(
            currency, 'ECB', 'BSI_M_U2_Y_U_A80_A_Q_U4_0000_Z01_F')


# -------------------------------------------------------
# Harmonised Index Of Consumer Prices
def get_eurozone_hicp(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'BUNDESBANK',
                            'BBXP1_M_U2_N_HICP_000000_IND_I00')


def get_ger_budgetdeficit(isReload=True):
    if isReload:
        get_economic_quandl(currency, 'AMECO',
                            'DEU_1_0_0_0_UUTGE')