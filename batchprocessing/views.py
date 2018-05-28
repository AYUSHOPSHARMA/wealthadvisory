from batchprocessing.models import nifty_500_companies
from batchprocessing.models import nifty_200_companies
from batchprocessing.models import nifty_100_companies
from batchprocessing.models import nifty_50_companies
from django.http import HttpResponse
import screener.views as fdview
import batchprocessing.fundamentaldata as fdt

# Create your views here.
def top50FundamentalData(request,companyType):
    limitQuery(request,0,50,companyType)
    

def top100FundamentalData(request,companyType):
    limitQuery(request,0,75,companyType)
    limitQuery(request,76,100,companyType)

def top200FundamentalData(request,companyType):
    limitQuery(request,0,75,companyType)
    limitQuery(request,76,150,companyType)
    limitQuery(request,151,200,companyType)

def top500FundamentalData(request,companyType):
    limitQuery(request,0,75,companyType)
    limitQuery(request,76,150,companyType)
    limitQuery(request,151,225,companyType)
    limitQuery(request,225,300,companyType)
    limitQuery(request,301,375,companyType)
    limitQuery(request,376,450,companyType)
    limitQuery(request,451,500,companyType)
    
def callBatch(request,companyType):
    if(companyType == "nifty50"):
        top50FundamentalData(request,companyType)
    elif(companyType == "nifty100"):
        top100FundamentalData(request,companyType)
    elif(companyType == "nifty200"):
        top200FundamentalData(request,companyType)
    elif(companyType == "nifty500"):
        top500FundamentalData(request,companyType)
        
    
def uploadCompany(request,companyType):
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
    
     print(result)
     i=0
     for companyname in result:
        cname=companyname.Company_Name
        symbol=companyname.Symbol+".NS"
        industry=companyname.Industry
        print(cname)
        if(symbol != "NA"):
            print(symbol)
            fundamentalData=fdview.getBatchFundamentalData(symbol)
            print(fundamentalData)
            j = 0
            fd = fdt.FundamentalData(request,symbol)
            fd.setTicker(symbol)
            fd.setCompanyName(cname)
            fd.setIndustry(industry)
            while j < len(fundamentalData.columns.values):
                 fd.setvalues(fundamentalData.columns.values[j],fundamentalData.values[0][j])
                 j+=1
                 
            fd.saveFundamentalData(companyType)
            
        i+=1
   