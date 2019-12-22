import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('Goldmann Sachs.csv', parse_dates=True, index_col=0)

#!00 moving averages
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df.tail())

axis1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
axis2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=axis1)

axis1.plot(df.index, df['Adj Close'])
axis1.plot(df.index, df['100ma'])
axis2.bar(df.index, df['Volume'])

plt.show()