import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np
import math

df = pd.read_csv('data/daily-total-female-births.csv')
rolled = df.rolling(window=3)
rolled_mean = rolled.mean()

# ------------- Put all in 1 figure -------------------
'''
# transform dataframe to numpy array
transform = df['Births'].to_numpy()

fig = plt.figure()

# print(rolled_mean.head(10))

# subplots define (lack of subplot title)
fig.add_subplot(221)
plt.plot(transform)

fig.add_subplot(222)
plt.plot(rolled_mean, color='red')

fig.add_subplot(223)
plt.plot(transform[:100], color='green')

fig.add_subplot(224)
plt.plot(rolled_mean[:100], color='blue')

plt.show()
'''
# ---------------------------------------------------------
# ------------- 2:2 chart -------------------
'''
transform = df['Births'].to_numpy()
plt.plot(transform)
plt.plot(rolled_mean, color='red')
plt.show()

# plot the first 100 observations
plt.plot(transform[:100])
plt.plot(rolled_mean[:100], color='red')
plt.show()
'''
# ---------------------------------------------------------
'''
# --- moving average smoothing as feature engineering ---
df = df['Births']
width = 3
lag1 = df.shift(1)
lag3 = df.shift(width-1)
window = lag3.rolling(window=width)
means = window.mean()
temp = pd.concat([means, lag1, df], axis=1)
temp.columns = ['mean', 't', 't+1']
print(temp.head(10))
'''
# --- moving average as Prediction ---
df = df['Births']
window = 3
history = [df[i] for i in range(window)]  # 3 first values
test = [df[i] for i in range(window, len(df))]  # 3 to last
predictions = []

# walk forward over time steps in test
# each loop add 1 day param then calculate mean of all
for t in range(len(test)):
    length = len(history)
    yhat = np.mean([history[i] for i in range(length-window, length)])
    obs = test[t]
    predictions.append(yhat)
    history.append(obs)
    # print(f'predicted={yhat}, expected={obs}')

rmse = math.sqrt(mean_squared_error(test, predictions))
print(f'Test RMSE: {rmse}')
# plot
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()
# zoom plot
plt.plot(test[:100])
plt.plot(predictions[:100], color='red')
plt.show()
