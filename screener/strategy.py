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

from PIL import Image

def getSMAStrategy(request,backtestyear):
    # import cufflinks
    smafig = []
    plt.style.use('seaborn')
    ##%matplotlib inline
    
    end = datetime.date.today()
    begin=end-pd.DateOffset(365*backtestyear)
    
    
    #timestamp format and get apple stock.
    st=begin.strftime('%Y-%m-%d')
    ed=end.strftime('%Y-%m-%d')
    yf.pdr_override()
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
    
    data.tail()
    
    
    data[['Returns', 'Strategy']].dropna().cumsum(
                    ).apply(np.exp).plot(figsize=(10, 6));
    
    smafig.append(fig_to_html(plt.gcf()))
    return fig_to_html(plt.gcf())


def getStrategy(request):
     smafig = getSMAStrategy(request,9)
     bbbandGraph=view_indices_chart(request,"SBIN.NS",9)
     return render(request,"stratergyOption.html",{"smadata":smafig,"bbbandGraph":bbbandGraph})

def view_indices_chart(request,companyname,backtestyear):
     #from pandas.plotting import scatter_matrix
	#end = datetime.date(2018,5,5)
	#begin = datetime.date(2017,1,1)
    end = datetime.date.today()
    begin=end-pd.DateOffset(365*backtestyear)
	#timestamp format and get apple stock.

    st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')

    yf.pdr_override() # <== that's all it takes :-)
    
    fig, ax = plt.subplots()
    
    data = pdr.get_data_yahoo(companyname,st,ed)
    print(data)
    if len(data) > 0:
        data = data.dropna()
        data['Open'],data['High'],data['Low'] = talib.BBANDS(np.asarray(data['Close']), timeperiod=30,nbdevup=1,nbdevdn=1,matype=0)
        data['Buy'] = data.apply(lambda x : 1 if x['Close'] < x['Low']  else 0, axis=1)
        data['Sell'] = data.apply(lambda y : 1 if y['Close'] > y['Open']  else 0, axis=1)
        data.plot(y= ['Close','Open','High','Low'], title='NSEI BBBANDS',figsize=(10,10),grid=True)
        
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
        graph =data.plot(y= ['Close','Open','High','Low'], title='NSEI BBBANDS',figsize=(10,10),grid=True)
        fig_html = mpld3.fig_to_html(graph)
    return fig_html
