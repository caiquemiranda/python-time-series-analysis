# necessary libs
import matplotlib.pyplot as plt     # visualization data
import seaborn as sns               # visualization data
import pandas as pd                 # manipulation data

# import data and tranform time-series
stock_prices = pd.read_csv('./data/stock_prices.csv', index_col='Date', parse_dates = ['Date'])

# daily returns 
daily_returns = stock_prices.pct_change()

# correlation matrix
correlations = daily_returns.corr()

# plot correlation matrix in seaborn
plt.figure(figsize=(12,6))
plt.title('Correlation Matrix')
sns.heatmap(correlations, annot=True, fmt='.2f', cmap='coolwarm');