# #######################################################
# -------------------------------------------------------
# get params then calculate corr
# muon lay param nao de so sanh cung dc

# Documentation of Fred api
# https://pypi.org/project/fredapi/
# https://github.com/MicroPyramid/forex-python
# https://pypi.org/project/datamine/

# chu kì kinh tế: 6 phần
# https://www.pringturner.com/business-cycle-stage-3-which-market-bullish-for/
# Giai đoạn 1: Trái phiếu tăng (lợi tức, cổ phiếu, hàng hóa giảm)
# Giai đoạn 2: Cổ phiếu tăng (trái phiếu tăng trong khi hàng hóa vẫn giảm)
# Giai đoạn 3: Hàng hóa tăng ( bond, stock và commondity cùng tăng)
# Giai đoạn 4: Trái phiếu giảm (lợi tức, cổ phiếu và hàng hóa vẫn tăng)
# Giai đoạn 5: Cổ phiếu giảm (trái phiếu giảm và hàng hóa tăng)
# Giai đoạn 6: Bond, stock và commondity cùng giảm

# 5 Nguyên tắc:

# 1. Dollar đang rớt giá, thì mua hàng hóa.

# 2. Mua hàng hóa khi cổ phiếu tăng, đặc biệt là Đồng hay Dầu

# 3. Mua cổ phiếu khi trái phiếu giảm

# 4. Sử dụng tỷ số Cổ phiếu/ Trái phiếu khi “dịch chuyển”ngành
# cổ phiếu có 10 ngành
# tỉ số tăng -> chú ý ngành tăng trưởng
# tỉ số tăng -> chú ý ngành phòng vệ

# 5. Chú ý đến thị trƣờng chứng khoán nƣớc ngoài
# thị trƣờng mới nổi quan hệ rất mật thiết với thị trƣờng hàng hóa.
# chứng khoán châu Âu thước đo nợ xấu
# chú ý các quỹ ETFs

# -------------------------------------------------------

# Mô hình nến + mô hình giá

# -------------------------------------------------------


# #######################################################

# --------------- THE MOST IMPORTANT THINGS ------------------
# 10Y treasury bond yeild (5Y, 2Y)
# how calculate bond spread (có thể cùng 1 QG hoặc khác) and yeild curve
# bond spread thu hẹp -> yeild curve phẳng hơn và có khả năng đảo ngược
# yield cao, đô và giá hàng hóa tăng lên và ngược lại
# bond kì hạn càng cao, rủi ro càng lớn, nên lợi tức càng phải cao
# nếu bond spread bất thường phải xem xét ngay

# giá bond đi ngược với yeild và thị trường vốn (stock)
# Khi yield tăng cao thì ngƣời ta tìm về các món hàng hóa như GOLD,
#  OIL, COPPER or bộ ba đồng tiền hàng hóa để go long ????


# Flatten yield curve

# Inverted yield curve

# so sánh với EU, GU
# ------------- import part ------------------------------
from alphautils import *

currency = 'usd'
# ------------------------------


def calculate_usbond(useQuandl=True, isReload=True):
    # https://www.quandl.com/data/USTREASURY-US-Treasury
    # dict of all treasury params
    ustreasury = {'USTREASURY': ['YIELD', 'REALYIELD',
                                 'BILLRATES', 'HQMYC',
                                 'MATDIS', 'AVMAT',
                                 'TNMBOR', 'TMBOR',
                                 'MKTDM', 'BRDNM']}
    main_key = list(ustreasury.keys())[0]
    # params = [useQuandl, isReload, currency, data, key]
    params = [useQuandl, isReload, 'usd', ustreasury, main_key]
    get_yeild(params)
    # https://www.investing.com/rates-bonds/u.s.-10-year-bond-yield
    # https://pypi.org/project/nelson-siegel-svensson/0.1.0/
    # https://pypi.org/project/yield-curve-dynamics/
    pass


# calculate_bond(useQuandl=True, isReload=True)


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
# so sánh với EU, GU


# https://www.cmegroup.com/trading/why-futures/welcome-to-cme-fx-futures.html#
# cme_calling()


# -------------------------------------------------------
# Economic calendar and predict index:
# GDP: https://www.quandl.com/data/FRED/GDP-Gross-Domestic-Product
# ----------------------------
# NFP: same direction Stock/ USD
# https://www.quandl.com/data/ACC/NFP-Non-Farm-Payrolls


# --------THE MOST IMPORTANT THINGS--------------------------------------

# FED fund rate: https://fred.stlouisfed.org/series/DFF
# ----------------------------

# CPI: already code
# ngược với stock/ bond và yeild

# ----------------------------
# inflation: already code - cùng chiều với yeild
# cùng chiều với lãi suất

# ----------------------------------------------------------------------


# Retail sales:
# https://www.quandl.com/data/FRED/RSXFS-Retail-Sales-Total-Excluding-Food-Services
# ----------------------------
# PMI: same direction Stock/ USD
# https://www.quandl.com/data/FRED/NAPM-ISM-Manufacturing-PMI-Composite-Index
# ----------------------------
# PPI:
# https://www.quandl.com/data/FRED/PPIACO-Producer-Price-Index-for-All-Commodities

# ----------------------------
# Unemployment rate ngược với lãi suất...
# ----------------------------
# Trade Balance ngược với lãi suất...
# ----------------------------
# Retail Sales cùng chiều với lãi suất
# -------------------------------------------------------
