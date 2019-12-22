import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#To obtian the dataset
start = dt.datetime(2000,1,1)
end = dt.datetime(2019,7,11)

#Dataframe
df = web.DataReader('GS', 'yahoo', start, end)
df.to_csv('Goldmann Sachs.csv')

df = pd.read_csv('Goldmann Sachs.csv', parse_dates=True, index_col=0)

print(df.head())

df.plot()
plt.show()