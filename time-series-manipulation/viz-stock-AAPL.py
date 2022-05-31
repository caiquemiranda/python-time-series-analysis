#necessary libs
import pandas as pd                   # manipulation data
import matplotlib.pyplot as plt       # visualization data

# import data and tranform time-series
stock = pd.read_csv('./data/AAPL-5Y.csv', parse_dates=['Date'], index_col='Date')

# 
stock.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=True)

# last price
print(stock.iloc[-1])

# visualization time-series
plt.figure(figsize=(10,5))
plt.title('Price APPL 5 years')
plt.xlabel('Date')
plt.ylabel('Price')
plt.plot(stock)
plt.show();
