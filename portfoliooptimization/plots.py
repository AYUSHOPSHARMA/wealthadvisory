import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as mtick
from matplotlib import style
import os
import seaborn as sns
import calendar
import inspect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

style.use('ggplot')

def correl(portfolio,type='data'):
        type = type.lower()
        if type == "returns":
            pdata = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Returns.csv',index_col=0)
            n = len(pdata.columns) - 1
            pdata = pdata.iloc[:,0:n]
        else:
            pdata = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Daily_Prices.csv' ,index_col=0)

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

        plt.savefig(root_path + '/Figures/'+portfolio.Portfolio_Name+'_port_correl.png')

        call_name = inspect.stack()[1][3]

        if call_name != "diversification":
            plt.show()

def risk_return(portfolio):
        port_rets = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Returns.csv', index_col=0)
        x = (port_rets.std() * np.sqrt(252)) * 100
        x = x[:-1]
        y = (port_rets.mean() * 252) * 100
        y = y[:-1]
        n = y.index
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        t = x
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

def violin(portfolio,group=0):
        port_rets = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Returns.csv')
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

def box_plot(portfolio,group=0):
        port_rets = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Returns.csv')
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

def calmap(portfolio):
        port_rets = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Returns.csv',index_col=0)

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

def weights_plot(portfolio):
        port_weights = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portfolio.Portfolio_Name+'_Portfolio_Weights.csv',index_col=0)

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
