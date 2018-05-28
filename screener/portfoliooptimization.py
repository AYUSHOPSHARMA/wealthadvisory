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

 
def portfolioOptimization(stocks, st,ed,num_portfolios):
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
    stocks = ['AAPL','AMZN','MSFT','ACC']
    yf.pdr_override() # <== that's all it takes :-)
    
    #indices= nift200Indices.objects(Ticker__in=["ACC.NS","AMZN.NS"], Date__lte=ed, Date__gte=st)

    #=nift200Indices.objects(Ticker ='AAPL.NS')
    yf.pdr_override() # <== that's all it takes :-)

    end = datetime.date(2018,5,27)
    begin = datetime.date(2017,1,1)

	#timestamp format and get apple stock.

    st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')

    data = web.get_data_yahoo(stocks,st,ed)['Adj Close']
    print("####################Data################")
    print(data)
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
    num_portfolios = 6
     
    #set up array to hold results
    #We have increased the size of the array to hold the weight values for each stock
    results = np.zeros((4+len(stocks)-1,num_portfolios))
    labels = []
    for i in range(num_portfolios):
        #select random weights for portfolio holdings
        weights = np.array(np.random.random(4))
       
        #rebalance weights to sum to 1
        weights /= np.sum(weights)
        
        print("#######WEIGHT##########")
        print(weights)
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
    print("#########################RESULT##############")    
    print(results)
    
    fig, ax = plt.subplots() 
    
    print("############ results.######  T###########")
    print(results.T)
    print("############ ARRAY###########")
        #convert results array to Pandas DataFrame
    results_frame = pd.DataFrame(results.T,columns=['ret','stdev','sharpe',stocks[0],stocks[1],stocks[2],stocks[3]])
    print("################## FRAME###############")
    for i in range(num_portfolios):
        label = results_frame.ix[[i], :].T
        label.columns = ['Row {0}'.format(i)]
    # .to_html() is unicode; so make leading 'u' go away with str()
        labels.append(str(label.to_html()))
    print(results_frame)
        #locate position of portfolio with highest Sharpe Ratio
    #print(results_frame['sharpe'])
    max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
        #locate positon of portfolio with minimum standard deviation
    min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]
       
        #create scatter plot coloured by Sharpe Ratio
    plt.xlabel('Volatility')
    plt.ylabel('Returns')
    points = plt.scatter(results_frame.stdev,results_frame.ret,c=results_frame.sharpe,cmap='RdYlBu')
    #label = results_frame
    #label.columns = results_frame
        # .to_html() is unicode; so make leading 'u' go away with str()
    #labels.append(str(label.to_html()))
    plt.colorbar()
        #plot red star to highlight position of portfolio with highest Sharpe Ratio
    plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=1000)
        #plot green star to highlight position of minimum variance portfolio
    plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=1000)
    print("#########################stdev###########")
        #print(results_frame.stdev)
    print("#########################ret###########")
       # print(results_frame.ret)
    print("#########################sharpe###########")
        #print(results_frame.sharpe)
        
    ax.grid(color='lightgray', alpha=0.7)
        #fig1 = plt.gcf()
    print("#############FIG###########")
        #print(fig1)
    byte_file = io.BytesIO()
    tooltip = plugins.PointHTMLTooltip(points[0], labels,voffset=10, hoffset=10, css=css)
    plugins.connect(fig, tooltip)
   # tooltip = plugins.PointHTMLTooltip(points[0], labels,
   #                               voffset=10, hoffset=10, css=css)
    #plugins.connect(fig, tooltip)
    #print(fig_to_html(fig))
       # display_d3(fig1)
       # fig1.savefig(byte_file, format='png')
        #image_file= byte_file.getvalue()
    save_json(fig,"test.json")
    return fig_to_html(fig)