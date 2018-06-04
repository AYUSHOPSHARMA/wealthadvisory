import quandl
import datetime as dt
import calendar
import os
import pandas as pd
import sys
from main import root_path
from batchprocessing.models import nift50Indices
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as mtick
from matplotlib import style
import os
from main import root_path
import seaborn as sns
import calendar
import inspect

#Dates
end_date = dt.date.today()
emo = end_date.month
eday = end_date.day
eyear = end_date.year
emonth = calendar.month_abbr[emo]

def portfolio(symbols, allocations, api_key, start_date):
    symbolss = ['ASIANPAINT.NS','ADANIPORTS.NS']
    #Portfolio Data
    print("Port Folio Data##########")
    print(start_date)
    print(end_date)
    print("########################")
    merged_data_frame = pd.DataFrame()
    i=0
    for sysm in symbolss:
        objnf50=nift50Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm)
        objclose= objnf50.values_list('Close')
        objdt= objnf50.values_list('Date')
        closelist=list(objclose)
        datelist=list(objdt)
        if i==0:
            merged_data_frame=pd.DataFrame(closelist,columns=[sysm], index=[datelist])
        else:    
            data_frame =pd.DataFrame(closelist,columns=[sysm], index=[datelist])
            print("########### INSIDE DF ########")
            merged_data_frame = pd.merge(
                merged_data_frame, data_frame, right_index=True, left_index=True, how='outer')
        i+=1
    print("#########port_datalist###############")
    merged_data_frame=merged_data_frame.reindex(merged_data_frame.index.rename(['Date']))
    print(merged_data_frame)      
    print("#########END port_datalist###############")
    print(merged_data_frame.columns)
    print("########### INSIDE merged_data_frame ########")
    print(merged_data_frame.index.name)  
    temp_data = merged_data_frame.iloc[:,0:len(merged_data_frame.columns)].apply(pd.to_numeric)
    for column in temp_data.columns:
        c = temp_data[column]
        if c.isnull().all():
            print ("WARNING:  The following symbol: '+str(column)+' has no timeseries data. This could be due to an invalid ticker, or an entry not supported by Quandl. \n You will not be able to proceed with any function in the script until all of the symbols provided are downloaded.")
            sys.exit()

    port_val = merged_data_frame * allocations
    # Remove Rows With No Values

    #FIX!!!!!!
    #port_data.dropna(axis=0, how='any')
    port_val = port_val.fillna(port_val.mean())

    port_val['Portfolio Value'] = port_val.sum(axis=1)

    # Calculate Portfolio Returns
    port_rets = port_val.pct_change()
    port_rets = port_rets.dropna(how='any')

    #Calculate Portfolio Weights
    assets = port_val.tail(1)
    s = port_val.iloc[-1:, -1]
    port_weights = assets / int(s)
    port_weights = port_weights.transpose()
    port_weights.columns = ["Weight"]
    port_weights = port_weights.drop(port_weights.index[len(port_weights) - 1])
    
    print("###########port_val###########")
    print(port_val)
    print("###########port_rets###########")
    print(port_rets)
    print(merged_data_frame)
    print("###########port_weights###########")
    print(port_weights)
    correlData(type,merged_data_frame)
    #risk_return(port_rets)
    
def benchmark(bench_symbol, start_date, api_key):

    quandl.ApiConfig.api_key = api_key

    folders = [root_path + '/Daily Data', root_path + '/Daily Data/Benchmark', root_path + '/Daily Data/Portfolio' ]
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

    smo = start_date.month
    sday = start_date.day
    syear = start_date.year
    smonth = calendar.month_abbr[smo]

    #Benchmark Data
    bench_data = pd.read_csv(
        'http://finance.google.com/finance/historical?q='+str(bench_symbol)+'&startdate='+ str(smonth) +'+'+ str(sday) +'+'+ str(syear) +'&enddate='+ str(emonth) +'+'+ str(eday) +'+'+ str(eyear) +'&output=csv',
        index_col=0)["Close"]
    bench_data.index = pd.to_datetime(bench_data.index)

    #Reverse Frame
    bench_rets = bench_data.iloc[::-1]
    bench_rets = bench_rets.dropna(how='any')

    bench_rets = bench_rets.pct_change()

    bench_data.to_csv(root_path+'/Daily Data/Benchmark/Benchmark Price Data.csv' ,index=True)
    bench_rets.to_csv(root_path+'/Daily Data/Benchmark/Benchmark Returns.csv' ,index=True)

    print("Benchmark data has finished downloading.'")# -*- coding: utf-8 -*-


style.use('ggplot')

def correlData(type,pdata):
        cor = pdata.corr()
        data = cor.values

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        heatmap = ax.pcolor(data, cmap=plt.cm.coolwarm)
        fig.colorbar(heatmap)
        ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
        ax.set_yticks(np.arange(data.shape[0]) + 0.5, minor=False)
        ax.invert_yaxis()

        column_labels = cor.columns
        row_labels = cor.index

        ax.set_xticklabels(column_labels, rotation=90, fontsize=8)
        ax.set_yticklabels(row_labels, fontsize=8)
        heatmap.set_clim(-1, 1)
        plt.title('Portfolio Correlation', fontsize=15)
        plt.tight_layout()

        #plt.savefig(root_path + '/Figures/port_correl.png')

        call_name = inspect.stack()[1][3]
        print("call_name########")
        print(call_name)      

        if call_name != "diversification":
            plt.show()

