import yfinance as yf
from pandas_datareader import data, wb

import pandas as pd
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2020, 1, 31)


df = data.get_data_yahoo('ISP.MI', start, end)

df.to_csv('ISP.csv')
print(df)


k = df['Adj Close'] / df['Close']

df['Adj Open'] = k * df['Open']
df['Adj High'] = k * df['High']
df['Adj Low'] = k * df['Low']

df['Close'].plot(label='Close')
df['Adj Close'].plot(label='Adj Close', ls=':')
plt.legend()
plt.show()


df.to_excel('ISP.xlsx')