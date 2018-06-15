import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.ticker as tkr
import os
import inspect
style.use('ggplot')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

def portfolio(portobj):
    print("#####portobj#######")
    print(portobj.Company_Type)
    port_rets = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portobj.Portfolio_Name+'_Portfolio_Returns.csv')
    port_data = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portobj.Portfolio_Name+'_Portfolio_Daily_Prices.csv')
    port_val = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portobj.Portfolio_Name+'_Portfolio_Value.csv')
    bench_rets = pd.read_csv(root_path+'/Daily_Data/Benchmark/Benchmark_Returns.csv')
    bench_data = pd.read_csv(root_path+'/Daily_Data/Benchmark/Benchmark_Price_Data.csv')
    bench_rets.columns = ['Date','Return']
    bench_data.columns = ['Date','Close']
    bench_rets=bench_rets.set_index('Date')
    bench_data=bench_data.set_index('Date')
    port_rets=port_rets.set_index('Date')
    port_data=port_data.set_index('Date')
    print("######## inside portfolio port_rets #######")
    print(port_rets)
    print("######## inside portfolio bench_rets#######")
    print(bench_rets)       
    return port_rets, bench_rets

    
def asset_performance(portfolio):

        port_rets = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Returns.csv')
        port_val = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Value.csv')

        port_val = port_val.set_index('Date')
        port_rets = port_rets.set_index('Date')

        asset_performance = port_val.iloc[-1] / port_val.iloc[0] - 1
        asset_performance = asset_performance[:-1]
        asset_performance = asset_performance.sort_values(ascending=False)

        top_holdings = port_val.iloc[-1]
        top_holdings = top_holdings[:-1]
        top_holdings = top_holdings.sort_values(ascending=False)

        call_name = inspect.stack()[1][3]

        daily_perf_asset = port_rets.iloc[-1,0:len(port_rets.columns) - 1]

        if call_name != "perf":
            print ("--------Asset Performance Today--------")
            for ticker, val in zip(daily_perf_asset.index, daily_perf_asset):
                print (ticker, "{0:.2f}%".format(val * 100))

            print ("--------Top Performers Since Allocation--------")
            for ticker, val in zip(asset_performance.index, asset_performance):
                print (ticker, "{0:.2f}%".format(val * 100))

            print ("--------Top Holdings By Dollar Amount--------")
            for ticker, val in zip(top_holdings.index, top_holdings):
                print (ticker, "${:,.2f}".format(val))

        return asset_performance
    