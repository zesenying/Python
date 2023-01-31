import pandas as pd
from yahoofinancials import YahooFinancials as YF
import yfinance as yf
import yahoo_fin as yahoof
import tickers

class stock:
    def __init__(self,ticker): 
        self.ticker = ticker
        self.s = YF(ticker)
        print('Initialize done')
        
    def get_fin(self):
        
        print('getting data...')
        fin = {}
        for stmt in ['income','balance','cash']:
            fin[stmt] = self.s.get_financial_stmts('Quarterly', stmt)
        
        return fin


if __name__ == '__main__':
    

    dic = {}
    for ticker in tickers.dow_list:
        try:
            print(ticker)
            s = stock(ticker)
            d = s.get_fin()
            dic[ticker] = d
        except:
            print('error')

    print(dic)









print('done')

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
    
#     return "<p>Hello, World!</p>"
