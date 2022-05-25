# importações necessarias

import pstats
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

data = pd.read_csv('./data/AirPassengers.csv', 
                 sep=',',
                 parse_dates=True,
                 index_col=0).values


print(data[0:30])



pass