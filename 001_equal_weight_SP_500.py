import numpy as np
import pandas as pd
import math
import requests
import xlsxwriter

stocks = pd.read_csv("sp_500_stocks.csv")

from my_secrets import IEX_CLOUD_API_TOKEN

stock = "AAPL"
api_url = f"https://api.iex.cloud/v1/data/core/QUOTE/{stock}/?token={IEX_CLOUD_API_TOKEN}"
data = requests.get(api_url).json()
'''
[{'avgTotalVolume': 57582206, 'calculationPrice': 'iexlasttrade', 
'change': -0.78, 'changePercent': -0.00407, 'close': None, 
'closeSource': 'official', 'closeTime': None, 'companyName': 'Apple Inc', 
'currency': 'USD', 'delayedPrice': None, 'delayedPriceTime': None, 
'extendedChange': None, 'extendedChangePercent': None, 'extendedPrice': None, 
'extendedPriceTime': None, 'high': None, 'highSource': None, 'highTime': None, 'iexAskPrice': 
0, 'iexAskSize': 0, 'iexBidPrice': 0, 'iexBidSize': 0, 'iexClose': 190.67, 
'iexCloseTime': 1700600399415, 'iexLastUpdated': 1700600399415, 'iexMarketPercent': 0.017634576394237426, 
'iexOpen': 191.43, 'iexOpenTime': 1700577000300, 'iexRealtimePrice': 190.67, 'iexRealtimeSize': 10, 
'iexVolume': 672445, 'lastTradeTime': 1700600399998, 'latestPrice': 190.67, 'latestSource': 'IEX Last Trade', 
'latestTime': 'November 21, 2023', 'latestUpdate': 1700600399415, 'latestVolume': None, 'low': None, 
'lowSource': None, 'lowTime': None, 'marketCap': 2965443223840, 'oddLotDelayedPrice': None, 
'oddLotDelayedPriceTime': None, 'open': None, 'openTime': None, 'openSource': 'official', 'peRatio': 31.1, 
'previousClose': 191.45, 'previousVolume': 46538614, 'primaryExchange': 'NASDAQ', 'symbol': 'AAPL', 'volume': None, 
'week52High': 197.18, 'week52Low': 123.15, 'ytdChange': 0.48160712577155107, 'isUSMarketOpen': False}]
'''

price = data[0]['latestPrice']
market_cap = data[0]['marketCap']


