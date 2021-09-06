markets = ['indices', 'currencies', 'commodities',
           'rates-bonds', 'equities', 'etfs', 'crypto']
combine_path = 'investpy/combinedata/'
# global starttime
starttime = '01/01/2010'
analysis_path = 'investpy/analysisdata/'


def round_nums(arr):
    res = []
    for num in arr:
        res.append(round(num, 4))
    return res


# improve 1 candle vs multicandle (2 or more)
def fibocalculator(source="investpy/currenciesdata/", quotes='USDCHF',
                   interval='Monthly', periods=15):
    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    df = df.iloc[-periods-1:]
    low = df['Low'].min()
    high = df['High'].max()
    # get index
    last_pos = df.index.tolist()[len(df)-1]
    low_index, high_index = df.loc[df['Low'] ==
                                   low].index, df.loc[df['High'] == high].index
    isUptrend = True if (high_index - low_index > 0) else False
    fiboret_level = (0.236, 0.382, 0.5,
                     0.618, 0.707, 0.786, 0.887)
    fiboexp_level = (-0.382, -0.236, 0, 0.236, 0.5,
                     0.618, 0.786, 1, 1.272, 1.618)
    # process uptrend price level
    print(isUptrend)
    if isUptrend:
        high_pos = high_index.tolist()[0]
        retrace = df[high_pos-last_pos-1:]['Low'].min()
        # Fibonnaci path
        price_ret = [round((1-level)*(high-low) + low, 4)
                     for level in fiboret_level]
        price_ret.reverse()
        price_ret.append(high)
        price_ret.insert(0, low)

        # Fibonacci Expansion:
        price_exp = [round(level*(high-low) + retrace, 4)
                     for level in fiboexp_level]
    # downtrend
    else:
        low_pos = low_index.tolist()[0]
        retrace = df[low_pos-last_pos-1:]['High'].max()
        # Fibonnaci path
        price_ret = [round(low + level*(high-low), 4)
                     for level in fiboret_level]
        price_ret.reverse()
        price_ret.append(low)
        price_ret.insert(0, high)

        # Fibonacci Expansion:
        price_exp = [round(retrace - level*(high-low), 4)
                     for level in fiboexp_level]
    return (price_ret, price_exp, isUptrend)


def pivotpointcalculator(pivotType='Fibonacci',
                         source='investpy/currenciesdata/',
                         quotes='USDCHF', interval='Monthly'):
    ret = []
    df = pd.read_csv(source + f'/{quotes}_{interval}.csv')
    pOpen, pHigh, pLow, pClose = df.iloc[-1:, 1:5].values.tolist()[0]
    # Classic
    if pivotType is 'Classic':
        pp = (pHigh + pLow + pClose) / 3
        S1 = pp*2 - pHigh
        S2 = pp - (pHigh-pLow)
        S3 = pp - 2*(pHigh-pLow)

        R1 = pp*2 - pLow
        R2 = pp + (pHigh-pLow)
        R3 = pp + 2*(pHigh-pLow)

        ret = round_nums([R3, R2, R1, pp, S1, S2, S3])
        print(ret)
    # Fibonacci
    if pivotType is 'Fibonacci':
        pp = (pHigh + pLow + pClose) / 3

        R1 = pp + ((pHigh-pLow)*0.382)
        R2 = pp + ((pHigh-pLow)*0.618)
        R3 = pp + ((pHigh-pLow)*1)

        S1 = pp - ((pHigh-pLow)*0.382)
        S2 = pp - ((pHigh-pLow)*0.618)
        S3 = pp - ((pHigh-pLow)*1)

        ret = round_nums([R3, R2, R1, pp, S1, S2, S3])
        print(ret)
    # Camarilla
    if pivotType is 'Camarilla':
        pp = (pHigh + pLow + pClose) / 3

        S1 = pClose - ((pHigh-pLow) * 1.0833)
        S2 = pClose - ((pHigh-pLow) * 1.1666)
        S3 = pClose - ((pHigh-pLow) * 1.25)
        S4 = pClose - ((pHigh-pLow) * 1.5)

        R1 = pClose + ((pHigh-pLow) * 1.0833)
        R2 = pClose + ((pHigh-pLow) * 1.1666)
        R3 = pClose + ((pHigh-pLow) * 1.25)
        R4 = pClose + ((pHigh-pLow) * 1.5)

        ret = round_nums([R4, R3, R2, R1, pp, S1, S2, S3, S4])
        print(ret)
    # Woodie's
    if pivotType is 'Woodie':
        pp = (pHigh + pLow + 2*pClose) / 4

        R1 = 2*pp - pLow
        R2 = pp + pHigh - pLow
        R3 = (pHigh + 2 * (pp - pLow))

        S1 = 2*pp - pHigh
        S2 = pp - pHigh + pLow
        S3 = (pLow - 2 * (pHigh - pp))

        ret = round_nums([R3, R2, R1, pp, S1, S2, S3])
        print(ret)
    # DeMark's
    if pivotType is 'DeMark':
        if pClose > pOpen:
            X = 2*pHigh + pLow + pClose
        elif pClose < pOpen:
            X = pHigh + 2*pLow + pClose
        else:
            X = pHigh + pLow + 2*pClose
        pp = X/4
        R1 = X/2 - pLow
        S1 = X/2 - pHigh

        ret = round_nums([R1, pp, S1])
        print(ret)
    return ret
