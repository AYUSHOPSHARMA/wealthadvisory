from django.shortcuts import render
import screener.fundamentalData as fd
import screener.screenerBean as sb
from batchprocessing.models import nifty_500_companies_fundamental_data
from batchprocessing.models import nifty_200_companies_fundamental_data
from batchprocessing.models import nifty_100_companies_fundamental_data
from batchprocessing.models import nifty_50_companies_fundamental_data
import json
# Create your views here.
keyStatistics = [
    "Market Cap ",
    "Enterprise Value",
    "Trailing P/E",
    "Forward P/E",
    "PEG Ratio",
    "Price/Sales",
    "Price/Book",
    "Enterprise Value/Revenue",
    "Enterprise Value/EBITDA",
    "Fiscal Year Ends",
    "Most Recent Quarter",
    "Profit Margin",
    "Operating Margin",
    "Return on Assets",
    "Return on Equity",
    "Revenue",
    "Revenue Per Share",
    "Quarterly Revenue Growth",
    "Gross Profit",
    "EBITDA",
    "Net Income Avi to Common",
    "Diluted EPS",
    "Quarterly Earnings Growth",
    "Total Cash",
    "Total Cash Per Share",
    "Total Debt",
    "Total Debt/Equity",
    "Current Ratio",
    "Book Value Per Share",
    "Operating Cash Flow",
    "Levered Free Cash Flow",
    "Beta",
    "52-Week Change",
    "S&P500 52-Week Change",
    "52 Week High",
    "52 Week Low",
    "50-Day Moving Average",
    "200-Day Moving Average",
    "Avg Vol (3 month)",
    "Avg Vol (10 day)",
    "Shares Outstanding",
    "Float",
    "% Held by Insiders",
    "% Held by Institutions",
    "Shares Short",
    "Short Ratio",
    "Short % of Float",
    "Shares Short (prior month)",
    "Forward Annual Dividend Rate",
    "Forward Annual Dividend Yield",
    "Trailing Annual Dividend Yield",
    "Trailing Annual Dividend Yield",
    "5 Year Average Dividend Yield",
    "Payout Ratio",
    "Dividend Date",
    "Ex-Dividend Date",
    "Last Split Factor (new per old)",
    "Last Split Date"
]

valuationMeasureStatistics = [
    "Market Cap ",
    "Enterprise Value",
    "Trailing P/E",
    "Forward P/E",
    "PEG Ratio",
    "Price/Sales",
    "Price/Book",
    "Enterprise Value/Revenue",
    "Enterprise Value/EBITDA"
    ]
financialHighlightsStatics=[
    "Fiscal Year Ends",
    "Most Recent Quarter"
    ]

profitablity=[
    "Profit Margin",
    "Operating Margin"
    ]

managementEffectivenessStatics=[
    "Return on Assets",
    "Return on Equity"
    ]
incomeStatementStatics=[
    "Revenue",
    "Revenue Per Share",
    "Quarterly Revenue Growth",
    "Gross Profit",
    "EBITDA",
    "Net Income Avi to Common",
    "Diluted EPS",
    "Quarterly Earnings Growth"
    ]
balanceSheetStatics=[
    "Total Cash",
    "Total Cash Per Share",
    "Total Debt",
    "Total Debt/Equity",
    "Current Ratio",
    "Book Value Per Share"
    ]
cashFlowStatementsStatics=[
    "Operating Cash Flow",
    "Levered Free Cash Flow"
    ]

stockPricsHistoryStatics=[
    "Beta",
    "52-Week Change",
    "S&P500 52-Week Change",
    "52 Week High",
    "52 Week Low",
    "50-Day Moving Average",
    "200-Day Moving Average"
    ]
shareStatics=[
    "Avg Vol (3 month)",
    "Avg Vol (10 day)",
    "Shares Outstanding",
    "Float",
    "% Held by Insiders",
    "% Held by Institutions",
    "Shares Short",
    "Short Ratio",
    "Short % of Float",
    "Shares Short (prior month)"
    ]
dividentSplitStatics=[
    "Forward Annual Dividend Rate",
    "Forward Annual Dividend Yield",
    "Trailing Annual Dividend Yield",
    "Trailing Annual Dividend Yield",
    "5 Year Average Dividend Yield",
    "Payout Ratio",
    "Dividend Date",
    "Ex-Dividend Date",
    "Last Split Factor (new per old)",
    "Last Split Date"
]

