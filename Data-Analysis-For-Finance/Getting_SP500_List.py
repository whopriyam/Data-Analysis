import bs4 as bs
import pickle
import datetime as dt
import requests
import lxml
import os
import pandas as pd
from pandas_datareader import data as web

def save_sp500_tickers():
    resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find("table", { "class" : "wikitable sortable"}) 
    # print(soup)
    # print(soup.table)

    tickers = []
    for row in table.findAll("tr")[1:]:     #First row is table header
        ticker = row.findAll("td")[0].text #Table data
        tickers.append(ticker)
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers, f)
    print(tickers)
    
    return tickers

#save_sp500_tickers()

def get_data_from_yahoo(reload_sp500=False):
    
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2016,1,1)
    end = dt.datetime(2018,12,31)

    for ticker in tickers[:100]:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.get_data_yahoo('MMM', start, end,)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()