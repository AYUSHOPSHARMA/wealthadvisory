import pandas as pd
import requests
from requests.exceptions import HTTPError
import matplotlib.pyplot as plt
import inspect
from batchprocessing.models import portfolio
import os
from batchprocessing.models import nift50Indices,nift100Indices,nift200Indices,nift500Indices

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

#whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def info(portfolioobj):
       weights = pd.read_csv(root_path + '/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Weights.csv', index_col=0)
       industry_info = pd.DataFrame()
       for symbol in portfolioobj.Ticker_List:
           if portfolioobj.Company_Type =="nifty50":
               objnf50=nift50Indices.objects.filter(Ticker=symbol).values_list('Industry').distinct('Industry')
           elif portfolioobj.Company_Type =="nifty100":
               objnf50=nift100Indices.objects.filter(Ticker=symbol).values_list('Industry').distinct('Industry')
           elif portfolioobj.Company_Type =="nifty200":
               objnf50=nift200Indices.objects.filter(Ticker=symbol).values_list('Industry').distinct('Industry')
           else:
               objnf50=nift500Indices.objects.filter(Ticker=symbol).values_list('Industry').distinct('Industry')
           for indsObj in objnf50:
               industry_info = industry_info.append({'Industry': indsObj, 'Symbol': symbol}, ignore_index=True)

       industry_info.set_index('Symbol', inplace=True)
       print("########industry_info ####")
       print(industry_info)
       print("###########weights ####")
       print(weights)
       dat1 = pd.concat([industry_info, weights], axis=1)
       dat1.columns = ["Industry", "Weight"]
       t = dat1.groupby(["Industry"]).sum()
       t.to_csv(root_path+'/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Industrial_Weights.csv', index=True)
       fig= plt.figure()
       plt.pie(
        t["Weight"],
        labels=t.index,
        shadow=False,
        startangle=90,
        autopct='%1.1f%%',
        )

       plt.axis('equal')
       plt.suptitle('Industrial Weights')
       fig.savefig(root_path + '/Figures/'+portfolioobj.Portfolio_Name+'_ind_pie.png')

       call_name = inspect.stack()[1][3]

       if call_name != "diversification":
           plt.show()

    #rpdf = pd.concat([sector_info, industry_info], axis=1)
    #rpdf.to_csv(root_path+'/Daily Data/Portfolio/Asset Exposure.csv',index=True)

