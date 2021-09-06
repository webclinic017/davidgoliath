'''
1. diversify portfolio in short/ long term investments
2. analyze companies, expected return annual basis
3. analyze the average daily return in different date ranges:
(1 year - 3 year - 5 year)
'''
# -------------------- default template ------------------
import numpy as np
import pandas as pd
from pathlib import Path
from matplotlib import style
import matplotlib.pyplot as plt

style.use('fivethirtyeight')

if __name__ == "__main__":
    def process(quote):
        # for quote in quotes:
        path = Path(f'data/{quote}.csv')
        df = pd.read_csv(path, index_col="Date",
                         infer_datetime_format=True, parse_dates=True)
        df.rename(columns={"Close": f"{quote}"}, inplace=True)
        df.sort_values('Date', inplace=True)

        daily_return = df.pct_change()
        pct_xyear = []
        for i in range(1, 6, 2):
            # last day in dataset
            day = df.tail(1).index.day.tolist()[0]
            month = df.tail(1).index.month.tolist()[0]
            year = df.tail(1).index.year.tolist()[0]
            # combine then convert to datetime index
            before = pd.to_datetime(str(year - i)+'-'+str(month)+'-'+str(day))
            now = pd.to_datetime(str(year)+'-'+str(month)+'-'+str(day))
            # 1/3/5-Year Daily Returns
            daily_year = daily_return.loc[before:now]
            pct_xyear.append(daily_year)
        return pct_xyear

    amd_df = process('AMD')
    mu_df = process('MU')
    on_df = process('OnSemi')

    # # dump things: data set not same range
    # for i in range(3):
    #     Year_Returns = pd.concat([amd_df[i]['AMD'], mu_df[i]['MU'],
    #                               on_df[i]['OnSemi']], axis="columns",
    #                              join="outer")
    #     Year_Returns.plot()
    #     plt.show()

    items = ['AMD', 'MU', 'OnSemi']
    for i in range(3):
        for item in items:
            # print(
            #     f'{item} {2*i+1} year stats:\n{process(item)[i].describe()}')
            print(
                f'\n{item} {2*i+1} year stats:\n{process(item)[i].mean()*100}')
    pass
# ------------------ end default template -----------------
