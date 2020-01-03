import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2019,7,11)

#Dataframe
df = web.DataReader('MSFT', 'yahoo', start, end)
print(df.tail(7))

