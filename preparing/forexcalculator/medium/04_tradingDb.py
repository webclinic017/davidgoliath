# -------------------- default template ------------------
import numpy as np
import pandas as pd
import hvplot.pandas
# import matplotlib.pyplot as plt
# from matplotlib import style
import yfinance as yf
from pathlib import Path

# style.use('fivethirtyeight')
pd.options.mode.chained_assignment = None  # default='warn'

if __name__ == "__main__":
    '''
    pull live data
    '''
    # # Cloudflare ltd, maybe use another code like TSLA ..
    # net = yf.Ticker('TSLA')
    # net_hist = net.history(start='2018-01-01', end='2021-05-26',
    #                        interval='1d')
    # net_hist.to_csv('data/TSLA.csv')

    net_hist = pd.read_csv('data/TSLA.csv')
    signal_df = net_hist.drop(columns=['Open', 'High', 'Low',
                                       'Volume', 'Dividends',
                                       'Stock Splits'])
    # --------------------------------------
    '''
    Set the Short and Long: pair MA(50, 100) or (20, 50)
    '''
    short_roll = 50
    long_roll = 100
    signal_df['SMA50'] = signal_df['Close'].rolling(window=short_roll).mean()
    signal_df['SMA100'] = signal_df['Close'].rolling(window=long_roll).mean()
    signal_df['Signal'] = 0.0
    # --------------------------------------
    '''
    Generate trading signals: 0 (SMA50 above SMA100) or 1
    '''
    signal_df['Signal'][short_roll:] = np.where(
        signal_df['SMA50'][short_roll:]
        > signal_df['SMA100'][short_roll:], 1.0, 0.0)
    signal_df['Entry/Exit'] = signal_df['Signal'].diff()
    # print(signal_df.tail())
    # --------------------------------------
    '''
    Plot Entry/Exit points
    # https://coderzcolumn.com/tutorials/data-science/how-to-convert-static-pandas-plot-matplotlib-to-interactive-hvplot
    # read more about pd.diff
    '''
    # Visualize exit pos
    exit_ = signal_df[signal_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
        color='red', legend=False, ylabel='Price in $',
        width=1000, height=400)
    # Visualize entry pos
    entry_ = signal_df[signal_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
        color='green', legend=False, ylabel='Price in $',
        width=1000, height=400)
    # Visualize close price
    close_ = signal_df[['Close']].hvplot(
        color='lightgray', ylabel='Price in $', width=1000, height=400)
    # Visualize moving averages
    ma = signal_df[['SMA50', 'SMA100']].hvplot(ylabel='Price in $',
                                               width=1000, height=400)
    # Overlay plots
    entry_exit_plt = close_*ma*entry_*exit_
    entry_exit_plt.opts(xaxis=None)
    # entry_exit_plt.plot()
    # --------------------------------------

    '''
    Backtest
    '''
    # --------------------------------------

    '''
    Analyze Portfolio metrics
    '''
    # --------------------------------------

    '''
    Serve Dashboard
    '''
    pass
# --------------------------------------
# ------------------ end default template -----------------