def risk_return(port_rets):
        x = (port_rets.std() * np.sqrt(252)) * 100
        x = x[:-1]
        y = (port_rets.mean() * 252) * 100
        y = y[:-1]
        n = y.index
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        t = x
        print("############x#############")
        print(x)
        print("############Y#############")
        print(y)
        ax.scatter(x, y, c=t, cmap='jet')

        fmt = '%.2f%%'  # Format you want the ticks, e.g. '40%'
        xticks = mtick.FormatStrFormatter(fmt)
        ax.xaxis.set_major_formatter(xticks)
        ax.yaxis.set_major_formatter(xticks)

        for i, txt in enumerate(n):
            ax.annotate(txt, (x[i], y[i]))

        plt.suptitle("Risk / Return of Assets")
        plt.xlabel("Risk", fontsize=10)
        plt.ylabel("Return", fontsize=10)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.show()
   
def violin(group=0):
    if os.path.exists(root_path + '/Daily Data/Portfolio/Portfolio Returns.csv'):
        port_rets = pd.read_csv(root_path + '/Daily Data/Portfolio/Portfolio Returns.csv')
        port_rets['month'] = pd.DatetimeIndex(port_rets['Date']).month
        port_rets['day'] = pd.DatetimeIndex(port_rets['Date']).weekday_name
        port_rets['month'] = port_rets['month'].apply(lambda x: calendar.month_abbr[x])

        if group == "day":
            ax = sns.violinplot(x="day", y="Portfolio Value", data=port_rets, palette="Pastel1")
            title = "Daily Returns"
        else:
            title = "Monthly Returns"
            ax = sns.violinplot(x="month", y="Portfolio Value", data=port_rets, palette="Pastel1")

        #Modify x axis labels
        vals = ax.get_yticks()
        ax.set_yticklabels(['{:.2f}%'.format(x * 100) for x in vals])
        ax.set_xlabel('')
        ax.set_ylabel('')
        plt.suptitle(title)
        plt.show()
    else:
        print ("You have not downloaded data for your portfolio yet in oder for the optimization module to be run. Please download the data by running the following function --- port_data.portfolio_daily_data()")

def box_plot(group=0):
    if os.path.exists(root_path + '/Daily Data/Portfolio/Portfolio Returns.csv'):
        port_rets = pd.read_csv(root_path + '/Daily Data/Portfolio/Portfolio Returns.csv')
        port_rets['month'] = pd.DatetimeIndex(port_rets['Date']).month
        port_rets['day'] = pd.DatetimeIndex(port_rets['Date']).weekday_name
        port_rets['month'] = port_rets['month'].apply(lambda x: calendar.month_abbr[x])

        if group == "day":
            title = "Daily Returns"
            ax = sns.boxplot(x="day", y="Portfolio Value", data=port_rets, palette="Pastel1")
            ax = sns.swarmplot(x="day", y="Portfolio Value", data=port_rets, color="grey")

        else:
            title = "Monthly Returns"
            ax = sns.boxplot(x="month", y="Portfolio Value", data=port_rets, palette="Pastel1")
            ax = sns.swarmplot(x="month", y="Portfolio Value", data=port_rets, color="grey")

        #Modify x axis labels
        vals = ax.get_yticks()
        ax.set_yticklabels(['{:.2f}%'.format(x * 100) for x in vals])
        ax.set_xlabel('')
        ax.set_ylabel('')
        plt.suptitle(title)
        plt.show()
    else:
        print ("You have not downloaded data for your portfolio yet in oder for the optimization module to be run. Please download the data by running the following function --- port_data.portfolio_daily_data()")

def calmap():
    if os.path.exists(root_path + '/Daily Data/Portfolio/Portfolio Returns.csv'):
        port_rets = pd.read_csv(root_path + '/Daily Data/Portfolio/Portfolio Returns.csv',index_col=0)

        import numpy as np;
        np.random.seed(sum(map(ord, 'calmap')))
        import calmap

        events = port_rets['Portfolio Value']
        events.index = pd.to_datetime(events.index)

        #calmap.yearplot(events, year=2018)

        calmap.calendarplot(events, monthticks=3, daylabels='MTWTFSS',
                            dayticks=[0, 2, 4, 6], cmap='YlGn',
                            fillcolor='grey', linewidth=0,
                            fig_kws=dict(figsize=(8, 4)))
        plt.show()
    else:
        print ("You have not downloaded data for your portfolio yet in oder for the optimization module to be run. Please download the data by running the following function --- port_data.portfolio_daily_data()")

def weights_plot():
    if os.path.exists(root_path + '/Daily Data/Portfolio/Portfolio Weights.csv'):
        port_weights = pd.read_csv(root_path + '/Daily Data/Portfolio/Portfolio Weights.csv',index_col=0)

        plt.pie(
            port_weights["Weight"],
            labels=port_weights.index,
            shadow=False,
            startangle=90,
            autopct='%1.1f%%',
        )

        plt.axis('equal')
        plt.suptitle('Portfolio Weights')
        plt.show()

    else:
        print ("You have not downloaded data for your portfolio yet in oder for the optimization module to be run. Please download the data by running the following function --- port_data.portfolio_daily_data()")
