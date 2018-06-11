import bs4 as bs
import pandas as pd
import numpy as np
import datetime as dt
import calendar
import os
import requests
import inspect
import re
from batchprocessing.models import nifty_50_fundamental_data,nifty_100_companies_fundamental_data,nifty_200_companies_fundamental_data,nifty_500_companies_fundamental_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

#Check if data downloaded to run functions
def fundis(rate, method,portfolioobj):
        print(root_path)
        weights = pd.read_csv(root_path + '/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Weights.csv', index_col=0)
        symbols = portfolioobj.Ticker_List
        columns = ["Trailing P/E","Forward P/E","PEG","Price/Book","Beta","Dividend Yield"]
        fundamental_df = pd.DataFrame(columns=columns, index=symbols[:1])
            #Ensure proper notation
            #Web scrape data
        for symbol in portfolioobj.Ticker_List:
            if portfolioobj.Company_Type =="nifty50":
                objnf50=nifty_50_fundamental_data.objects.filter(Ticker=symbol).values_list('Ticker','Trailing_P_E','Forward_P_E','PEG_Ratio','Price_Book','Beta','Trailing_Annual_Dividend_Yield','Year_5_Average_Dividend_Yield')
            elif portfolioobj.Company_Type =="nifty100":
                objnf50=nifty_100_companies_fundamental_data.objects.filter(Ticker=symbol).values_list('Ticker','Trailing_P_E','Forward_P_E','PEG_Ratio','Price_Book','Beta','Trailing_Annual_Dividend_Yield','Year_5_Average_Dividend_Yield')
            elif portfolioobj.Company_Type =="nifty200":
                objnf50=nifty_200_companies_fundamental_data.objects.filter(Ticker=symbol).values_list('Ticker','Trailing_P_E','Forward_P_E','PEG_Ratio','Price_Book','Beta','Trailing_Annual_Dividend_Yield','Year_5_Average_Dividend_Yield')
            else:
                objnf50=nifty_500_companies_fundamental_data.objects.filter(Ticker=symbol).values_list('Ticker','Trailing_P_E','Forward_P_E','PEG_Ratio','Price_Book','Beta','Trailing_Annual_Dividend_Yield','Year_5_Average_Dividend_Yield')
                
            for obj in objnf50:
                    print(obj[0])
                    fundamental_df.ix[symbol,"Trailing P/E"] = obj[1]
                    fundamental_df.ix[symbol,"Forward P/E"] = obj[2]
                    fundamental_df.ix[symbol,"PEG"] = obj[3]
                    fundamental_df.ix[symbol,"Price/Book"] = obj[4]
                    fundamental_df.ix[symbol,"Beta"] = obj[5]
                    s=str(obj[6])
                    if "%" in s:
                        s = s[-1] 
                    fundamental_df.ix[symbol,"Dividend Yield"] = s
                    r= obj[7]
                    if r == "N/A":
                        r = 0
                    rf=r
            print(fundamental_df.mean()) 
            print("MEAN###########")
            fundamental_df.fillna(fundamental_df.mean())
            fundamental_df=fundamental_df.replace("N/A",0)
            fundamental_df=fundamental_df.replace("%","")
            print("#########")
            print(fundamental_df)       
        fundis = fundamental_df.apply(pd.to_numeric)
        fundis["Dividend Yield"] = fundis["Dividend Yield"] / 100
        weights = weights["Weight"].tolist()
        temp = fundis.multiply(weights, axis=0)

            # Output
        weighted_metrics = temp.sum()

        call_name = inspect.stack()[1][3]
        print(weighted_metrics)

            #Save data
        weighted_metrics.to_csv(root_path + '/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Fundis.csv', index=True)
        fundis.to_csv(root_path + '/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Asset_Fundis.csv', index=True)
        port_val= pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Value.csv')
        port_rets= pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Returns.csv')
        port_data= pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Daily_Prices.csv')

        bench_data= pd.read_csv(root_path+'/Daily_Data/Benchmark/Benchmark_Price_Data.csv')
        bench_rets= pd.read_csv(root_path+'/Daily_Data/Benchmark/Benchmark_Returns.csv')
    
        bench_rets.columns = ['Date', 'Return']
        bench_data.columns = ['Date', 'Close']

        weighted_metrics = pd.read_csv(root_path + '/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Fundis.csv', index_col=0)
        beta = float(weighted_metrics.iloc[3])

            #YTD Return
        spy_ytd = float(bench_data.iloc[0, 1]) / float(bench_data.iloc[-1, 1]) - 1
        port_ytd = float(port_val['Portfolio Value'].iloc[-1]) / float(port_val['Portfolio Value'].iloc[0]) - 1

            # STDEV
        port_std = port_rets['Portfolio Value'].std() * np.sqrt(252)
        bench_std = float(bench_rets.std() * np.sqrt(252))

            # Treynor
        print("##########Treynor########")    
        print(port_ytd)
        print(rf)
        print(beta)
        port_treynor = (float(port_ytd) - float(rf)) / float(beta)
        market_treynor = (float(spy_ytd) - float(rf)) / 1

            # Alpha
        port_alpha = float(port_ytd) - (float(rf) + (float(spy_ytd) - float(rf)) * float(beta))

            # Sharpe
        sharpe_port = (float(port_ytd) - float(rf)) / float(port_std)
        sharpe_spy = (float(spy_ytd) - float(rf)) / float(bench_std)

        call_name = inspect.stack()[1][3]

        if call_name != "mets":
            print("\n")
            print("----------Risk Adjusted Metrics-----------")
            print ("Current Risk Free Rate " + rate + ": " + "{0:.2f}%".format(rf * 100))
            print ("Portfolio Raw Return: " + "{0:.2f}%".format(port_ytd * 100))
            print ("Benchmark Return: " + "{0:.2f}%".format(spy_ytd * 100))
            print ("Portfolio Volatility: " + "{0:.2f}%".format(port_std * 100))
            print ("Market Volatility: " + "{0:.2f}%".format(bench_std * 100))
            print ("Portfolio Sharpe: " + "{0:.2f}".format(sharpe_port))
            print ("Market Sharpe: " + "{0:.2f}".format(sharpe_spy))
            print ("Portfolio Treynor: " + "{0:.2f}".format(port_treynor))
            print ("Market Treynor: " + "{0:.2f}".format(market_treynor))
            print ("Portfolio Alpha: " + "{0:.2f}%".format(port_alpha * 100))
        else:
            data = [['','Volatility','Sharpe Ratio', 'Treynor Ratio','Alpha'],
                        ['Portfolio',"{0:.2f}%".format(port_std * 100),"{0:.2f}".format(sharpe_port),"{0:.2f}".format(port_treynor),"{0:.2f}%".format(port_alpha * 100)],
                        ['Benchmark',"{0:.2f}%".format(bench_std * 100),"{0:.2f}".format(sharpe_spy),"{0:.2f}".format(market_treynor),"-"]]

        return data
