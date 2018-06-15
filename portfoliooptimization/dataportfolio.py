import datetime as dt
from datetime import date, datetime
import calendar
import os
import pandas as pd
import sys
from mpld3._display import fig_to_html,save_json
from batchprocessing.models import nift50Indices,nift100Indices,nift200Indices,nift500Indices,nifty_50_fundamental_data,nifty_100_companies_fundamental_data,nifty_200_companies_fundamental_data,nifty_500_companies_fundamental_data,niftBanchMarkIndices
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
import seaborn as sns
import inspect
import screener.portfoliooptimization as po
import matplotlib.ticker as tkr

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"
#Dates
end_date = dt.date.today()
emo = end_date.month
eday = end_date.day
eyear = end_date.year
emonth = calendar.month_abbr[emo]

def optimizePortfolio(portfolio,start_date):
    portfolio=portfoliodetail(portfolio,start_date)
    return portfolio

def portfoliodetail(portfolio,start_date):
    symbolss = portfolio.Ticker_List
    #Portfolio Data
    merged_data_frame = pd.DataFrame()
    i=0
    for sysm in symbolss:
        if portfolio.Company_Type =="nifty50":
            objnf50=nift50Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Close','Date')
        elif portfolio.Company_Type =="nifty100":
            objnf50=nift100Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Close','Date')
        elif portfolio.Company_Type =="nifty200":
            objnf50=nift200Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Close','Date')
        else:
            objnf50=nift500Indices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=sysm).values_list('Close','Date')
        
        if i==0:
            merged_data_frame=pd.DataFrame(list(objnf50),columns=[sysm,'Date'])
            merged_data_frame=merged_data_frame.set_index('Date')
        else:    
            data_frame =pd.DataFrame(list(objnf50),columns=[sysm,'Date'])
            data_frame=data_frame.set_index('Date')
            merged_data_frame = pd.merge(
                merged_data_frame, data_frame, right_index=True, left_index=True, how='outer')
        i+=1
    temp_data = merged_data_frame.iloc[:,0:len(merged_data_frame.columns)].apply(pd.to_numeric)
    for column in temp_data.columns:
        c = temp_data[column]
        if c.isnull().all():
            print ("WARNING:  The following symbol: '+str(column)+' has no timeseries data. This could be due to an invalid ticker, or an entry not supported by Quandl. \n You will not be able to proceed with any function in the script until all of the symbols provided are downloaded.")
            sys.exit()
    allocations = []
    for tk in portfolio.Ticker_List:
        allocations.append(10)
    port_val = merged_data_frame * allocations
    port_val = port_val.fillna(port_val.mean())
    port_val['Portfolio Value'] = port_val.astype(float).sum(axis=1,skipna=True,numeric_only=True)
    port_rets = port_val.astype(float).pct_change()
    port_rets = port_rets.dropna(how='any')
    assets = port_val.tail(1)
    s = port_val.iloc[-1:, -1]
    port_weights = assets / int(s)
    port_weights = port_weights.transpose()
    port_weights.columns = ["Weight"]
    port_weights = port_weights.drop(port_weights.index[len(port_weights) - 1])
    portfolio.correlationData=fig_to_html(correlData(merged_data_frame.astype(float)))
    portfolio.riskandreturnData=fig_to_html(risk_return(port_rets.astype(float)))
    portfolio.banchmarkData=benchmark(portfolio,port_rets.astype(float),merged_data_frame.astype(float),port_val,start_date)
    num_portfolios = 25000
    portfolio.heatMapData=fig_to_html(po.portfolioOptimization(portfolio,start_date,end_date,num_portfolios))
    portfolio.violationData=fig_to_html(violin(port_rets.astype(float),start_date))
    portfolio.minvariance=fig_to_html(min_var(portfolio,port_rets.astype(float)))
    portfolio.boxplotData= fig_to_html(box_plot(port_rets.astype(float),0))
    portfolio.weightplotData=fig_to_html(weights_plot(port_weights.astype(float)))
    port_val.to_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Value.csv',index=True)
    port_rets.to_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Returns.csv' ,index=True)
    merged_data_frame.to_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Daily_Prices.csv' ,index=True)
    port_weights.to_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Weights.csv' ,index=True)

    return portfolio
    
