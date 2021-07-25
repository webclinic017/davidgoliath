import alphautils as al
import pandas as pd
from operator import itemgetter
import math


def vol_sort(volume, order):
    return {k: v for k, v in sorted(volume.items(),
                                    key=itemgetter(order), reverse=True)}


def inner_vol_handle(args):
    quote, df, index, bias, enum = args
    dict_ = {}
    for num, name in enumerate(enum):
        temp = df.loc[index == num+bias]
        dict_[name] = temp['Pips'].mean()
    return dict_


def add_week_of_month(df):
    df['Week'] = pd.to_numeric(df.index.day/7)
    df['Week'] = df['Week'].apply(lambda x: math.ceil(x))
    return df


def forexvolatility(pairs, timeframe='Daily', periods=10):
    vols = {}
    timeframe_vol = {}
    WEEK_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    MONTH_WEEKS = ['1st', '2nd', '3rd', '4th', '5th']
    YEAR_MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                   'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for quote in pairs:
        df = pd.read_csv(f'investpy/currenciesdata/{quote}_{timeframe}.csv')
        df = df.iloc[-periods:]
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Monthly/ Weekly/ Daily Volatility
        df['Vol'] = ((df['High']-df['Low'])/df['Low']*100).abs()
        if 'JPY' in quote or 'XAG' in quote:
            df['Pips'] = ((df['High']-df['Low'])*100).abs()
        elif 'XAU' in quote:
            df['Pips'] = ((df['High']-df['Low'])*10).abs()
        else:
            df['Pips'] = ((df['High']-df['Low'])*10000).abs()
        vols.setdefault(quote, [df['Pips'].mean(), df['Pips'].std(),
                                df['Vol'].mean(), df['Vol'].std()])
        # vols.setdefault(quote, df['Pips'].mean())

        df['Year'] = df.index.year
        df['Month'] = df.index.month
        df = add_week_of_month(df)

        # Weekday Volatility In Pips
        if timeframe == "Daily":
            tmp = inner_vol_handle(
                (quote, df, df.index.dayofweek, 0, WEEK_DAYS))

        # Monthweek Volatility In Pips
        elif timeframe == "Weekly":
            tmp = inner_vol_handle(
                (quote, df, df['Week'], 1, MONTH_WEEKS))

        # Yearmonth Volatility In Pips
        else:
            tmp = inner_vol_handle(
                (quote, df, df['Month'], 1, YEAR_MONTHS))
        timeframe_vol.setdefault(quote, tmp)

        # Hourly Volatility Pips/GMT Hours

        # # Economic/ markets events
        # markethours()
        # economiccalendar()

        # rate
        # khác biệt cố hữu trong các động lực kinh tế của mỗi quốc gia
        # -> xu hướng biến động nhiều hơn
        # get_commodities / services (majors)
        # Most agricultura/ commodities such as oil are priced in U.S. dollars
        # Try to draw a chart like this for 8 currencies
        # anti-U.S. dollar or pro-U.S. dollar (kháng/ hỗ Dollar)
        # https://www.babypips.com/learn/forex/crosses-present-more-trading-opportunities
        majors = ['GBP/USD', 'EUR/USD', 'USD/CHF', 'USD/JPY']
        commodity_pairs = ['AUD/USD', 'USD/CAD', 'NZD/USD']

        # cặp chéo
        # https://www.babypips.com/learn/forex/cleaner-trends-and-ranges
        majorcrosses = ['EUR/CHF', 'EUR/GBP', 'EUR/JPY', 'GBP/JPY']
        minorcrosses = ['AUD/CHF', 'AUD/JPY', 'CAD/CHF', 'CAD/JPY',
                        'CHF/JPY', 'EUR/AUD', 'EUR/CAD', 'EUR/NZD',
                        'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/NZD',
                        'NZD/CHF', 'NZD/JPY']
    return df, vol_sort(vols, 1), timeframe_vol


'''
pairs = ['EURUSD', 'EURJPY', 'EURCAD', 'EURGBP', 'EURAUD', 'EURNZD',
         'EURCHF', 'GBPUSD', 'GBPJPY', 'GBPCAD', 'GBPAUD', 'GBPNZD',
         'GBPCHF', 'AUDUSD', 'AUDNZD', 'AUDJPY', 'AUDCAD', 'AUDUSD',
         'AUDCHF', 'NZDUSD', 'NZDJPY', 'NZDCAD', 'NZDUSD', 'NZDCHF',
         'CHFJPY', 'USDJPY', 'USDCHF', 'USDCAD', 'XAUUSD', 'XAGUSD']
periods_list = [12, 18, 24, 36]
timeframe = ['Daily', 'Weekly', 'Monthly']
'''
# pairs = ['GBPUSD', 'GBPJPY', 'GBPCAD', 'GBPAUD', 'GBPNZD', 'GBPCHF']
# pairs = ['EURUSD', 'EURJPY', 'EURCAD', 'EURCHF',
#          'EURAUD', 'EURNZD', 'EURGBP']
# pairs = ['AUDUSD', 'AUDNZD', 'AUDJPY', 'AUDCAD', 'AUDUSD', 'AUDCHF']
# pairs = ['NZDUSD', 'NZDJPY', 'NZDCAD', 'NZDUSD', 'NZDCHF']
pairs = ['CHFJPY', 'USDJPY', 'USDCHF', 'USDCAD', 'XAUUSD', 'XAGUSD']

# periods_list = [20, 50, 100, 200]
# timeframes = ['Daily']

# periods_list = [20, 25, 35, 50]
# timeframes = ['Weekly']

periods_list = [12, 18, 24, 36]
timeframes = ['Monthly']

for time_ in timeframes:
    filename = f'data/quant_res/Others_{time_}.txt'
    with open(filename, 'w'):
        pass
    for period in periods_list:
        df, daily_vol, time_vols = forexvolatility(
            pairs=pairs, timeframe=time_, periods=period)
        for quote, vol in daily_vol.items():
            mes = f"{quote}-{period}-{time_}: mean={int(vol[0])} pips | std="
            mes += f"{int(vol[1])} | cv={(vol[1]/vol[0]*100):.2f}\n"
            mes += "-------\n"
            if time_vols:
                intraday_vols = vol_sort(time_vols[quote], 1)
                for day, vol_ in intraday_vols.items():
                    tmp = 0 if math.isnan(vol_) else int(vol_)
                    mes += f"{day}: {tmp} pips\n"
            mes += "--------------\n"
            with open(filename, 'a') as f:
                f.write(mes)
