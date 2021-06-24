# -------------------- default template ------------------
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import datetime as dt
# from pandas_datareader import data as web
import investpy as iv
from random import randint

style.use('fivethirtyeight')

if __name__ == "__main__":
    tickers = ['FB', 'AAPL', 'AMZN', 'NFLX', 'MSFT', 'GOOGL']

    def get_data(amounts, leverage):
        current_balance = 1.512e5 * leverage
        prices = []
        total = []
        # get price
        for ticker in tickers:
            df = iv.stocks.get_stock_recent_data(ticker, 'united states')
            prices.append(df.tail(1).Close.values.tolist()[0])
        # loop to get totals
        for amount in amounts:
            total.append(int(current_balance*amount/100))
        return prices, total

    def randomList(hm, sum):
        arr = [0]*hm
        for i in range(sum):
            # counting number in specific pos
            arr[randint(0, sum) % hm] += 1
        return arr

    def create_portfolio():
        # random portfolio percent
        amounts = randomList(len(tickers), 100)
        prices, total = get_data(amounts, 1)
        # SET THE OUTLINE OF THE PIE CHART
        fig, ax = plt.subplots(figsize=(14, 7))

        ax.set_facecolor('black')
        ax.figure.set_facecolor('white')
        ax.tick_params(axis='x', colors='black')
        ax.tick_params(axis='y', colors='black')
        ax.set_title("Stock Portfolio", color='black', fontsize=20)

        _, texts, _ = ax.pie(amounts, labels=tickers,
                             autopct='%1.1f%%', pctdistance=0.8,
                             radius=0.75)
        [text.set_color('black') for text in texts]

        # ax.axis('equal')

        ax.text(-2, 1, 'PORTFOLIO OVERVIEW:', fontsize=16, color="red",
                horizontalalignment='center', verticalalignment='center')
        ax.text(-2, 0.85, f'Total USD Amount: ${sum(total):.2f}', fontsize=18,
                color="green", horizontalalignment='center',
                verticalalignment='center')
        counter = 0.15
        # print(prices)
        for count, ticker in enumerate(tickers):
            tol_money = total[tickers.index(ticker)]
            hm_ = int(tol_money/prices[count])
            ax.text(-2, 0.85 - counter,
                    f'{ticker}: ${tol_money: .2f} - {hm_} stocks',
                    fontsize=12, color="black", horizontalalignment='center',
                    verticalalignment='center')
            counter += 0.15
        plt.show()

    create_portfolio()

    pass
# ------------------ end default template -----------------
