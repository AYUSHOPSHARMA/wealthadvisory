from batchprocessing.models import nift50Indices
from batchprocessing.models import nift100Indices
from batchprocessing.models import nift200Indices
from batchprocessing.models import nift500Indices
from batchprocessing.models import nifty_500_companies
from batchprocessing.models import nifty_200_companies
from batchprocessing.models import nifty_100_companies
from batchprocessing.models import nifty_50_companies
from batchprocessing.models import niftBanchMarkIndices
from django.http import HttpResponse
import screener.views as fdview
import batchprocessing.fundamentaldata as fdt
import scipy.stats as stats
import time

from pandas_datareader import data as pdr

import fix_yahoo_finance as yf

import numpy as np

import datetime

# Create your views here.
def top50IndicesData(request,companyType):
    limitQuery(request,1,3,companyType)
    limitQuery(request,4,6,companyType)
    limitQuery(request,7,9,companyType)
    limitQuery(request,10,12,companyType)
    limitQuery(request,13,15,companyType)
    limitQuery(request,16,18,companyType)
    limitQuery(request,19,21,companyType)
    limitQuery(request,22,24,companyType)
    limitQuery(request,25,27,companyType)
    limitQuery(request,28,30,companyType)
    limitQuery(request,31,33,companyType)
    limitQuery(request,34,36,companyType)
    limitQuery(request,37,39,companyType)
    limitQuery(request,40,42,companyType)
    limitQuery(request,43,45,companyType)
    limitQuery(request,46,48,companyType)
    limitQuery(request,49,50,companyType)
    
    

def top100IndicesData(request,companyType):
    limitQuery(request,0,75,companyType)
    limitQuery(request,76,100,companyType)

def top200IndicesData(request,companyType):
    limitQuery(request,0,75,companyType)
    limitQuery(request,76,150,companyType)
    limitQuery(request,151,200,companyType)

def top500IndicesData(request,companyType):
    #limitQuery(request,0,75,companyType)
    limitQuery(request,76,150,companyType)
    limitQuery(request,151,225,companyType)
    limitQuery(request,225,300,companyType)
    limitQuery(request,301,375,companyType)
    limitQuery(request,376,450,companyType)
    limitQuery(request,451,500,companyType)
 
def banchMarkIndicesData(request,companyType):
    limitQuery(request,0,50,companyType)
    
def callBatch(request,companyType):
    if(companyType == "nifty50"):
        top50IndicesData(request,companyType)
    elif(companyType == "nifty100"):
        top100IndicesData(request,companyType)
    elif(companyType == "nifty200"):
        top200IndicesData(request,companyType)
    elif(companyType == "nifty500"):
        top500IndicesData(request,companyType)
    elif(companyType == "banchMark"):
         banchMarkIndicesData(request,companyType)
    
def uploadIndices(request,companyType):
    callBatch(request,companyType)
    return HttpResponse("Read All Data")

def limitQuery(request,start,limit,companyType):
     if(companyType == "nifty50"):
         result=nifty_50_companies.objects[start:limit]
     elif(companyType == "nifty100"):
         result=nifty_100_companies.objects[start:limit]
     elif(companyType == "nifty200"):
         result=nifty_200_companies.objects[start:limit]
     elif(companyType == "nifty500"):
         result=nifty_500_companies.objects[start:limit]
     elif(companyType == "banchMark"):
         result =[]
         result.append("%5Ensei")
     now= datetime.datetime.now().strftime("%Y-%m-%d")    
     begin = datetime.date(2013,1,1)
     #timestamp format and get apple stock.
     st=begin.strftime('%Y-%m-%d')
     ed=now
     print("############# companyType ############")
     print(result)
     i=0
     for companyname in result:
        if(companyType == "banchMark"):
            cname="NIFTY 50"
            symbol=companyname
            industry = ""
        else:
            cname=companyname.Company_Name
            symbol=companyname.Symbol+".NS"
            industry = companyname.Industry
        print(cname)
        if(symbol != "NA"):
            yf.pdr_override() # <== that's all it takes :-)
            print("############## DOWNLOADING DATA ###########")
            print(symbol)
            print(st)
            print(ed)
            data = pdr.get_data_yahoo(symbol,st,ed)
            print("#########downloaded data from yahoo for ############")
            print(symbol)
            print(len(data))
            if len(data) <= 0 :
                time.sleep(10)
                data = pdr.get_data_yahoo(symbol,st,ed)
                
            j = 0
            
            while j < len(data):
                print("###### START Index ######")
                if(companyType=="nifty500"):
                     companies_indices_data_obj=nift500Indices()
                     indices = nift500Indices.objects(Ticker=symbol,Date=data.index.date[j])
                elif(companyType=="nifty200"):
                     companies_indices_data_obj=nift200Indices()
                     indices = nift200Indices.objects(Ticker=symbol,Date=data.index.date[j])
                elif(companyType=="nifty100"):
                    companies_indices_data_obj=nift100Indices()
                    indices = nift100Indices.objects(Ticker=symbol,Date=data.index.date[j])
                elif(companyType=="nifty50"):
                    companies_indices_data_obj=nift50Indices()
                    indices = nift50Indices.objects(Ticker=symbol,Date=data.index.date[j])
                elif(companyType=="banchMark"):
                    companies_indices_data_obj=niftBanchMarkIndices()
                    indices = {}  
                print("############################################# Length Indices##################")
                print(len(indices))      
                if len(indices) <= 0:
                    companies_indices_data_obj.Date = data.index.date[j]
                    companies_indices_data_obj.Ticker=symbol
                    companies_indices_data_obj.Industry=industry
                    companies_indices_data_obj.Company_Name=cname
                    companies_indices_data_obj.Open = data['Open'][j]
                    companies_indices_data_obj.High = data['High'][j]
                    companies_indices_data_obj.Low =  data['Low'][j]
                    companies_indices_data_obj.Close =data['Close'][j]
                    companies_indices_data_obj.Adj_Close =data['Adj Close'][j]
                    companies_indices_data_obj.Volume = data['Volume'][j]
                    companies_indices_data_obj.save()
                    print("###### END ######")
                j+=1
                
            print("#########SAVED data from yahoo for ############")
   