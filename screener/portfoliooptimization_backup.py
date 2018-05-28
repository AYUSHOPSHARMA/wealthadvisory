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

 
def portfolioOptimization(stocks, st,ed,num_portfolios):
    #list of stocks in portfolio
    
    
    yf.pdr_override() # <== that's all it takes :-)
    
    #indices= nift200Indices.objects(Ticker__in=["ABB.NS","AMZN.NS","MSFT.NS","ACC.NS"], Date__lte=ed, Date__gte=st)
    
    indices= nift200Indices.objects.filter(Ticker__in=["ABB.NS","AMZN.NS","MSFT.NS","ACC.NS"], Date__lte=ed, Date__gte=st).values_list("Date","Ticker","Adj_Close")
    
    #=nift200Indices.objects(Ticker ='AAPL.NS')
    print("####################RESULT##################")
    print(indices)
    data1 = web.get_data_yahoo(stocks,st,ed)['Adj Close']
    print("####################Data################")
    data = pd.DataFrame.from_records(indices)
    print(data)
    print("####################Data-11111################")
    print(data1)
    #download daily price data for each of the stocks in the portfolio
    #data = web.DataReader(stocks,data_source='yahoo',start='01/01/2010')['Adj Close']
     
    data.sort_index(inplace=True)
     
    #convert daily stock prices into daily returns
    returns = data.pct_change()
     
    #calculate mean daily return and covariance of daily returns
    mean_daily_returns = returns.mean()
    cov_matrix = returns.cov()
    
    print("##########cov_matrix########")
    print(cov_matrix)
     
    #set up array to hold results
    #We have increased the size of the array to hold the weight values for each stock
    results = np.zeros((4+len(stocks)-1,num_portfolios))
     
    for i in range(num_portfolios):
        #select random weights for portfolio holdings
        weights = np.array(np.random.random(4))
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
    
        print(results)
    
        #convert results array to Pandas DataFrame
        results_frame = pd.DataFrame(results.T,columns=['ret','stdev','sharpe',stocks[0],stocks[1],stocks[2],stocks[3]])
         
        #locate position of portfolio with highest Sharpe Ratio
        print(results_frame['sharpe'])
        max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
        #locate positon of portfolio with minimum standard deviation
        min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]
         
        #create scatter plot coloured by Sharpe Ratio
        plt.scatter(results_frame.stdev,results_frame.ret,c=results_frame.sharpe,cmap='RdYlBu')
        plt.xlabel('Volatility')
        plt.ylabel('Returns')
        plt.colorbar()
        #plot red star to highlight position of portfolio with highest Sharpe Ratio
        plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=1000)
        #plot green star to highlight position of minimum variance portfolio
        plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=1000)
        
        fig1 = plt.gcf()

        byte_file = io.BytesIO()
        
        
        fig1.savefig(byte_file, format='png')
        image_file= byte_file.getvalue()
        return image_file