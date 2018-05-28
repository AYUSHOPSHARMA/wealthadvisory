# -*- coding: utf-8 -*-
from django.shortcuts import render
import screener.portfoliooptimization as po
from django.http import HttpResponse
import datetime

def getportfolio(request):
    return render(request,"portfolio.html")

def getPortfolioChart(request):
    stocks = ['AAPL','AMZN','MSFT','ACC']
    end = datetime.date(2018,5,27)
    begin = datetime.date(2017,1,1)
    
    	#timestamp format and get apple stock.
    
    st=begin.strftime('%Y-%m-%d')
    
    ed=end.strftime('%Y-%m-%d')
    
    #set number of runs of random portfolio weights
    num_portfolios = 25000
    
    image_file = po.portfolioOptimization(stocks,st,ed,num_portfolios)
    return HttpResponse(image_file)
