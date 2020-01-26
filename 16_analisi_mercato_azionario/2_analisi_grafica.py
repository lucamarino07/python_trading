import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb
import yfinance as yf
import datetime
from pandas.plotting import scatter_matrix

isp = pd.read_csv('ISP.csv')
ubi = pd.read_csv('UBI.csv')
ucg = pd.read_csv('UCG.csv')

# isp['Open'].plot(label='ISP', title='Open Price')
# ucg['Open'].plot(label='UCG')
# ubi['Open'].plot(label='UBI')
# plt.legend()
# plt.show()
#
# isp['Volume'].plot(label='ISP', title='Volume Tradato')
# ucg['Volume'].plot(label='UCG')
# ubi['Volume'].plot(label='UBI')
# plt.legend()
# plt.show()

isp.index = isp['Date']
ucg.index = ucg['Date']
ubi.index = ubi['Date']

print(isp['Volume'].argmax())

isp['Totale Tradato'] = isp['Close'] * isp['Volume']
ucg['Totale Tradato'] = ucg['Close'] * ucg['Volume']
ubi['Totale Tradato'] = ubi['Close'] * ubi['Volume']

isp['Totale Tradato'].plot(label='ISP')
ucg['Totale Tradato'].plot(label='UCG')
ubi['Totale Tradato'].plot(label='UBI')
plt.legend()
plt.ylabel('Totale Valore Tradato')
plt.show()

print(isp['Totale Tradato'].argmax())

bank_comp = pd.concat([isp['Close'], ubi['Close'], ucg['Close']], axis=1)
bank_comp.columns = ['ISP', 'UBI', 'UCG']
scatter_matrix(bank_comp,
               figsize=(8, 8),
               alpha=0.2,
               hist_kwds={'bins': 50})
plt.show()


