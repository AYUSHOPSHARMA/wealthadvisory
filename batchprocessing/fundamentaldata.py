# -*- coding: utf-8 -*-

from batchprocessing.models import nifty_500_companies_fundamental_data
from batchprocessing.models import nifty_200_companies_fundamental_data
from batchprocessing.models import nifty_100_companies_fundamental_data
from batchprocessing.models import nifty_50_companies_fundamental_data
import datetime

class FundamentalData:
    
    def __init__(request,self,ticker):
        self.Ticker= ticker
    
    Ticker= "NA"
    CompanyName= "NA"
    Industry= "NA"
    Market_Cap= "NA"
    Enterprise_Value= "NA"
    Trailing_P_E= "NA"
    Forward_P_E= "NA"
    PEG_Ratio= "NA"
    Price_Sales= "NA"
    Price_Book= "NA"
    Enterprise_Value_Revenue= "NA"
    Enterprise_Value_EBITDA= "NA"
    Fiscal_Year_Ends= "NA"
    Most_Recent_Quarter= "NA"
    Profit_Margin= "NA"
    Operating_Margin= "NA"
    Return_on_Assets= "NA"
    Return_on_Equity= "NA"
    Revenue= "NA"
    Revenue_Per_Share= "NA"
    Quarterly_Revenue_Growth= "NA"
    Gross_Profit= "NA"
    EBITDA= "NA"
    Net_Income_Avi_to_Common= "NA"
    Diluted_EPS= "NA"
    Quarterly_Earnings_Growth= "NA"
    Total_Cash= "NA"
    Total_Cash_Per_Share= "NA"
    Total_Debt= "NA"
    Total_Debt_Equity= "NA"
    Current_Ratio= "NA"
    Book_Value_Per_Share= "NA"
    Operating_Cash_Flow= "NA"
    Levered_Free_Cash_Flow= "NA"
    Beta= "NA"
    Week_52_Change= "NA"
    SP500_52_Week_Change= "NA"
    Week_52_High= "NA"
    Week_52_Low= "NA"
    Day_50_Moving_Average= "NA"
    Day_200_Moving_Average= "NA"
    Avg_Vol_3_month= "NA"
    Avg_Vol_10_day= "NA"
    Shares_Outstanding= "NA"
    Float= "NA"
    Held_by_Insiders= "NA"
    Held_by_Institutions= "NA"
    Shares_Short= "NA"
    Short_Ratio= "NA"
    Short_of_Float= "NA"
    Shares_Short_prior_month= "NA"
    Forward_Annual_Dividend_Rate= "NA"
    Forward_Annual_Dividend_Yield= "NA"
    Trailing_Annual_Dividend_Rate= "NA"
    Trailing_Annual_Dividend_Yield= "NA"
    Year_5_Average_Dividend_Yield= "NA"
    Payout_Ratio= "NA"
    Dividend_Date= "NA"
    Ex_Dividend_Date= "NA"
    Last_Split_Factor_new_per_old= "NA"
    Last_Split_Date= "NA"

    def setTicker(self,ticker):
        self.Ticker= ticker
    
    def setCompanyName(self,companyname):
        self.CompanyName= companyname
    
    def setIndustry(self,industry):
        self.Industry= industry
        
    def setvalues(self,keystatiscs,value):
        if keystatiscs.strip()== "Market Cap":
            print("Market CAP Value for "+keystatiscs+" : Value "+ value)
            self.Market_Cap=value
        if keystatiscs.strip()== "Trailing P/E":
            self.Trailing_P_E=value
        if keystatiscs.strip()== "Forward P/E":
            self.Forward_P_E=value
        if keystatiscs.strip()== "PEG Ratio":
            self.PEG_Ratio=value
        if keystatiscs.strip()== "Price/Sales":
            self.Price_Sales=value
        if keystatiscs.strip()== "Price/Book":
            self.Price_Book=value
        if keystatiscs.strip()== "Enterprise Value/Revenue":
            self.Enterprise_Value_Revenue=value
        if keystatiscs.strip()== "Enterprise Value/EBITDA":
            self.Enterprise_Value_EBITDA=value
        if keystatiscs.strip()== "Fiscal Year Ends":
            self.Fiscal_Year_Ends=value
        if keystatiscs.strip()== "Most Recent Quarter":
            self.Most_Recent_Quarter=value
        if keystatiscs.strip()== "Profit Margin":
            self.Profit_Margin=value
        if keystatiscs.strip()== "Operating Margin":
            self.Operating_Margin=value
        if keystatiscs.strip()== "Return on Assets":
            self.Return_on_Assets=value
        if keystatiscs.strip()== "Return on Equity":
            self.Return_on_Equity=value
        if keystatiscs.strip()== "Revenue":
            self.Revenue=value
        if keystatiscs.strip()== "Revenue Per Share":
            self.Revenue_Per_Share=value
        if keystatiscs.strip()== "Quarterly Revenue Growth":
            self.Quarterly_Revenue_Growth=value
        if keystatiscs.strip()== "Gross Profit":
            self.Gross_Profit=value
        if keystatiscs.strip()== "EBITDA":
            self.EBITDA=value
        if keystatiscs.strip()== "Net Income Avi to Common":
            self.Net_Income_Avi_to_Common=value
        if keystatiscs.strip()== "Diluted EPS":
            self.Diluted_EPS=value
        if keystatiscs.strip()== "Quarterly Earnings Growth":
            self.Quarterly_Earnings_Growth=value
        if keystatiscs.strip()== "Total Cash":
            self.Total_Cash=value
        if keystatiscs.strip()== "Total Cash Per Share":
            self.Total_Cash_Per_Share=value
        if keystatiscs.strip()== "Total Debt":
            self.Total_Debt=value
        if keystatiscs.strip()== "Total Debt/Equity":
            self.Total_Debt_Equity=value
        if keystatiscs.strip()== "Current Ratio":
            self.Current_Ratio=value
        if keystatiscs.strip()== "Book Value Per Share":
            self.Book_Value_Per_Share=value
        if keystatiscs.strip()== "Operating Cash Flow":
            self.Operating_Cash_Flow=value
        if keystatiscs.strip()== "Levered Free Cash Flow":
            self.Levered_Free_Cash_Flow=value
        if keystatiscs.strip()== "Beta":
            self.Beta=value
        if keystatiscs.strip()== "52-Week Change":
            self.Week_52_Change=value
        if keystatiscs.strip()== "S&P500 52-Week Change":
            self.SP500_52_Week_Change=value
        if keystatiscs.strip()== "52 Week High":
            self.Week_52_High=value
        if keystatiscs.strip()== "52 Week Low":
            self.Week_52_Low=value
        if keystatiscs.strip()== "50-Day Moving Average":
            self.Day_50_Moving_Average=value
        if keystatiscs.strip()== "200-Day Moving Average":
            self.Day_200_Moving_Average=value
        if keystatiscs.strip()== "Avg Vol (3 month)":
            self.Avg_Vol_3_month=value
        if keystatiscs.strip()=="Avg Vol (10 day)":
            self.Avg_Vol_10_day=value
        if keystatiscs.strip()== "Shares Outstanding":
            self.Shares_Outstanding=value
        if keystatiscs.strip()== "Float":
            self.Float=value
        if keystatiscs.strip()== "% Held by Insiders":
            self.Held_by_Insiders=value
        if keystatiscs.strip()== "% Held by Institutions":
            self.Held_by_Institutions=value
        if keystatiscs.strip()== "Shares Short":
            self.Shares_Short=value
        if keystatiscs.strip()== "Short Ratio":
            self.Short_Ratio=value
        if keystatiscs.strip()== "Short % of Float":
            self.Short_of_Float=value
        if keystatiscs.strip()== "Shares Short (prior month)":
            self.Shares_Short_prior_month=value
        if keystatiscs.strip()== "Forward Annual Dividend Rate":
            self.Forward_Annual_Dividend_Rate=value
        if keystatiscs.strip()== "Forward Annual Dividend Yield":
            self.Forward_Annual_Dividend_Yield=value
        if keystatiscs.strip()== "Trailing Annual Dividend Yield":
            self.Trailing_Annual_Dividend_Yield=value
        if keystatiscs.strip()== "Trailing Annual Dividend Yield":
            self.Trailing_Annual_Dividend_Rate=value
        if keystatiscs.strip()== "5 Year Average Dividend Yield":
            self.Year_5_Average_Dividend_Yield=value
        if keystatiscs.strip()== "Ex-Dividend Date":
            self.Ex_Dividend_Date=value
        if keystatiscs.strip()== "Payout Ratio":
            self.Payout_Ratio=value
        if keystatiscs.strip()== "Dividend Date":
            self.Dividend_Date=value
        if keystatiscs.strip()== "Last Split Factor (new per old)":
            self.Last_Split_Factor_new_per_old=value
        if keystatiscs.strip()== "Last Split Date":
            self.Last_Split_Date=value
        print("#################VALUE SET##################")
              
              
    def saveFundamentalData(self,typeDb):
        print("################### OBJECT IS NONE ###################")
        now = datetime.datetime.now()
        if(typeDb=="nifty500"):
            companies_fundamental_data_obj=nifty_500_companies_fundamental_data()
        elif(typeDb=="nifty200"):
            companies_fundamental_data_obj=nifty_200_companies_fundamental_data()
        elif(typeDb=="nifty100"):
             companies_fundamental_data_obj=nifty_100_companies_fundamental_data()
        elif(typeDb=="nifty50"):
                companies_fundamental_data_obj=nifty_50_companies_fundamental_data()
        companies_fundamental_data_obj.Date = now
        companies_fundamental_data_obj.Ticker=self.Ticker
        companies_fundamental_data_obj.Industry=self.Industry
        companies_fundamental_data_obj.Company_Name=self.CompanyName
        companies_fundamental_data_obj.Market_Cap=self.Market_Cap
        companies_fundamental_data_obj.Enterprise_Value=self.Enterprise_Value
        companies_fundamental_data_obj.Trailing_P_E=self.Trailing_P_E
        companies_fundamental_data_obj.Forward_P_E=self.Forward_P_E
        companies_fundamental_data_obj.PEG_Ratio=self.PEG_Ratio
        companies_fundamental_data_obj.Price_Sales=self.Price_Sales
        companies_fundamental_data_obj.Price_Book=self.Price_Book
        companies_fundamental_data_obj.Enterprise_Value_Revenue=self.Enterprise_Value_Revenue
        companies_fundamental_data_obj.Enterprise_Value_EBITDA=self.Enterprise_Value_EBITDA
        companies_fundamental_data_obj.Fiscal_Year_Ends=self.Fiscal_Year_Ends
        companies_fundamental_data_obj.Most_Recent_Quarter=self.Most_Recent_Quarter
        companies_fundamental_data_obj.Profit_Margin=self.Profit_Margin
        companies_fundamental_data_obj.Operating_Margin=self.Operating_Margin
        companies_fundamental_data_obj.Return_on_Assets=self.Return_on_Assets
        companies_fundamental_data_obj.Return_on_Equity=self.Return_on_Equity
        companies_fundamental_data_obj.Revenue=self.Revenue
        companies_fundamental_data_obj.Revenue_Per_Share=self.Revenue_Per_Share
        companies_fundamental_data_obj.Quarterly_Revenue_Growth=self.Quarterly_Revenue_Growth
        companies_fundamental_data_obj.Gross_Profit=self.Gross_Profit
        companies_fundamental_data_obj.EBITDA=self.EBITDA
        companies_fundamental_data_obj.Net_Income_Avi_to_Common=self.Net_Income_Avi_to_Common
        companies_fundamental_data_obj.Diluted_EPS=self.Diluted_EPS
        companies_fundamental_data_obj.Quarterly_Earnings_Growth=self.Quarterly_Earnings_Growth
        companies_fundamental_data_obj.Total_Cash=self.Total_Cash
        companies_fundamental_data_obj.Total_Cash_Per_Share=self.Total_Cash_Per_Share
        companies_fundamental_data_obj.Total_Debt=self.Total_Debt
        companies_fundamental_data_obj.Total_Debt_Equity=self.Total_Debt_Equity
        companies_fundamental_data_obj.Current_Ratio=self.Current_Ratio
        companies_fundamental_data_obj.Book_Value_Per_Share=self.Book_Value_Per_Share
        companies_fundamental_data_obj.Operating_Cash_Flow=self.Operating_Cash_Flow
        companies_fundamental_data_obj.Levered_Free_Cash_Flow=self.Levered_Free_Cash_Flow
        companies_fundamental_data_obj.Beta=self.Beta
        companies_fundamental_data_obj.Week_52_Change=self.Week_52_Change
        companies_fundamental_data_obj.SP500_52_Week_Change=self.SP500_52_Week_Change
        companies_fundamental_data_obj.Week_52_High=self.Week_52_High
        companies_fundamental_data_obj.Week_52_Low=self.Week_52_Low
        companies_fundamental_data_obj.Day_50_Moving_Average=self.Day_50_Moving_Average
        companies_fundamental_data_obj.Day_200_Moving_Average=self.Day_200_Moving_Average
        companies_fundamental_data_obj.Avg_Vol_3_month=self.Avg_Vol_3_month
        companies_fundamental_data_obj.Avg_Vol_10_day=self.Avg_Vol_10_day
        companies_fundamental_data_obj.Shares_Outstanding=self.Shares_Outstanding
        companies_fundamental_data_obj.Float=self.Float
        companies_fundamental_data_obj.Held_by_Insiders=self.Held_by_Insiders
        companies_fundamental_data_obj.Held_by_Institutions=self.Held_by_Institutions
        companies_fundamental_data_obj.Shares_Short=self.Shares_Short
        companies_fundamental_data_obj.Short_Ratio=self.Short_Ratio
        companies_fundamental_data_obj.Short_of_Float=self.Short_of_Float
        companies_fundamental_data_obj.Shares_Short_prior_month=self.Shares_Short_prior_month
        companies_fundamental_data_obj.Forward_Annual_Dividend_Rate=self.Forward_Annual_Dividend_Rate
        companies_fundamental_data_obj.Forward_Annual_Dividend_Yield=self.Forward_Annual_Dividend_Yield
        companies_fundamental_data_obj.Trailing_Annual_Dividend_Yield=self.Trailing_Annual_Dividend_Yield
        companies_fundamental_data_obj.Trailing_Annual_Dividend_Rate=self.Trailing_Annual_Dividend_Rate
        companies_fundamental_data_obj.Year_5_Average_Dividend_Yield=self.Year_5_Average_Dividend_Yield
        companies_fundamental_data_obj.Payout_Ratio=self.Payout_Ratio
        companies_fundamental_data_obj.Dividend_Date=self.Dividend_Date
        companies_fundamental_data_obj.Ex_Dividend_Date=self.Ex_Dividend_Date
        companies_fundamental_data_obj.Last_Split_Factor_new_per_old=self.Last_Split_Factor_new_per_old
        companies_fundamental_data_obj.Last_Split_Date=self.Last_Split_Date
        print("################ SEVING VALUE###############")
        print("################ SAVING #########################")
        companies_fundamental_data_obj.save()
            ##companies_fundamental_data_obj.update()
        print("################ VALUE SAVED#########################")