def benchmark(portfolio,port_rets,port_data,port_val,start_date):
    
    bench_symbol ="%5Ensei"
    banchmarkData=niftBanchMarkIndices.objects.filter(Date__gte=start_date, Date__lte=end_date,Ticker=bench_symbol).values_list('Date','Close')
    bench_data=pd.DataFrame(list(banchmarkData),columns=['Date','Close'])
    bench_rets = bench_data.iloc[::-1]
    bench_rets = bench_rets.dropna(how='any')
    #bench_rets['Close'] = bench_rets['Close'].astype(float).pct_change(1)
    bench_rets['Close'] = np.log(bench_rets['Close'].astype(float).shift(1)) - np.log(bench_rets['Close'].astype(float))
    bench_rets = bench_rets.dropna(how='any')
    
    bench_data.to_csv(root_path+'/Daily_Data/Benchmark/Benchmark_Price_Data.csv' ,index=False)
    bench_rets.to_csv(root_path+'/Daily_Data/Benchmark/Benchmark_Returns.csv' ,index=False)
    
    print("Benchmark data has finished downloading.'")

    return portfolioBanchmark(portfolio,port_rets,port_data,port_val,bench_rets,bench_data)



style.use('ggplot')

def portfolioBanchmark(portfolio,port_rets,port_data,port_val,bench_rets,bench_data):
    bench_rets.columns = ['Date', 'Return']
    bench_data.columns = ['Date','Close']
    if not os.path.exists(root_path + '/Figures'):
        os.mkdir(root_path + '/Figures')

        # ----------Plot Performance--------------#
        #port_val = port_val.set_index('Date')
    port_values = port_val['Portfolio Value']
    port_values = pd.DataFrame(port_values)
    bench_values = bench_data.set_index('Date')

    perf = pd.merge(port_values, bench_values, left_index=True, right_index=True)

    port_data = perf["Portfolio Value"]
    bench_d = perf["Close"]

    fig = plt.figure()
    ax = fig.add_subplot(111, facecolor='#576884')
    fig.set_size_inches(11.7, 8.27)
    ax2 = ax.twinx()
    ax2.grid(None)
    print("########bench_d##########")
    print(bench_d)
    print("########port_data##########")
    print(port_data)
    lns1 = ax2.plot(bench_d, linestyle='-', color='#6aa527', label='Nifty50')
    lns2 = ax.plot(port_data, linestyle='-', color="white", label='Portfolio')  
    fig.add_axes(ax,ax2)              
        # added these three lines
    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)
    ax.grid(linestyle='--', alpha=0.2)
    print(tkr.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.get_yaxis().set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x), ',')))

        #Annotate Last Price
    print(json_serial(port_val.index[-1]))    
    bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
    ax.annotate("{:0,.2f}".format(port_val["Portfolio Value"][-1]), (json_serial(port_val.index[-1]), port_val["Portfolio Value"][-1]),
                     xytext=(json_serial(port_val.index[-1]), port_val["Portfolio Value"][-1]), bbox=bbox_props)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.title(portfolio.Portfolio_Name+" Portfolio Performance vs. Nifty 50 Benchmark")
    plt.savefig(root_path + "/Figures/"+portfolio.Portfolio_Name+"_port_perf.png")
   
    plt.tight_layout()
    fig.tight_layout()
    return  "/static/Figures/"+portfolio.Portfolio_Name+"_port_perf.png"

def correlData(pdata):
        cor = pdata.corr()
        print("########## cor ##########")
        print(cor)
        data = cor.values
        print("########## data ##########")
        print(data)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        fig.set_size_inches(11.7, 8.27)
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

        #if call_name != "diversification":
         #   plt.show()
        save_json(fig,"correlation.json")
        return fig


def risk_return(port_rets):
        #port_rets=getPortfolioRiskReturn(portfolio,start_date)
        x = (port_rets.std() * np.sqrt(252)) * 100
        x = x[:-1]
        y = (port_rets.mean() * 252) * 100
        y = y[:-1]
        n = y.index
        fig = plt.figure()
        fig.set_size_inches(11.7, 8.27)
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
        plt.title("Risk / Return of Assets", fontsize=15)
        plt.xlabel("Risk", fontsize=10)
        plt.ylabel("Return", fontsize=10)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        save_json(fig,"risk_return.json")
        return fig
   
def violin(port_rets,start_date):
        print(port_rets)
        group=0
        port_rets['month'] = pd.DatetimeIndex(port_rets.index).month
        port_rets['day'] = pd.DatetimeIndex(port_rets.index).weekday_name
        port_rets['month'] = port_rets['month'].apply(lambda x: calendar.month_abbr[x])
        fig, ax = plt.subplots()
        # the size of A4 paper
        fig.set_size_inches(11.7, 8.27)

        if group == "day":
            sns.violinplot(x="day", y="Portfolio Value", data=port_rets, palette="Pastel1",ax=ax)
            title = "Daily Returns"
        else:
            title = "Monthly Returns"
            sns.violinplot(x="month", y="Portfolio Value", data=port_rets, palette="Pastel1",ax=ax)

        #Modify x axis labels
        sns.despine()
        #vals = ax.get_yticks()
        #ax.set_yticklabels(['{:.2f}%'.format(x * 100) for x in vals])
        #ax.set_xlabel('')
        #ax.set_ylabel('')
        plt.title(title,fontsize=15)
        save_json(fig,"violation.json")
        return fig
        
