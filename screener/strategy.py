from django.shortcuts import render
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
from pylab import plt
import datetime
from mpld3._display import display_d3,fig_to_html,save_json
from mpld3 import plugins
import fix_yahoo_finance as yf
import talib
import io
import mpld3
from batchprocessing.models import nifty_200_companies
from PIL import Image
from datetime import datetime as dt
from batchprocessing.models import nift50Indices
import matplotlib.pyplot as pplt
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.metrics import categorical_accuracy
import random
random.seed(42)
import talib as ta

def getSMAStrategy(request,company,begin):
    # import cufflinks
    smafig = []
    plt.style.use('seaborn')
    ##%matplotlib inline
    
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
    
    stdt=dt.strptime(begin,'%Y-%m-%d')
    #timestamp format and get apple stock.
    st=stdt.strftime('%Y-%m-%d')
    ed=end.strftime('%Y-%m-%d')
    yf.pdr_override()
    print(st)
    print(ed)
    symbol= company+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close'])
    print(dataframe)
    data=dataframe.astype(float)
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
    
    ax=data[['Close', 'SMA1', 'SMA2', 'Position']].plot(figsize=(10, 6), secondary_y='Position');
    
    print("##########AX#######")
    print(ax)
     
    data.tail()
    
    data.head()
    
    
    
    data['Close'].shift(1).head()
    
    
    #np.log(data['Close'] / data['Close'].shift(1).head())
    
    data['Returns'] = np.log(data['Close'] / data['Close'].shift(1))
    
    data.dropna(inplace=True)
    
    print("##########Returns#######")
    print(data['Returns'])    
    
    data['Strategy'] = data['Position'].shift(1) * data['Returns']
    
    print("#########33Data Strategy########")
    print(data['Strategy'])
    data.tail()
    
    
    data[['Returns', 'Strategy']].dropna().cumsum(
                    ).apply(np.exp).plot(figsize=(10, 6));
    
    smafig.append(fig_to_html(plt.gcf()))
    return fig_to_html(plt.gcf())


def getStrategy(request):
     smafig = getSMAStrategy(request,9)
     bbbandGraph=view_indices_chart(request,"SBIN.NS",9)
     return render(request,"stratergyOption.html",{"smadata":smafig,"bbbandGraph":bbbandGraph})

def view_indices_chart(request,companyname,begin):
     #from pandas.plotting import scatter_matrix
	#end = datetime.date(2018,5,5)
	#begin = datetime.date(2017,1,1)
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.
    st=dt.strptime(begin,'%Y-%m-%d')
    #st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')

    #yf.pdr_override() # <== that's all it takes :-)
    
    fig, ax = plt.subplots()
    
    #data = pdr.get_data_yahoo(companyname,st,ed)
    symbol= companyname+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close','Open','High','Low')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close','Open','High','Low'])
    print(dataframe)
    data=dataframe.astype(float)
    print(data)
    if len(data) > 0:
        data = data.dropna()
        data['Open'],data['High'],data['Low'] = talib.BBANDS(np.asarray(data['Close']), timeperiod=30,nbdevup=1,nbdevdn=1,matype=0)
        data['Buy'] = data.apply(lambda x : 1 if x['Close'] < x['Low']  else 0, axis=1)
        data['Sell'] = data.apply(lambda y : 1 if y['Close'] > y['Open']  else 0, axis=1)
        data.plot(y= ['Close','Open','High','Low'], title=companyname+' BBBANDS',figsize=(10,10),grid=True)
        
        fig1 = plt.gcf()

        
        fig_html = mpld3.fig_to_html(fig1)
        #fig1.savefig(byte_file, format='png')
        #image_file= byte_file.getvalue()
        # fig, ax = plt.subplots(figsize=(500,500))
        #ax.grid(True)
        # fig.ylabel('Weight')
        # fig.title('Minutes')
        #ax.set_title('ax1 title')
    
    else:
        data['Open'],data['High'],data['Low'] = talib.BBANDS(np.asarray(data['Close']), timeperiod=30,nbdevup=1,nbdevdn=1,matype=0)
        data['Buy'] = data.apply(lambda x : 1 if x['Close'] < x['Low']  else 0, axis=1)
        data['Sell'] = data.apply(lambda y : 1 if y['Close'] > y['Open']  else 0, axis=1)
        plt.figure(figsize=(500,500))
        graph =data.plot(y= ['Close','Open','High','Low'], title=companyname+' BBBANDS',figsize=(10,10),grid=True)
        fig_html = mpld3.fig_to_html(graph)
    return fig_html

