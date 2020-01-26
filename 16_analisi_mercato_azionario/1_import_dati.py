import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data, wb
import yfinance as yf
import datetime


start = datetime.datetime(2014,1,1)
end = datetime.datetime(2019,3,1)

df = data.get_data_yahoo('ISP.MI', start, end)
df.to_csv('ISP.csv')
df = data.get_data_yahoo('UCG.MI', start, end)
df.to_csv('UCG.csv')
df = data.get_data_yahoo('UBI.MI', start, end)
df.to_csv('UBI.csv')
