import requests
import pandas as pd
from pprint import PrettyPrinter
import numpy as np
# import forex_python

# -----------------------------
# https://tradermade.com/tutorials/fetch-forex-api-with-python-and-pandas/
# -----------------------------

pp = PrettyPrinter()

if __name__ == "__main__":
    api_key = "tmchMkOIlm0CyLsdUgSj"
# -----------------------------------------------------------------------
    """ # Calling real-time forex rates using live endpoint
    url = "https://marketdata.tradermade.com/api/v1/live"
    currencies = "USDCAD,GBPUSD"
    querystring = {"currency": currencies, "api_key": api_key}
    response = requests.get(url, params=querystring)
    # pp().pprint(response.json())

    df = pd.DataFrame(response.json()["quotes"])
    # print(df)

    # # if all instruments are currencies just write a
    # # # in front of line 1 and take # off line 2 in the below code.
    # # If all instruments are CFDs just write # in line 1 and 2.
    # df['instrument'] = np.where(df["base_currency"].isnull(
    # ), df["instrument"], df["base_currency"]+df["quote_currency"])
    df["instrument"] = df["base_currency"]+df["quote_currency"]
    df["timestamp"] = response.json()["timestamp"]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    df = df[['instrument', 'bid', 'mid', 'ask', 'timestamp']]
    # print(df)
    df.T.to_csv('Data/live_rates.csv')
    """
# -----------------------------------------------------------------------
    url = "https://marketdata.tradermade.com/api/v1/historical"
    date = "2021-06-10"
    # # Minute and hour Historical
    # dates = ["2021-03-15-13:00"]
    # array = []
    currencies = "GBPUSD"
    querystring = {"currency": currencies, "date": date, "api_key": api_key}
    response = requests.get(url, params=querystring)
    df = pd.DataFrame.from_dict(
        response.json()["quotes"], orient='columns', dtype=None, columns=None)
    # df["instrument"] = np.where(df["base_currency"].isnull(
    # ), df["instrument"], df["base_currency"]+df["quote_currency"])
    df["instrument"] = df["base_currency"]+df["quote_currency"]
    df["date"] = response.json()["date"]
    df["date"] = pd.to_datetime(df["date"])
    df = df[['instrument', 'open', 'high', 'low', 'close', 'date']]
    # print(df)