def box_plot(port_rets,group):
        port_rets['month'] = pd.DatetimeIndex(port_rets.index).month
        port_rets['day'] = pd.DatetimeIndex(port_rets.index).weekday_name
        port_rets['month'] = port_rets['month'].apply(lambda x: calendar.month_abbr[x])
        print("############ port_rets['month'] #######")
        print(port_rets)
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        if group == "day":
            title = "Daily Returns"
            ax = sns.boxplot(ax=ax,x="day", y="Portfolio Value", data=port_rets, palette="Pastel1")
            ax = sns.swarmplot(ax=ax,x="day", y="Portfolio Value", data=port_rets, color="grey")
            sns.despine()
        else:
            title = "Monthly Returns"
            ax = sns.boxplot(ax=ax,x="month", y="Portfolio Value", data=port_rets, palette="Pastel1")
            ax = sns.swarmplot(ax=ax,x="month", y="Portfolio Value", data=port_rets, color="grey")
            sns.despine()
        #Modify x axis labels
        vals = ax.get_yticks()
        ax.set_yticklabels(['{:.2f}%'.format(x * 100) for x in vals])
        ax.set_xlabel('')
        ax.set_ylabel('')
        plt.title(title, fontsize=18)
        return plt.gcf()
        
def calmap(port_rets):
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
        
def weights_plot(port_weights):
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.set_size_inches(11.7, 8.27)
    plt.pie(
            port_weights["Weight"],
            labels=port_weights.index,
            shadow=False,
            startangle=90,
            autopct='%1.1f%%',
        )

    plt.axis('equal')
    plt.title("Portfolio Weights", fontsize=18)
        #plt.show()
    return fig

def min_var(portfolio,port_rets):
        symbols= portfolio.Ticker_List
        n = len(port_rets.columns) - 1
        returns = port_rets.iloc[:,0:n]

        cov_matrix = returns.astype(float).cov()
        mean_daily_returns = returns.astype(float).mean()

        # set number of runs of random portfolio weights
        num_portfolios = 25000

        # set up array to hold results
        # We have increased the size of the array to hold the weight values for each stock
        results = np.zeros((4 + len(symbols) - 1, num_portfolios))

        for i in range(num_portfolios):
            # select random weights for portfolio holdings
            weights = np.array(np.random.random(len(symbols)))

            # rebalance weights to sum to 1
            weights /= np.sum(weights)

            # calculate portfolio return and volatility
            portfolio_return = np.sum(mean_daily_returns * weights) * 252
            portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)

            # store results in results array
            results[0, i] = portfolio_return
            results[1, i] = portfolio_std_dev

            # store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
            results[2, i] = results[0, i] / results[1, i]

           # iterate through the weight vector and add data to results array
            for j in range(len(weights)):
                results[j + 3, i] = weights[j]

        # convert results array to Pandas DataFrame
        flds = ['ret', 'stdev', 'sharpe']
        lista = flds + symbols
        results_frame = pd.DataFrame(results.T,
                                     columns=lista)

        # locate position of portfolio with highest Sharpe Ratio
        max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]
        # locate positon of portfolio with minimum standard deviation
        min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]
        fig, ax = plt.subplots()
        #print(results_frame)

        print ("-------------Max Sharpe Portfolio------------")
        print(max_sharpe_port)
        print ("\n")
        print ("-------------Minimum Variance Portfolio------------")
        print(min_vol_port)

        plt.scatter(results_frame.stdev, results_frame.ret, c=results_frame.sharpe, cmap='plasma')
        plt.title('Efficient Froniter of a ' + str(len(symbols)) + ' Asset Portfolio', fontsize=14, fontweight='bold', y=1.02)
        plt.xlabel('Risk')
        plt.ylabel('Return')
        clb = plt.colorbar()
        clb.ax.set_ylabel('Sharpe Ratio Value', color='Black')
        plt.scatter(max_sharpe_port[1], max_sharpe_port[0], marker='o', color='b', s=20, label='Tangent Portfolio')
        plt.scatter(min_vol_port[1], min_vol_port[0], marker='o', color='r', s=20, label='Minimum Variance Portfolio')
        plt.legend(loc='upper left', fontsize='small')
        #plt.show()
        fig.set_size_inches(11.7, 8.27)
        return fig


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