def getfundamentalData(request,ticker):
     result = fd.get_fundamental_data(ticker,valuationMeasureStatistics)
     i = 0
     valuationMeasuredata =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         valuationMeasuredata.append(item)
         print(valuationMeasuredata)
         i+=1
     result = fd.get_fundamental_data(ticker,financialHighlightsStatics)
     i = 0
     financialHighlightsStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         financialHighlightsStaticsData.append(item)
         print(financialHighlightsStaticsData)
         i+=1
     result = fd.get_fundamental_data(ticker,profitablity)
     i = 0
     profitablityData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         profitablityData.append(item)
         print(profitablityData)
         i+=1
     result = fd.get_fundamental_data(ticker,managementEffectivenessStatics)
     i = 0
     managementEffectivenessStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         managementEffectivenessStaticsData.append(item)
         print(managementEffectivenessStaticsData)
         i+=1
     result = fd.get_fundamental_data(ticker,incomeStatementStatics)
     i = 0
     incomeStatementStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         incomeStatementStaticsData.append(item)
         print(incomeStatementStaticsData)
         i+=1
     result = fd.get_fundamental_data(ticker,balanceSheetStatics)
     i = 0
     balanceSheetStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         balanceSheetStaticsData.append(item)
         print(balanceSheetStaticsData)
         i+=1
     result = fd.get_fundamental_data(ticker,cashFlowStatementsStatics)
     i = 0
     cashFlowStatementsStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         cashFlowStatementsStaticsData.append(item)
         print(cashFlowStatementsStaticsData)
         i+=1
         
     result = fd.get_fundamental_data(ticker,stockPricsHistoryStatics)
     i = 0
     stockPricsHistoryStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         stockPricsHistoryStaticsData.append(item)
         print(stockPricsHistoryStaticsData)
         i+=1
     result = fd.get_fundamental_data(ticker,shareStatics)
     i = 0
     shareStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         shareStaticsData.append(item)
         print(shareStaticsData)
         i+=1
     result = fd.get_fundamental_data(ticker,dividentSplitStatics)
     i = 0
     dividentSplitStaticsData =[]
     while i < len(result.columns.values):
         item = {"keyStatistics":result.columns.values[i]}
         item["value"] =result.values[0][i]
         dividentSplitStaticsData.append(item)
         print(dividentSplitStaticsData)
         i+=1
     return render(request,"fundamentaldata.html",{"valuationMeasuredata":valuationMeasuredata,"financialHighlightsStaticsData": financialHighlightsStaticsData,"profitablityData":profitablityData,"managementEffectivenessStaticsData":managementEffectivenessStaticsData,"incomeStatementStaticsData":incomeStatementStaticsData,"balanceSheetStaticsData":balanceSheetStaticsData,"cashFlowStatementsStaticsData":cashFlowStatementsStaticsData,"stockPricsHistoryStaticsData":stockPricsHistoryStaticsData,"shareStaticsData":shareStaticsData,"dividentSplitStaticsData":dividentSplitStaticsData,"ticker":ticker})
 

def getBatchFundamentalData(ticker):
     result = fd.get_fundamental_data(ticker,keyStatistics)
     return result
 
def getStaticVr(request):
    return render(request,"blockbuilder.html")

def fundamentalDataHome(request):
    pe = request.GET.get('TrailingP_E')
    screenerdatabean=sb.ScreenerData(request,"nifty500")
    print(screenerdatabean.Trailing_P_E)
    print("Value111###############################")
    print(pe)
    if pe is not None:
        print("Inside if#########")
        screenerdatabean.setTrailing_P_E(pe)
    print("Value###############################")
    print(pe)
    totalresult=100
    result=nifty_500_companies_fundamental_data.objects[0:100]
    pagecount =totalresult/20
    currentpage=1
    input = '' 
    input +=  '{"companyType":"'+screenerdatabean.companyType+'" ,"Trailing_P_E":"'+str(screenerdatabean.getTrailing_P_E)+'",'
    input +=  '"Forward_P_E":"'+screenerdatabean.Forward_P_E+'",'
    input +=  '"PEG_Ratio" :"'+screenerdatabean.PEG_Ratio+'",'
    input +=  '"Quarterly_Earnings_Growth":"'+screenerdatabean.Quarterly_Earnings_Growth+'",'
    input +=  '"Price_Sales":"'+screenerdatabean.Price_Sales+'",'
    input +=  '"Price_Book":"'+screenerdatabean.Price_Book+'",'
    input +=  '"Total_Cash_Per_Share":"'+screenerdatabean.Total_Cash_Per_Share+'",'
    input +=  '"Levered_Free_Cash_Flow":"'+screenerdatabean.Levered_Free_Cash_Flow+'",'
    input +=  '"Diluted_EPS":"'+screenerdatabean.Diluted_EPS+'",'
    input +=  '"Return_on_Assets":"'+screenerdatabean.Return_on_Assets+'",'
    input +=  '"Return_on_Equity":"'+screenerdatabean.Return_on_Equity+'",'
    input +=  '"Current_Ratio":"'+screenerdatabean.Current_Ratio+'",'
    input +=  '"Short_Ratio":"'+screenerdatabean.Short_Ratio+'",'
    input +=  '"Short_of_Float":"'+screenerdatabean.Short_of_Float+'",'
    input +=  '"Total_Debt":"'+screenerdatabean.Total_Debt+'",'
    input +=  '"Total_Debt_Equity":"'+screenerdatabean.Total_Debt_Equity+'",'
    input +=  '"Profit_Margin":"'+screenerdatabean.Profit_Margin+'",'
    input +=  '"Operating_Margin":"'+screenerdatabean.Operating_Margin+'",'
    input +=  '"Payout_Ratio":"'+screenerdatabean.Payout_Ratio+'",'
    input +=  '"Held_by_Insiders":"'+screenerdatabean.Held_by_Insiders+'",'
    input +=  '"Held_by_Institutions":"'+screenerdatabean.Held_by_Institutions+'",'
    input +=  '"companyType":"'+screenerdatabean.companyType+'"}'
    input +=  ''
    
    print("############- JSON DATA - ##############")
    print(input)
    return render(request,"Screener.html",{"fundamentaldata":result,"limit":100, "complanyType":"nifty500","input":input, "pagecount":pagecount,"currentpage":currentpage})

def fundamentalDataHomeResponse(request,**kwargs):
        value=request.GET["Trailing_P_E"]
        print("########################Value#############")
        print(value)
        start=0
        limit=100
        if(companyType == "nifty50"):
             result=nifty_50_companies_fundamental_data.objects[start:limit]
        elif(companyType == "nifty100"):
             result=nifty_100_companies_fundamental_data.objects[start:limit]
        elif(companyType == "nifty200"):
             result=nifty_200_companies_fundamental_data.objects[start:limit]
        elif(companyType == "nifty500"):
             result=nifty_500_companies_fundamental_data.objects[start:limit]
        else:
            result=nifty_500_companies_fundamental_data.objects[0:100]
            
        return render(request,"screenerResponse.html",{"fundamentaldata":result,"limit":100, "companyType":companyType})
    