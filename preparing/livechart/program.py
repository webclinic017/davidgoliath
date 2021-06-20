#############################################################
# resource data:
# https://stackoverflow.com/questions/44604440/forex-historical-data-in-python
#############################################################
"""
import investpy as iv
import pandas as pd
if __name__ == "__main__":
    # def get_data():
    # get data
    df = iv.commodities.get_commodity_historical_data(
        'gold', from_date='01/01/2021',
        to_date='10/06/2021', order='ascending')
    df = df.iloc[:, :-1]
    df.to_csv('Data/Gold.csv')

    # read data
    df = pd.read_csv('Data/Gold.csv')
    df.set_index('Date', inplace=True)
    # print(df.tail())
"""
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time
# import duka

if __name__ == "__main__":
    # fig, ax1 = plt.subplots(1, 1)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    def animate(i):
        pullData = open('Data/sample.txt', 'r').read()
        dataArray = pullData.split('\n')
        xar = []
        yar = []
        for eachLine in dataArray:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xar.append(int(x))
                yar.append(int(y))
        ax1.clear()
        ax1.plot(xar, yar)
    ani = anim.FuncAnimation(fig, animate, interval=1000)
    plt.show()
