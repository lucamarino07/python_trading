import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_finance import candlestick2_ohlc

df = pd.read_excel('ISP.xlsx')

df.index = df['Date']

df['g_m_a'] = df['Date'].apply(lambda x: x.strftime('%d-%m-%Y'))

fig, ax = plt.subplots(figsize=(12, 9))

cl = candlestick2_ohlc(ax, opens=df['Open'],
                       highs=df['High'],
                       lows=df['Low'],
                       closes=df['Close'],
                       width=0.4, colorup='#77d879',
                       colordown='#db3f3f'
                       )
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df['g_m_a'], fontsize=8, rotation=45)
ax.set_xlim(0,30)
ax.set_ylim(1.78,2.15)
plt.show()