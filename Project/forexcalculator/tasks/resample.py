import sys
import pandas as pd
import pandas_ta as ta
import investpy as iv
import numpy as np
from datetime import date, datetime
from calendar import monthrange


def find_days_in_month():
    today = date.today()
    first = today.replace(day=1)
    last = today.replace(day=monthrange(today.year, today.month)[1])
    return first, last


# def find_days_in_arange(*args):
def find_days_in_arange(day_range, interval='Daily'):
    '''
    Now only support Days and Weeks
    -> handle Months | Years TypeError issue

    * Daily: get when new day income
    * Weekly: get when new week income
    * Monthly: get when new month income
    '''
    interval_dict = {'Daily': 'D', 'Weekly': 'W'}
    end = date.today()
    start = np.datetime64(end) - \
        np.timedelta64(day_range, interval_dict[interval])

    start = np.datetime64(start).astype(datetime)
    return start, end


def convert_date(date):
    return date.strftime("%d/%m/%Y")


# Get data
def get_data(*inputs):
    # start, end = find_days_in_month()   # need changing this
    quote, interval, day_range = inputs
    start, end = find_days_in_arange(day_range, interval)
    start, end = convert_date(start), convert_date(end)  # can reuse
    print(start, end)
    # issue if current month not reach the end
    df = iv.commodities.get_commodity_historical_data(
        quote, start, end, interval=interval)
    # print(df.tail(10))
    # print(df)
    df.to_csv(f"data\\{quote}_{interval}.csv")
    return


# Load data
def load_data(quote, interval):
    df = pd.read_csv(f"data\\{quote}_{interval}.csv")
    df.drop('Currency', axis=1, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    # print(df.describe())
    # print(df.tail())
    return df


# apply caching to get | set data
def caching(*args, **kwargs):
    return


def upsampling(*args, **kwargs):
    return


def downsampling(*args, **kwargs):
    return


def resample(option=1):
    if option == 1:
        ''' get_data '''
        print("Example: I say get the fucking data out")
        # inputs = {"quote": "Gold",
        #           "country": "united states", "interval": "Daily"}
        # inputs = ("Gold", "Daily", 100)
        inputs = ("Gold", "Weekly", 21)
        get_data(*inputs)
    elif option == 2:
        ''' load_data '''
        quote, interval = "Gold", "Weekly"
        df = load_data(quote, interval)
        upsampled = df.resample('D').mean()
        methods = ['linear', 'from_derivatives']
        for method in methods:
            interpolated = upsampled.interpolate(method=method)
            interpolated.to_csv(f"data\\{quote}_{method}.csv")
    elif option == 3:
        ''' day_range customize '''
        find_days_in_arange(30)
    elif option == 4:
        ''' option_purpose '''
        pass
    elif option == 5:
        ''' option_purpose '''
        pass
    else:
        ''' option_purpose '''
        pass
    pass


def main():
    resample(int(sys.argv[1]))


if __name__ == "__main__":
    main()
