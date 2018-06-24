from batchprocessing.models import nifty_500_companies
from batchprocessing.models import nifty_200_companies
from batchprocessing.models import nifty_100_companies
from batchprocessing.models import nifty_50_companies
from batchprocessing.models import portfolio
from django.http import HttpResponse
import screener.views as fdview
import batchprocessing.fundamentaldata as fdt
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, URLError

from mongoengine import *

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
    elif(companyType == "mutualfund"):
        loadMutualFundData(request,companyType)
        
    
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
            if fundamentalData is None:
                pass
            print(fundamentalData)
            j = 0
            fd = fdt.FundamentalData(request,symbol)
            fd.setTicker(symbol)
            fd.setCompanyName(cname)
            fd.setIndustry(industry)
            if fundamentalData is not None:
                while j < len(fundamentalData.columns.values):
                     fd.setvalues(fundamentalData.columns.values[j],fundamentalData.values[0][j])
                     j+=1
                 
            fd.saveFundamentalData(companyType)
            
        i+=1

def createPortfolio(request):
    portfolioobj = portfolio()
    portfolioobj.Portfolio_Name = 'Nifty50_Zero_Debt_Equity'
    portfolioobj.Company_Type = 'nifty50'
    portfolioobj.Ticker_List = ['BAJAJ-AUTO.NS', 'BAJAJFINSV.NS', 'INFRATEL.NS', 'HEROMOTOCO.NS', 'HINDUNILVR.NS', 'ITC.NS', 'IOC.NS', 'INFY.NS', 'MARUTI.NS']
    portfolioobj.save()
    return HttpResponse("Portfolio Created")

def savePortfolio(tickerList,Portfolio_Name,companyType,fundamental_form):
     print("#########inside Save Portfolio Method########")
     print(tickerList)      
     portfolioobj = portfolio()
     portfolioobj.Portfolio_Name = Portfolio_Name
     portfolioobj.Company_Type = companyType
     portfolioobj.Ticker_List = tickerList
     portfolioobj.Trailing_P_E=fundamental_form['Trailing_P_E'].value()
     portfolioobj.Forward_P_E=fundamental_form['Forward_P_E'].value()
     portfolioobj.Beta=fundamental_form['Beta'].value()
     portfolioobj.PEG=fundamental_form['PEG'].value()
     portfolioobj.PS=fundamental_form['PS'].value()
     portfolioobj.PB=fundamental_form['PB'].value()
     portfolioobj.Price_Cash=fundamental_form['Price_Cash'].value()
     portfolioobj.Price_Free_Cash_Flow=fundamental_form['Price_Free_Cash_Flow'].value()
     portfolioobj.EPS_growth_this_year=fundamental_form['EPS_growth_this_year'].value()
     portfolioobj.Return_on_Assets=fundamental_form['Return_on_Assets'].value()
     portfolioobj.Return_on_Equity=fundamental_form['Return_on_Equity'].value()
     portfolioobj.Current_Ratio=fundamental_form['Current_Ratio'].value()
     portfolioobj.Quick_Ratio=fundamental_form['Quick_Ratio'].value()
     portfolioobj.Lt_Debt_Equity=fundamental_form['Lt_Debt_Equity'].value()
     portfolioobj.Debt_Equity=fundamental_form['Debt_Equity'].value()
     portfolioobj.Gross_Margin=fundamental_form['Gross_Margin'].value()
     portfolioobj.Net_Profit_Margin=fundamental_form['Net_Profit_Margin'].value()
     portfolioobj.Payout_Ratio=fundamental_form['Payout_Ratio'].value()
     portfolioobj.Insider_Ownership=fundamental_form['Insider_Ownership'].value()
     portfolioobj.Institutional_Ownership=fundamental_form['Institutional_Ownership'].value()
     portfolioobj.save()
     

def uploadMutualFund(request):
    callBatch(request,"mutualfund")
    return HttpResponse("Read All Data")

def loadMutualFundData(request,companyType):
    limitMutualFundQuery(request,0,75,companyType)

def limitMutualFundQuery(request,offset,count,companyType):
    try:
        #tickers = ['F00000GUQS.BO',' F00000GUQR.BO',' F000001A8O.BO',' F0GBR06RVN.BO',' F00000Q9VS.BO',' F00000PSMK.BO','F00000PSRX.BO','F000001A8F.BO','F00000Q03F.BO','F00000Q47F.BO',' F000001A9K.BO',' F000002R3N.BO',' F00000NX9B.BO',' F00000UET8.BO',' F00000UETC.BO',' F00000NUJJ.BO',' F0GBR06SC1.BO',' F00000PPPW.BO',' F00000PSRW.BO',' F00000PSRP.BO',' F00000PSRQ.BO',' F0GBR06R6U.BO',' F000001A8G.BO',' F000003WEI.BO',' F00000Q15M.BO',' F00000UET9.BO',' F0GBR06SCV.BO',' F00000U4WQ.BO' ]
        #for tk in tickers:
         #result = pd.DataFrame(index = tk, columns = statics)
         url = 'https://in.finance.yahoo.com/mutualfunds/?offset=0&count=100&guccounter=1'
         print(url)
         resp = urlopen(url)
         soup = BeautifulSoup(resp.read(), 'html.parser')
         allTd = soup.find_all('td',attrs={'class':'Va(m) Fz(s) Ta(start) Pstart(6px) Pend(10px)'})
         print("All Ids")
         print(allTd) 
         #
         #for static in statics:
         #    result.ix[ticker, static] = getValue(allTd, static)
    except:
        print("Error in url Opening")
        return None
    return HttpResponse("Read All Data")
