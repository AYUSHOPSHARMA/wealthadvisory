import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
from pandas_datareader import data as web
from pylab import plt
import fix_yahoo_finance as yf
# import cufflinks
plt.style.use('seaborn')
##%matplotlib inline

import datetime
end = datetime.date.today()
begin=end-pd.DateOffset(365*9)

yf.pdr_override()

#timestamp format and get apple stock.
st=begin.strftime('%Y-%m-%d')
ed=end.strftime('%Y-%m-%d')
data = pdr.get_data_yahoo('SBIN.NS',st,ed)

data['Close'].plot(figsize=(10, 6));

data['SMA1'] = data['Close'].rolling(15).mean()

data['SMA2'] = data['Close'].rolling(60).mean()

data.head()

data.tail()

data[['Close', 'SMA1', 'SMA2']].plot(figsize=(10, 6));

data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)

data.dropna(inplace=True)

data.head()

data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)

data.dropna(inplace=True)

data.head()

data[['Close', 'SMA1', 'SMA2', 'Position']].plot(figsize=(10, 6), secondary_y='Position');

data.tail()

data.head()

data['Close'].shift(1).head()


#np.log(data['Close'] / data['Close'].shift(1).head())

data['Returns'] = np.log(data['Close'] / data['Close'].shift(1))

data.dropna(inplace=True)


data['Strategy'] = data['Position'].shift(1) * data['Returns']

data.tail()

#data[['Returns', 'Strategy']].dropna().cumsum(
#                ).apply(np.exp).plot(figsize=(10, 6));

plt.show()
