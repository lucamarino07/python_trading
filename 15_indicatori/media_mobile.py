import matplotlib.dates as dates
import numpy as np
import yfinance as yf
from pandas_datareader import data, wb

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 1, 1)


df = data.get_data_yahoo('ISP.MI', start, end)
# df.to_excel('15_indicatori/ISP.xlsx')

df['50D SMA'] = df['Adj Close'].rolling(50).mean()
df['200D SMA'] = df['Adj Close'].rolling(200).mean()

df['Adj Close'].plot()
df['50D SMA'].plot()
df['200D SMA'].plot()
plt.legend(['ISP', 'SMA 50d', 'SMA 200d'])
plt.show()



n = 20
pesi = np.linspace(0, n, n)
df['20D WMA'] = df['Adj Close'].rolling(n).apply(lambda x: np.sum(pesi*x)/np.sum(pesi))
df['20D SMA'] = df['Adj Close'].rolling(20).mean()

df['Adj Close'].plot()
df['20D SMA'].plot()
df['20D WMA'].plot()

plt.legend(['ISP', 'SMA 20d', 'WMA 20d'])
plt.show()


df['50D EMA'] = df['Adj Close'].ewm(span=50).mean()
df['200D EMA'] = df['Adj Close'].ewm(span=200).mean()

df['Adj Close'].plot()
df['50D EMA'].plot()
df['200D EMA'].plot()
plt.legend(['ISP', 'EMA 50d', 'EMA 200d'])
plt.show()



df['Media BB'] = df['Adj Close'].rolling(20).mean()
df['Dev std 20'] = df['Adj Close'].rolling(20).std()


df['Banda Superiore'] = df['Media BB'] + 2 * df['Dev std 20']
df['Banda Inferiore'] = df['Media BB'] - 2 * df['Dev std 20']

df[['Adj Close', 'Media BB', 'Banda Superiore', 'Banda Inferiore']].plot()
plt.show()


df['Delta'] = df['Adj Close'].diff()
df['Delta'] = df['Delta'][1:]

U, D = df['Delta'].copy(), df['Delta'].copy()
U[U<0] = 0
D[D>0]=0

roll_up1 = U.rolling(14).mean()
roll_down1 = D.abs().rolling(14).mean()


RS = roll_up1 / roll_down1
RSI = 100.0 - (100.0 / (1.0 + RS))

df['ipercomprato'] = 70
df['ipervenduto'] = 30


fig, (ax1, ax2) = plt.subplots(2,1)

ax1.plot(df['Adj Close'], label='ISP')
ax2.plot(RSI, label='RSI')
ax2.plot(df['ipercomprato'], ls='--', color='r',label='')
ax2.plot(df['ipervenduto'], ls='--', color='r',label='')
ax1.legend()
ax2.legend()
plt.show()