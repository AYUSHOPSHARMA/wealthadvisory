import pandas as pd
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import numpy as np
import datetime
import matplotlib.pyplot as plt
import talib


end = datetime.date.today()
begin=end-pd.DateOffset(365*9)
st=begin.strftime('%Y-%m-%d')
ed=end.strftime('%Y-%m-%d')
yf.pdr_override() # <== that's all it takes :-)
 
data = pdr.get_data_yahoo('RELIANCE.NS',st,ed)

#SIMPLE MOVING AVERAGE
data['SMA_20'] = talib.SMA(np.asarray(data['Close']), 20)
data['SMA_50'] = talib.SMA(np.asarray(data['Close']), 50) 
data.plot(y= ['Close','SMA_20','SMA_50'], title='AAPL Close & Moving Averages')

#RSI
data['RSI_14'] = talib.RSI(np.asarray(data['Close']), 14)
data.plot(y= ['RSI_14'], title='AAPL RSI with 14 day cycle')


#Exponetial moving average
data['EMA_20'] = talib.EMA(np.asarray(data['Close']), 20)
data.plot(y= ['EMA_20'], title='AAPL EMA with 20 day cycle')

#Rate of change ROC
data['ROC'] = talib.ROC(np.asarray(data['Close']), 20)
data.plot(y= ['ROC'], title='AAPL ROC ')

#Bollinger Bands
#data['BBANDS'] = talib.BBANDS(np.asarray(data['Close']), timeperiod=20,nbdevup=2,nbdevdn=2,matype=0)
data['upper'],data['middle'],data['lower'] = talib.BBANDS(np.asarray(data['Close']), timeperiod=20,nbdevup=2,nbdevdn=2,matype=0)
data.plot(y= ['Close','upper','middle','lower'], title='AAPL BBBANDS')


#MACD
data['macd_talib'], data['signal'], data['diff_macd_signal'] = talib.MACD(np.asarray(data['Close']), fastperiod=12, slowperiod=26, signalperiod=9)
data.plot(y= ['macd_talib','signal','diff_macd_signal'], title='AAPL MACD')


#Stochastic Oscillator 
# stock oversold if below 10 , overbought if greater than 90
data['slowk'],data['slowd'] = talib.STOCH(np.asarray(data['High']),
                                            np.asarray(data['Low']),
                                            np.asarray(data['Close']),
                                            fastk_period=5,
                                            slowk_period=3,
                                            slowk_matype=0,
                                            slowd_period=3,
                                            slowd_matype=0)
                                                        
data.plot(y= ['slowk','slowd'], title='AAPL Stochastic Oscillator')

print("############RSI_14 ########")
print(data)