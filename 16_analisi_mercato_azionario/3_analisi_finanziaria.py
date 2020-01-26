import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.core.common.is_list_like = pd.api.types.is_list_like


isp = pd.read_csv('ISP.csv')
ubi = pd.read_csv('UBI.csv')
ucg = pd.read_csv('UCG.csv')

isp['rend'] = isp['Adj Close'].pct_change(1)
ubi['rend'] = ubi['Adj Close'].pct_change(1)
ucg['rend'] = ucg['Adj Close'].pct_change(1)

isp['rend'].hist(bins=100, label='ISP', figsize=(10,8), alpha=0.5)
ucg['rend'].hist(bins=100, label='UCG',  alpha=0.5)
ubi['rend'].hist(bins=100, label='UBI',  alpha=0.5)
plt.legend()
plt.show()

isp['rend'].plot(kind='kde', label='ISP')
ucg['rend'].plot(kind='kde', label='UCG')
ubi['rend'].plot(kind='kde', label='UBI')
plt.legend()
plt.show()

isp['Log_Ret'] = np.log(isp['Adj Close'] / isp['Adj Close'].shift(1))
ucg['Log_Ret'] = np.log(ucg['Adj Close'] / ucg['Adj Close'].shift(1))
ubi['Log_Ret'] = np.log(ubi['Adj Close'] / ubi['Adj Close'].shift(1))

isp['Vol'] = (isp['Log_Ret'].rolling(30).std()) * np.sqrt(252)
ucg['Vol'] = (ucg['Log_Ret'].rolling(30).std()) * np.sqrt(252)
ubi['Vol'] = (ubi['Log_Ret'].rolling(30).std()) * np.sqrt(252)

isp['Vol'].plot(label='ISP')
ucg['Vol'].plot(label='UCG')
ubi['Vol'].plot(label='UBI')
plt.legend()
plt.show()

print(isp['rend'].mean())
print(ucg['rend'].mean())
print(ubi['rend'].mean())


isp['Cum_ret'] = (1 + isp['rend']).cumprod()
ucg['Cum_ret'] = (1 + ucg['rend']).cumprod()
ubi['Cum_ret'] = (1 + ubi['rend']).cumprod()

isp['Cum_ret'].plot(label='ISP', title='Ritorno Cumulativo')
ucg['Cum_ret'].plot(label='UCG')
ubi['Cum_ret'].plot(label='UBI')
plt.legend()
plt.show()


print(isp['Cum_ret'])
print(ucg['Cum_ret'])
print(ubi['Cum_ret'])
