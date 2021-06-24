# -------------------- default template ------------------
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
from matplotlib import style

import warnings
warnings.filterwarnings('ignore')


style.use('fivethirtyeight')
# import scipy as sp

if __name__ == "__main__":
    '''
    read csv dataset
    LinearRegression: predict the relationship between 2 variables or factors
    MSE (Mean Squared Error): how accurate the model
    '''
    filePath = Path('data/gold_price.csv')
    df = pd.read_csv(filePath, parse_dates=True, index_col='Date')
    # ------------------------------------
    '''
    Return and Lagged Return
    drop any NaN values
    '''
    df['Return'] = df['USD (PM)'].pct_change()*100
    df['Lagged_Return'] = df.Return.shift()
    df.dropna(inplace=True)
    # ------------------------------------
    '''
    Plot
    '''
    # df['USD (PM)'].plot()
    # plt.show()
    # ------------------------------------
    '''
    Split the data set for Gold into Train & Test
    '''
    train = df['2001':'2018']
    test = df['2019']
    X_train = train['Lagged_Return'].to_frame()
    # print(type(X_train))  # pandas.core.frame.DataFrame
    y_train = train['Return']
    # print(type(y_train))  # pandas.core.series.Series
    X_test = test['Lagged_Return'].to_frame()
    y_test = test['Return']
    # ------------------------------------
    '''
    Create and Fit the model to our train data
    and test on out of sample data
    '''
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    # print(predictions)
    results = y_test.to_frame()
    # print(results)
    results['Predictions'] = model.predict(X_test)
    # print(results['Predictions'])

    # ------------------------------------
    '''
    Compare & Plot results
    '''
    # results.plot(subplots=True, title='Gold prices, USD')
    # plt.show()

    # ------------------------------------
    '''
    Analyze model predictions
    '''
    mse = mean_squared_error(results['Return'], results['Predictions'])
    rmse = np.sqrt(mse)
    # print(f'RMSE: {rmse} - MSE: {mse}')

    # ----- ----- ----- Rolling predictions ----- ----- -----
    # def rolling_predict(timeframe='week'):
    weeks = df.index.to_period('w').unique()
    # print(len(weeks))
    train_window = 12   # train_window = 1
    # why???
    timeframe = len(weeks) - train_window - 1
    # print(timeframe)
    '''
    new empty placeholder dataframes
    '''
    all_predictions = pd.DataFrame(columns=['Predictions'])
    all_actual_returns = pd.DataFrame(columns=['Actual Returns'])
    '''
    test the split datasets, append predictions into new DataFrame
    '''
    for i in range(0, timeframe):
        # train_window range
        start_of_train = weeks[i].start_time.strftime(format="%Y-%m-%d")
        end_of_train = weeks[train_window +
                             i].end_time.strftime(format="%Y-%m-%d")
        test_week = weeks[train_window+i+1]
        # test_week range
        start_of_test = test_week.start_time.strftime(format="%Y-%m-%d")
        end_of_test = test_week.end_time.strftime(format="%Y-%m-%d")

        train = df.loc[start_of_train:end_of_train]
        test = df.loc[start_of_test:end_of_test]
        # split process
        X_train = train['Lagged_Return'].to_frame()
        y_train = train['Return']
        X_test = test['Lagged_Return'].to_frame()
        y_test = test['Return']
        # training process
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        # -----------------------------------------------------------------
        # hold predictions to a DF
        predictions = pd.DataFrame(
            predictions, index=X_test.index, columns=['Predictions'])
        # hold actual returns to a DF
        actuals = pd.DataFrame(y_test, index=y_test.index)
        actuals.columns = ['Actual Returns']
        all_predictions = all_predictions.append(predictions)
        all_actual_returns = all_actual_returns.append(actuals)
    rets = pd.concat([all_actual_returns, all_predictions], axis=1)
    # print(rets.head())
    rets_2019 = rets.loc['2019':]
    # print(rets_2019)
    rets_2019.plot(subplots=True)
    # plt.show()
    '''
    # metrics: mse between actual and prediction
    '''
    mse = mean_squared_error(
        rets_2019['Actual Returns'], rets_2019['Predictions'])
    rolling_rmse = np.sqrt(mse)
    # print(f'Rolling RMSE: {rolling_rmse} - MSE: {mse}')
    print(f'Rolling RMSE: {rolling_rmse}\nRMSE: {rmse}')
    pass
# ------------------ end default template -----------------