def machineLearningChart(request,companyname,begin):
    
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.
    st=dt.strptime(begin,'%Y-%m-%d')
    #st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')
    
    symbol= companyname+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close','Open','High','Low')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close','Open','High','Low'])
    print(dataframe)
    df=dataframe.astype(float)
    print(df)
    #df = pdr.get_data_yahoo('SBIN.NS', '2016-01-01', '2018-04-01')
    df = df.dropna()
    df = df.iloc[:,:4]
    df.head()

    #dataset = pd.read_csv('RELIANCE.NS.csv')
    #dataset = dataset.dropna()
    dataset = df[['Open', 'High', 'Low', 'Close']]
    
    dataset['H-L'] = dataset['High'] - dataset['Low']
    dataset['O-C'] = dataset['Close'] - dataset['Open']
    dataset['3day MA'] = dataset['Close'].shift(1).rolling(window = 3).mean()
    dataset['10day MA'] = dataset['Close'].shift(1).rolling(window = 10).mean()
    dataset['30day MA'] = dataset['Close'].shift(1).rolling(window = 20).mean()
    dataset['Std_dev']= dataset['Close'].rolling(10).std()
    dataset['RSI'] = ta.RSI(dataset['Close'].values, timeperiod = 9)
    dataset['Williams %R'] = ta.WILLR(dataset['High'].values, dataset['Low'].values, dataset['Close'].values, 7)
    
    
    dataset['Price_Rise'] = np.where(dataset['Close'].shift(-1) > dataset['Close'], 1, 0)
    
    dataset = dataset.dropna()
    
    X = dataset.iloc[:, 4:-1]
    y = dataset.iloc[:, -1]
    
    split = int(len(dataset)*0.8)
    X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]
    
    
   
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    
    
    
    
    classifier = Sequential()
    
    classifier.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu', input_dim = X.shape[1]))
    
    
    classifier.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
    
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    
    #classifier.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])
    
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    
    #model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[categorical_accuracy])
    
    
    classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)
    
    
    y_pred = classifier.predict(X_test)
    #y_pred = (y_pred > 0.5)
    
    
    dataset['y_pred'] = np.NaN
    dataset.iloc[(len(dataset) - len(y_pred)):,-1:] = y_pred
    trade_dataset = dataset.dropna()
    
    
    
    
    trade_dataset['Tomorrows Returns'] = 0.
    trade_dataset['Tomorrows Returns'] = np.log(trade_dataset['Close']/trade_dataset['Close'].shift(1))
    trade_dataset['Tomorrows Returns'] = trade_dataset['Tomorrows Returns'].shift(-1)
    
    
    trade_dataset['Strategy Returns'] = 0.
    
    trade_dataset['y_pred'] = np.where(trade_dataset['y_pred'] < 0.5, 0,1)
    
    
    trade_dataset['Strategy Returns'] = np.where(trade_dataset['y_pred'] == 1, trade_dataset['Tomorrows Returns'], - trade_dataset['Tomorrows Returns'])
    
    
    trade_dataset['Cumulative Market Returns'] = np.cumsum(trade_dataset['Tomorrows Returns'])
    trade_dataset['Cumulative Strategy Returns'] = np.cumsum(trade_dataset['Strategy Returns'])
    
    
    
    pplt.figure(figsize=(10,5))
    pplt.plot(trade_dataset['Cumulative Market Returns'], color='r', label='Market Returns')
    pplt.plot(trade_dataset['Cumulative Strategy Returns'], color='g', label='Strategy Returns')
    #plt.plot(trade_dataset['Tomorrows Returns'], color='b', label='Tom Returns')
    pplt.legend()
    fig = pplt.gcf()
    #pplt.show()
    fig_html = mpld3.fig_to_html(fig)
    return fig_html

