#------------Necessary Variables--------------#
import datetime as dt

symbols = ['AAPL', 'MMM', 'INTC', 'JPM', 'DE', 'WFC', 'BK', 'PM', 'HD', 'GE']
allocations = [10,10]
start_date = dt.date(2017,1,3)

#Benchmark Index
bench_symbol = "ONGC.NS"

#RF Syntax: 6 MO, 2 YR etc.
rate = '1 YR'
#CUR, AVG
method = "AVG"

#For Quandl
api_key = "37NeVhjr4KhAPxKds_jZ"

#Dirctory Input For Data and Reports
root_path = "C:/Portfolio Tracker"

#------------Run Program----------------------#
if __name__ == '__main__':
    #import generatereport
    #from batchprocessing.models import portfolio
    #import rebalance
    #import dataportfolio
    #import data
    #import dataportfolio
    #import performance
    #import plots
    #import wealthmanagementreport
    #data.portfolio(symbols,allocations,api_key,start_date)
    
    #dataportfolio.portfolio(symbols,allocations,api_key,start_date)
    #print(symbols[:3])
    #dataportfolio.benchmark(bench_symbol,start_date,api_key)
    #data.benchmark(bench_symbol,start_date,api_key)
    #rebalance.rebalance(allocations=allocations)
    #performance.portfolio()
    #performance.asset_performance()
    # # 1.) Import the module
    # import report
    #
    # # Select Functions
    #end_date = dt.date.today()

    #r = wealthmanagementreport.rep(fname=root_path + '/Reports/Daily Report ' + str(end_date) + '.pdf',fund_name="Wealth Advisory",logo_path="")
    #r.cover()
    #r.perf()
    #r.mets()
    #r.diversification()
    #
    #r.savePDF()
   # plots.correl()
   
#portfolioList= portfolio.objects.all()
#for poobj in portfolioList:
 #   generatereport.report.generateReport(poobj)
