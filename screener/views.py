from django.shortcuts import render
import screener.fundamentalData as fd
import json
from batchprocessing.models import nifty_500_companies_fundamental_data
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
    result=nifty_500_companies_fundamental_data.objects[0:20]
    return render(request,"Screener.html",{"fundamentaldata":result,"limit":20})
    