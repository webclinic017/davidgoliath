# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc
from alphautils import *
import usd as king
currency = 'eur'
country = 'euro zone'


# -------------------------------------------------------
# #######################################################
# https://www.investing.com/rates-bonds/germany-10-year-bond-yield
def calculate_bond(isReload=True):
    # DE bond yeild for investpy
    bonds = {'Germany 2Y': 'rates-bonds',
             'Germany 5Y': 'rates-bonds', 'Germany 10Y': 'rates-bonds'}
    intervals = ['Daily', 'Weekly', 'Monthly']
    if isReload:
        dump_things('debondyeild', bonds, country, get_bonds)
    else:
        pass


# calculate_bond(isReload=True)
# https://pypi.org/project/nelson-siegel-svensson/0.1.0/
# https://pypi.org/project/yield-curve-dynamics/


def calculate_bondspread(isReload=True):
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    # read data not reload
    if isReload:
        king.calculate_bond()
    pass


# -------------------------------------------------------
# ---------------------------- stock indices:
# Euro Stoxx 50: https://www.investing.com/indices/eu-stoxx50
def get_estoxx(isReload=True):
    if isReload:
        get_indices('Euro Stoxx 50', 'germany')
    # # optional
    # get_indices('EURO STOXX 50 Daily Short', 'euro zone')
    # get_indices('EURO STOXX 50 Daily Leverage', 'euro zone')


# DAX: https://www.investing.com/indices/germany-30
def get_dax(isReload=True):
    if isReload:
        get_indices('DAX', 'germany')


# -------------------------------------------------------
# Exy : prefer Weekly, Monthly data
def get_exy(isReload=True):
    # read data instead then analysis
    pass


# eur major cross: (EURUSD vs Gold)
def compare_major(isReload=True):
    intervals = ['Daily', 'Weekly', 'Monthly']
    quotes = ['XAU/EUR', 'EUR/USD', 'EUR/JPY',
              'EUR/CAD', 'EUR/GBP', 'EUR/AUD', 'EUR/NZD', 'EUR/CHF']
    market = [markets[1]]*len(quotes)
    pairs = dict(zip(quotes, market))
    if isReload:
        dump_things('eurmajor', pairs, country, get_currency_cross)
    else:
        analysis_currency_cross(filename)
        pass


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