def rsiStretagy(request,companyname,begin):
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.
    st=dt.strptime(begin,'%Y-%m-%d')
    #st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')
    symbol= companyname+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close','Open','High','Low')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close','Open','High','Low'])
    print(dataframe)
    data=dataframe.astype(float)
    #data = pdr.get_data_yahoo('RELIANCE.NS',st,ed)
    
    #RSI
    data['RSI_14'] = talib.RSI(np.asarray(data['Close']), 14)
    graph=data.plot(y= ['RSI_14'], title=companyname+' RSI with 14 day cycle')
    graph = plt.gcf()
    fig_html = mpld3.fig_to_html(graph)
    return fig_html
    
def emaStretagy(request,companyname,begin):
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.
    st=dt.strptime(begin,'%Y-%m-%d')
    #st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')
    symbol= companyname+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close','Open','High','Low')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close','Open','High','Low'])
    print(dataframe)
    data=dataframe.astype(float)
    #data = pdr.get_data_yahoo('RELIANCE.NS',st,ed)
    
    #Exponetial moving average
    data['EMA_20'] = talib.EMA(np.asarray(data['Close']), 20)
    graph=data.plot(y= ['EMA_20'], title=companyname+' EMA with 20 day cycle')
    graph = plt.gcf()
    fig_html = mpld3.fig_to_html(graph)
    return fig_html
    
def rocStretagy(request,companyname,begin):
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.
    st=dt.strptime(begin,'%Y-%m-%d')
    #st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')
    symbol= companyname+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close','Open','High','Low')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close','Open','High','Low'])
    print(dataframe)
    data=dataframe.astype(float)
    #data = pdr.get_data_yahoo('RELIANCE.NS',st,ed)
   
    #Rate of change ROC
    data['ROC'] = talib.ROC(np.asarray(data['Close']), 20)
    graph=data.plot(y= ['ROC'], title=companyname+' ROC ')
    graph = plt.gcf()
    fig_html = mpld3.fig_to_html(graph)
    return fig_html
    
def macdStretagy(request,companyname,begin):
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.
    st=dt.strptime(begin,'%Y-%m-%d')
    #st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')
    symbol= companyname+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close','Open','High','Low')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close','Open','High','Low'])
    print(dataframe)
    data=dataframe.astype(float)
    #data = pdr.get_data_yahoo('RELIANCE.NS',st,ed)
           
    #MACD
    data['macd_talib'], data['signal'], data['diff_macd_signal'] = talib.MACD(np.asarray(data['Close']), fastperiod=12, slowperiod=26, signalperiod=9)
    graph=data.plot(y= ['macd_talib','signal','diff_macd_signal'], title=companyname+' MACD')
    graph = plt.gcf()
    fig_html = mpld3.fig_to_html(graph)
    return fig_html
    
    
def soStretagy(request,companyname,begin):
    end = datetime.date.today()
    #begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.
    st=dt.strptime(begin,'%Y-%m-%d')
    #st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')
    symbol= companyname+".NS"
    datanifty=nift50Indices.objects.filter(Ticker=symbol).values_list('Close','Open','High','Low')
    #data = pdr.get_data_yahoo(company,st,ed)
    dataframe=pd.DataFrame(list(datanifty),columns=['Close','Open','High','Low'])
    print(dataframe)
    data=dataframe.astype(float)
    #data = pdr.get_data_yahoo('RELIANCE.NS',st,ed)
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
                                                            
    graph=data.plot(y= ['slowk','slowd'], title=companyname+' Stochastic Oscillator')  
    graph = plt.gcf()
    fig_html = mpld3.fig_to_html(graph)
    return fig_html