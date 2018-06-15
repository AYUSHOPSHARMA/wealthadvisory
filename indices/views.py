from django.shortcuts import render
from indices.models import ind_nifty100list
from indices.models import nift100data
from django.template import RequestContext
import datetime
import pandas as pd


#from pandas.plotting import scatter_matrix

import scipy.stats as stats

from pandas_datareader import data as pdr

import fix_yahoo_finance as yf

import numpy as np

import datetime

import talib

import matplotlib.pyplot as plt

import matplotlib.gridspec as grid

import mpld3

import io

from PIL import Image


# Create your views here.

from django.http import HttpResponse

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   indices = ind_nifty100list(Symbol='ABCAPITAL')
   print(indices)
   data = ind_nifty100list.objects
   return render(request,"indices.html",{"data":data})


def nift50(request):
    end = datetime.date(2018,5,5)
    begin = datetime.date(2013,1,1)
    st=begin.strftime('%Y-%m-%d')
    ed=end.strftime('%Y-%m-%d')
    yf.pdr_override() # <== that's all it takes :-)
    data = pdr.get_data_yahoo('YESBANK.NS',st,ed)
    print(data)
    print(len(data))
    return render(request,"indices.html",{"data":data})

def nift100Indices(request,companyname,styear,stmonth,stday,endyear,endmonth,endday):
	#from pandas.plotting import scatter_matrix
	#end = datetime.date(2018,5,5)
	#begin = datetime.date(2017,1,1)
    end = datetime.date(endyear,endmonth,endday)
    begin = datetime.date(styear,stmonth,stday)
	#timestamp format and get apple stock.

    st=begin.strftime('%Y-%m-%d')

    ed=end.strftime('%Y-%m-%d')

    yf.pdr_override() # <== that's all it takes :-)
    data = pdr.get_data_yahoo(companyname,st,ed)
    print(data)
    if len(data) > 0:
         return render(request,"nift100indices.html",{"data":data,"companyname":companyname,"styear":styear,"stmonth":stmonth,"stday":stday,"endyear":endyear,"endmonth":endmonth,"endday":endday})
    else:
       data =nift100data.objects.all()
       print("Start Empty data")
       print(data)
       print("Empty data")
       return render(request,"nift100indices.html",{"data":data,"companyname":companyname,"styear":styear,"stmonth":stmonth,"stday":stday,"endyear":endyear,"endmonth":endmonth,"endday":endday})


def view_indices_chart(request,companyname,styear,stmonth,stday,endyear,endmonth,endday):
     #from pandas.plotting import scatter_matrix
	#end = datetime.date(2018,5,5)
	#begin = datetime.date(2017,1,1)
    end = datetime.date(endyear,endmonth,endday)
    begin = datetime.date(styear,stmonth,stday)
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
        fig=plt.figure(figsize=(500,500))
        data.plot(y= ['Close','Open','High','Low'], title='NSEI BBBANDS',figsize=(10,10),grid=True)
        
        fig1 = plt.gcf()

        byte_file = io.BytesIO()
        
        
        fig1.savefig(byte_file, format='png')
        image_file= byte_file.getvalue()
        # fig, ax = plt.subplots(figsize=(500,500))
        #ax.grid(True)
        # fig.ylabel('Weight')
        # fig.title('Minutes')
        #ax.set_title('ax1 title')
        return HttpResponse(image_file, content_type="image/png")
    
    else:
        data['Open'],data['High'],data['Low'] = talib.BBANDS(np.asarray(data['Close']), timeperiod=30,nbdevup=1,nbdevdn=1,matype=0)
        data['Buy'] = data.apply(lambda x : 1 if x['Close'] < x['Low']  else 0, axis=1)
        data['Sell'] = data.apply(lambda y : 1 if y['Close'] > y['Open']  else 0, axis=1)
        plt.figure(figsize=(500,500))
        graph =data.plot(y= ['Close','Open','High','Low'], title='NSEI BBBANDS',figsize=(10,10),grid=True)
        fig_html = mpld3.fig_to_html(graph)
        return HttpResponse(fig_html)
        return
        

 


