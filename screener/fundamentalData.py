import pandas as pd
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, URLError

#sp500 = pd.read_csv("S&P500.csv", header = 0)
#tickers = sp500.Symbol

tickers = ["AAPL"]


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

def getValue(allTd, keyStatistic):
    for t in allTd:
        tdValue = t.parent.find(text=re.compile(re.escape("%s" % keyStatistic)))
        if tdValue:
            #print '"'+t.get_text()+'",'
            return tdValue.findNext('td').text
            #return tdValue.parent.nextSibling.text
    return "NA"

def get_fundamental_data(ticker,statics):
    try:
        tickers = [ticker]
        result = pd.DataFrame(index = tickers, columns = statics)
        url = 'http://finance.yahoo.com/quote/'+ticker+'/key-statistics?ltr=1'
        print(url)
        resp = urlopen(url)
        soup = BeautifulSoup(resp.read(), 'html.parser')
        allTd = soup.find_all('td',attrs={'class':'Fz(s) Fw(500) Ta(end)'})
            #
        for static in statics:
            result.ix[ticker, static] = getValue(allTd, static)
    except:
        print("Error in url Opening")
        print(ticker)
        return None
    return result

def get_fundamental_data(ticker,statics):
    try:
        tickers = [ticker]
        result = pd.DataFrame(index = tickers, columns = statics)
        url = 'http://finance.yahoo.com/quote/'+ticker+'/key-statistics?ltr=1'
        print(url)
        resp = urlopen(url)
        soup = BeautifulSoup(resp.read(), 'html.parser')
        allTd = soup.find_all('td',attrs={'class':'Fz(s) Fw(500) Ta(end)'})
            #
        for static in statics:
            result.ix[ticker, static] = getValue(allTd, static)
    except:
        print("Error in url Opening")
        print(ticker)
        return None
    return result

def get_mutualfund_code(ticker,statics,offset,count):
    try:
        tickers = [ticker]
        result = pd.DataFrame(index = tickers, columns = statics)
        url = 'https://in.finance.yahoo.com/mutualfunds/?offset='+offset+'&count='+count+''
        print(url)
        resp = urlopen(url)
        soup = BeautifulSoup(resp.read(), 'html.parser')
        allTd = soup.find_all('td',attrs={'class':'Fz(s) Fw(500) Ta(end)'})
            #
        for static in statics:
            result.ix[ticker, static] = getValue(allTd, static)
    except:
        print("Error in url Opening")
        print(ticker)
        return None
    return result

def get_balance_sheet_data(ticker,static):
    try:
        url = 'http://finance.yahoo.com/quote/'+ticker+'/balance-sheet/'
        print(url)
        resp = urlopen(url)
        soup = BeautifulSoup(resp.read(), 'html.parser')
        allTd = soup.find_all('td',attrs={'class':'Fw(b) Fz(s) Ta(end) Pb(20px)'})
        asset=allTd[0].text
        asset = asset.replace(",", "")
        print(asset)
        if ('-' in allTd[0].text)  or not is_number_tryexcept(asset):
            asset=allTd[1].text
        if ('-' in asset)  or not is_number_tryexcept(asset):
            asset=allTd[2].text
        elif ('-' in asset):
            asset=1000000
        print("####ASSET#########")
        return float(asset)
    except:
        print("Error in url Opening")
        print(ticker)
        return None
    return result

def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False