from django.shortcuts import render
from batchprocessing.models import portfolio,portfolioDetail
import screener.portfoliooptimization as po
from mpld3._display import display_d3,fig_to_html,save_json
import portfoliooptimization.dataportfolio as dataportfolio
import datetime as datetime
from batchprocessing.models import nifty_50_fundamental_data,nifty_100_fundamental_data,nifty_200_fundamental_data,nifty_500_fundamental_data,niftBanchMarkIndices
from portfoliooptimization import generatereport
import datetime as dt

def getPortfolioDetails(request):
    return render(request,"portfolio.html")


def getPortfolioList(request):
     portfolioList=portfolio.objects.all() #.filter(Portfolio_Name='Nifty50_Zero_Debt_Equity')
     allportfolio= []
     for portfolioobj in portfolioList:
         portfolioDetailobj=portfolioDetail()
         begin = datetime.date(2017,1,1)
         portfolioDetailobj.Portfolio_Name=  portfolioobj.Portfolio_Name
         portfolioDetailobj.Company_Type=  portfolioobj.Company_Type
         portfolioDetailobj.Ticker_List =  portfolioobj.Ticker_List
         if portfolioobj.Trailing_P_E != "Any":
                     if isLE(portfolioobj.Trailing_P_E):
                         value = comparewithValue(portfolioobj.Trailing_P_E)
                         print("Returning Trailing PE LT")
                         portfolioobj.Trailing_P_E = "Under" + value
                     elif isGT(portfolioobj.Trailing_P_E):
                         value = comparewithValue(portfolioobj.Trailing_P_E)
                         print("Returning Trailing PE GT")
                         portfolioobj.Trailing_P_E = "Over" + value
         #num_portfolios = 25000
         portfolioDetailobj = dataportfolio.optimizePortfolio(portfolioDetailobj,begin)
         if portfolioobj.Company_Type =="nifty50":
             fundamentaldata = nifty_50_fundamental_data.objects.filter(Ticker__in=portfolioobj.Ticker_List)
         elif portfolioobj.Company_Type =="nifty100":
             fundamentaldata = nifty_100_fundamental_data.objects.filter(Ticker__in=portfolioobj.Ticker_List)
         elif portfolioobj.Company_Type =="nifty200":
             fundamentaldata = nifty_200_fundamental_data.objects.filter(Ticker__in=portfolioobj.Ticker_List)
         elif portfolioobj.Company_Type =="banchMark":
             fundamentaldata = niftBanchMarkIndices.objects.filter(Ticker ="%5Ensei")
         else:
             fundamentaldata = nifty_500_fundamental_data.objects.filter(Ticker__in=portfolioobj.Ticker_List)
         #print("###########SYMBOL##############")
         #print(fundamentaldata)
         portfolioDetailobj.fundamentalDataList.append(fundamentaldata)    
         allportfolio.append(portfolioDetailobj)
         portfolioDetailobj.portfolioobj = portfolioobj
         print("############## Debt_Equity ########")
         print(portfolioDetailobj.portfolioobj.Debt_Equity)
         #generatereport.report.generateReport(portfolioobj)
         date = str(dt.date.today())
         #print("################# FUNDAMENTAL############")
         #print(portfolioDetailobj.fundamentalDataList)
         #result_HTML=fig_to_html(po.portfolioOptimization(portfolio,st,ed,num_portfolios))
         #result_corr_HTML = fig_to_html(dataportfolio.correlData(portfolio,begin))
         #result_riskreturn_HTML = fig_to_html(dataportfolio.risk_return(portfolio,begin))
         #result_violin_HTML = fig_to_html(dataportfolio.violin(portfolio,begin))
     return render(request,"portfolioList.html", {"portfolioList":allportfolio,"date":date})
    
def comparewithValue(field):
    print("Field valueee#########")
    print(field.value())
    if  "_" in field.value():
        print("INSIDE IF FIND###############")
        splitedvalue=field.value().split("_")
        if is_number_tryexcept(splitedvalue[1]) == True:
            return float(splitedvalue[1])
        else:
             return float(1000)
    return float(1000)

def isLE(field):
    print("###########CHECKING LT##########")
    if  "lt_" in field.value():
        return True
    else:
        return False

def isGT(field):
    print("###########CHECKING GT##########")
    if "gt_" in field.value():
        return True;
    else:
        return False
    

