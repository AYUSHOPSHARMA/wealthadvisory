# -*- coding: utf-8 -*-
"""
Created on Sun May 27 12:57:50 2018

@author: ayush.sharma
"""

import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
from batchprocessing.models import nift200Indices
import datetime
import io
from mongoengine import *
from mongoengine.queryset.visitor import Q
from mpld3._display import display_d3,fig_to_html,save_json
from mpld3 import plugins
import json
from django.views.decorators.cache import cache_page
from batchprocessing.models import nift50Indices,nift100Indices,nift200Indices,nift500Indices,nifty_50_fundamental_data,nifty_100_fundamental_data,nifty_200_fundamental_data,nifty_500_fundamental_data
import datetime as dt
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

def portfolioOptimization(portfolio, st,ed,num_portfolios):
    #list of stocks in portfolio
    css = """
        table
        {
          border-collapse: collapse;
        }
        th
        {
          color: #ffffff;
          background-color: #000000;
        }
        td
        {
          background-color: #cccccc;
        }
        table, th, td
        {
          font-family:Arial, Helvetica, sans-serif;
          border: 1px solid black;
          text-align: right;
        }
        """
    stocks = portfolio.Ticker_List
    #yf.pdr_override() # <== that's all it takes :-)
    
    #indices= nift200Indices.objects(Ticker__in=["ACC.NS","AMZN.NS"], Date__lte=ed, Date__gte=st)

    #=nift200Indices.objects(Ticker ='AAPL.NS')
    #yf.pdr_override() # <== that's all it takes :-)

    begin = datetime.date(2017,1,1)

	#timestamp format and get apple stock.

    start_date=begin.strftime('%Y-%m-%d')

    #end_date=end.strftime('%Y-%m-%d')
    end_date = dt.date.today()
    #data = web.get_data_yahoo(stocks,st,ed)['Adj Close']
    i=0
    for sysm in stocks:
        if portfolio.Company_Type =="nifty50":
            objnf50=nift50Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Adj_Close','Date')
        elif portfolio.Company_Type =="nifty100":
            objnf50=nift100Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Adj_Close','Date')
        elif portfolio.Company_Type =="nifty200":
            objnf50=nift200Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Adj_Close','Date')
        else:
            objnf50=nift500Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Adj_Close','Date')
        
        if i==0:
            data=pd.DataFrame(list(objnf50),columns=[sysm,'Date'])
            data=data.set_index('Date')
        else:    
            data_frame =pd.DataFrame(list(objnf50),columns=[sysm,'Date'])
            data_frame=data_frame.set_index('Date')
            data = pd.merge(
                data, data_frame, right_index=True, left_index=True, how='outer')
        i+=1
    #temp_data = data.iloc[:,0:len(data.columns)].apply(pd.to_numeric)
     
        
    #download daily price data for each of the stocks in the portfolio
    #data = web.DataReader(stocks,data_source='yahoo',start='01/01/2010')['Adj Close']
    #print("########## data ##########")
    #print(portfolio.Portfolio_Name)
    #print(data)
    data.sort_index(inplace=True)
     
    #convert daily stock prices into daily returns
    returns = data.pct_change()
    #print("#########returns#########")
    returns = returns.dropna(how='any')
    #print(returns)
    #calculate mean daily return and covariance of daily returns
    mean_daily_returns = returns.mean()
    cov_matrix = returns.astype(float).cov()
    
    #print("#########DATA##########")
    #print(data)
    #print("##########cov_matrix##########")
    #print(cov_matrix)
    num_portfolios = 500
     
    #set up array to hold results
    #We have increased the size of the array to hold the weight values for each stock
    results = np.zeros((4+len(stocks)-1,num_portfolios))
    labels = []
    for i in range(num_portfolios):
        #select random weights for portfolio holdings
        weights = np.array(np.random.random(len(stocks)))
       
        #rebalance weights to sum to 1
        weights /= np.sum(weights)
        
        #calculate portfolio return and volatility
        portfolio_return = np.sum(mean_daily_returns * weights) * 252
        portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(252)
        
       # print("########### portfolio_return#############")
        #print(portfolio_return)
        #print("########### portfolio_std_dev#############")
        #print(portfolio_std_dev)
        #store results in results array
        results[0,i] = portfolio_return
        results[1,i] = portfolio_std_dev
        #store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
        results[2,i] = results[0,i] / results[1,i]
        #iterate through the weight vector and add data to results array
        for j in range(len(weights)):
            results[j+3,i] = weights[j]
    
    fig, ax = plt.subplots()
    columnst=[]
    columnst.append("returns")
    columnst.append("standard_deviation")
    columnst.append("sharpe_ratio")
    for st in stocks:
        columnst.append(st)
        #convert results array to Pandas DataFrame
    #print("###########columst#########")
    #print(columnst)      
    results_frame = pd.DataFrame(results.T,columns=columnst)
    for i in range(num_portfolios):
        label = results_frame.ix[[i], :].T
        label.columns = ['Statistics']
    # .to_html() is unicode; so make leading 'u' go away with str()
        labels.append(str(label.to_html()))
        #locate position of portfolio with highest Sharpe Ratio
    #print(results_frame['sharpe_ratio'])
    max_sharpe_port = results_frame.iloc[results_frame['sharpe_ratio'].idxmax()]
        #locate positon of portfolio with minimum standard deviation
    min_vol_port = results_frame.iloc[results_frame['standard_deviation'].idxmin()]
       
        #create scatter plot coloured by Sharpe Ratio
    plt.xlabel('Volatility')
    plt.ylabel('returns')
    points = plt.scatter(results_frame.standard_deviation,results_frame.returns,c=results_frame.sharpe_ratio,cmap='RdYlBu')
    #label = results_frame
    #label.columns = results_frame
        # .to_html() is unicode; so make leading 'u' go away with str()
    #labels.append(str(label.to_html()))
    plt.colorbar()
        #plot red star to highlight position of portfolio with highest sharpe_ratio Ratio
    pointsst1=plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=1000)
        #plot green star to highlight position of minimum variance portfolio
    pointsst2=plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=1000)
        #print(results_frame.standard_deviation)
       # print(results_frame.return)
        #print(results_frame.sharpe)
        
    ax.grid(color='lightgray', alpha=0.7)
        #fig1 = plt.gcf()
        #print(fig1)
    byte_file = io.BytesIO()
    point1= []
    pointsst1label = max_sharpe_port.ix[0:]
    pointsst1label=pointsst1label.to_frame()
    pointsst1label.columns = ['Statistics']
    print("######## pointsst1label######")
    print(pointsst1label) 
    point1.append(str(pointsst1label.to_html()))
    point2=[]
    pointsst2label = min_vol_port.ix[0:]
    pointsst2label=pointsst2label.to_frame()
    pointsst2label.columns = ['Statistics']
         
    point2.append(str(pointsst2label.to_html()))
    tooltip = plugins.PointHTMLTooltip(points, labels,voffset=10, hoffset=10, css=css)
    tooltipstr1 = plugins.PointHTMLTooltip(pointsst1, point1,voffset=10, hoffset=10, css=css)
    tooltipstr2 = plugins.PointHTMLTooltip(pointsst2, point2,voffset=10, hoffset=10, css=css)
    plugins.connect(fig, tooltip)
    plugins.connect(fig, tooltipstr1)
    plugins.connect(fig, tooltipstr2)
    fig.set_size_inches(11.7, 8.27)
   # tooltip = plugins.PointHTMLTooltip(points[0], labels,
   #                               voffset=10, hoffset=10, css=css)
    #plugins.connect(fig, tooltip)
    #print(fig_to_html(fig))
       # display_d3(fig1)
       # fig1.savefig(byte_file, format='png')
        #image_file= byte_file.getvalue()
    save_json(fig,"heatmap.json")
    return fig