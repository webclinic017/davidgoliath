import random

num = random.uniform(1.5, 1.9)
print(num)
start = 178
arr = [1, 2, 3, 4, 5, 7, 9, 11]
arr = [1, 1.095, 1.195, 1.295, 1.395, 1.59, 1.79, 1.995]
# arr = [1, 1.02, 1.03, 1.05, 1.07, 1.12, 1.15, 1.2]
for i in range(len(arr)):
    num = random.uniform(arr[i], 1.05*arr[i])
    # print(num)
    print(int(round(start*num, 0)))

'''
# pct change
pctValues['COO'] = round((pClose-pOpen)*100/pOpen, 5)
# interval range
pctValues['HLL'] = round((pHigh-pLow)*100/pLow, 5)

# bullish candlesticks
if pClose > pOpen:
    # short edge
    pctValues['HCC'] = round((pHigh-pClose)*100/pClose, 5)
    # long edge
    pctValues['OLL'] = round((pOpen-pLow)*100/pLow, 5)
    pctValues['HOL'] = round((pHigh-pOpen)*100/pLow, 5)
    pass
else:
    # short edge
    pctValues['HOO'] = round((pHigh-pOpen)*100/pOpen, 5)
    # long edge
    pctValues['CLL'] = round((pClose-pLow)*100/pLow, 5)
    pctValues['LOH'] = round((pLow-pOpen)*100/pHigh, 5)
    pass

# T.B.D named

pctValues['CLO'] = round((pClose-pLow)*100/pOpen, 5)
pctValues['COL'] = round((pClose-pOpen)*100/pLow, 5)
pctValues['HLO'] = round((pHigh-pLow)*100/pOpen, 5)
return pctValues
'''


df = pd.read_csv('investpy/currenciesdata/XAUUSD_Daily.csv')
# pct change
df['COO'] = round((df['Close']-df['Open'])*100/df['Open'], 5)
# entire lenght
df['HLL'] = round((df['High']-df['Low'])*100/df['Low'], 5)
# short edge
df['HCC'] = round((df['High']-df['Close'])*100/df['Close'], 5)
# long edge
df['CLL'] = round((df['Close']-df['Low'])*100/df['Low'], 5)
# bull/ bear domination all around
df['HOL'] = round((df['High']-df['Open'])*100/df['Low'], 5)
# bull/ bear Adj domination
df['CLO'] = round((df['Close']-df['Low'])*100/df['Open'], 5)
# real body
df['COL'] = round((df['Close']-df['Open'])*100/df['Low'], 5)
# strength volitality
df['HLO'] = round((df['High']-df['Low'])*100/df['Open'], 5)
# pct chage day previous close
df['PCT'] = round((df['Close']-df.shift()['Close'])*100/df['Close'], 5)
df.drop(['Open', 'High', 'Low', 'Close'], axis=1, inplace=True)
df.set_index('Date', inplace=True)
print(df.tail())
