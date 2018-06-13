# -*- coding: utf-8 -*-

from batchprocessing.models import nifty_500_fundamental_data
from batchprocessing.models import nifty_200_fundamental_data
from batchprocessing.models import nifty_100_fundamental_data
from batchprocessing.models import nifty_50_companies_fundamental_data
from batchprocessing.models import nifty_50_fundamental_data
import datetime
from decimal import Decimal

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
    Total_Debt= 0
    Total_Debt_Equity= 0
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
            companies_fundamental_data_obj=nifty_500_fundamental_data()
        elif(typeDb=="nifty200"):
            companies_fundamental_data_obj=nifty_200_fundamental_data()
        elif(typeDb=="nifty100"):
             companies_fundamental_data_obj=nifty_100_fundamental_data()
        elif(typeDb=="nifty50"):
                companies_fundamental_data_obj=nifty_50_fundamental_data()
        print("===>Saving DAta for--- ")
        print(self.Ticker)
        companies_fundamental_data_obj.Date = now
        companies_fundamental_data_obj.Ticker=self.Ticker
        companies_fundamental_data_obj.Industry=self.Industry
        companies_fundamental_data_obj.Company_Name=self.CompanyName
        if self.Market_Cap != 'NA' and self.Market_Cap != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Market_Cap)):
            companies_fundamental_data_obj.Market_Cap=text_to_num_if_require(self.Market_Cap)
        elif self.Market_Cap == 'NA' or self.Market_Cap == 'N/A':
             companies_fundamental_data_obj.Market_Cap=0
        companies_fundamental_data_obj.Enterprise_Value=self.Enterprise_Value
        if self.Trailing_P_E != 'NA' and self.Trailing_P_E != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Trailing_P_E)):
            companies_fundamental_data_obj.Trailing_P_E=text_to_num_if_require(self.Trailing_P_E)
        elif self.Trailing_P_E == 'NA' or self.Trailing_P_E == 'N/A':
             companies_fundamental_data_obj.Trailing_P_E=0
        if self.Forward_P_E != 'NA' and self.Forward_P_E != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Forward_P_E)):
            companies_fundamental_data_obj.Forward_P_E=text_to_num_if_require(self.Forward_P_E)
        elif self.Forward_P_E == 'NA' or self.Forward_P_E == 'N/A':
             companies_fundamental_data_obj.Forward_P_E=0
        if self.PEG_Ratio != 'NA' and self.PEG_Ratio != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.PEG_Ratio)):
            companies_fundamental_data_obj.PEG_Ratio=text_to_num_if_require(self.PEG_Ratio)
        elif self.PEG_Ratio == 'NA' or self.PEG_Ratio == 'N/A':
             companies_fundamental_data_obj.PEG_Ratio=0
        if self.Price_Sales != 'NA' and self.Price_Sales != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Price_Sales)):
            companies_fundamental_data_obj.Price_Sales=text_to_num_if_require(self.Price_Sales)
        elif self.Price_Sales == 'NA' or self.Price_Sales == 'N/A':
             companies_fundamental_data_obj.Price_Sales=0
        if self.Price_Book != 'NA' and self.Price_Book != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Price_Book)):
            companies_fundamental_data_obj.Price_Book=text_to_num_if_require(self.Price_Book)
        elif self.Price_Book == 'NA' or self.Price_Book == 'N/A':
             companies_fundamental_data_obj.Price_Book=0
        if self.Enterprise_Value_Revenue != 'NA' and self.Enterprise_Value_Revenue != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Enterprise_Value_Revenue)):    
            companies_fundamental_data_obj.Enterprise_Value_Revenue=text_to_num_if_require(self.Enterprise_Value_Revenue)
        elif self.Enterprise_Value_Revenue == 'NA' or self.Enterprise_Value_Revenue == 'N/A':
             companies_fundamental_data_obj.Enterprise_Value_Revenue=0
        if self.Enterprise_Value_EBITDA != 'NA' and self.Enterprise_Value_EBITDA != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Enterprise_Value_EBITDA)):
            companies_fundamental_data_obj.Enterprise_Value_EBITDA=text_to_num_if_require(self.Enterprise_Value_EBITDA)
        elif self.Enterprise_Value_EBITDA == 'NA' or self.Enterprise_Value_EBITDA == 'N/A':
             companies_fundamental_data_obj.Enterprise_Value_EBITDA=0
        if self.Fiscal_Year_Ends != 'NA' and self.Fiscal_Year_Ends != 'N/A':
            companies_fundamental_data_obj.Fiscal_Year_Ends=self.Fiscal_Year_Ends
        if self.Most_Recent_Quarter != 'NA' and self.Most_Recent_Quarter != 'N/A':    
            companies_fundamental_data_obj.Most_Recent_Quarter=self.Most_Recent_Quarter
        if self.Profit_Margin != 'NA' and self.Profit_Margin != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Profit_Margin)):
            companies_fundamental_data_obj.Profit_Margin=text_to_num_if_require(self.Profit_Margin)
        elif self.Profit_Margin == 'NA' or self.Profit_Margin == 'N/A':
             companies_fundamental_data_obj.Profit_Margin=0
        if self.Operating_Margin != 'NA' and self.Operating_Margin != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Operating_Margin)):
            companies_fundamental_data_obj.Operating_Margin=text_to_num_if_require(self.Operating_Margin)
        elif self.Operating_Margin == 'NA' or self.Operating_Margin == 'N/A':
             companies_fundamental_data_obj.Operating_Margin=0
        if self.Return_on_Assets != 'NA' and self.Return_on_Assets != 'N/A':
            companies_fundamental_data_obj.Return_on_Assets=text_to_num_if_require(self.Return_on_Assets)
        elif self.Return_on_Assets == 'NA' or self.Return_on_Assets == 'N/A':
             companies_fundamental_data_obj.Return_on_Assets=0
        if self.Return_on_Equity != 'NA' and self.Return_on_Equity != 'N/A':
            companies_fundamental_data_obj.Return_on_Equity=text_to_num_if_require(self.Return_on_Equity)
        elif self.Return_on_Equity == 'NA' or self.Return_on_Equity == 'N/A':
             companies_fundamental_data_obj.Return_on_Equity=0
        if self.Revenue != 'NA' and self.Revenue != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Revenue)):
            companies_fundamental_data_obj.Revenue=text_to_num_if_require(self.Revenue)
        elif self.Revenue == 'NA' or self.Revenue == 'N/A':
             companies_fundamental_data_obj.Revenue=0
        if self.Revenue_Per_Share != 'NA' and self.Revenue_Per_Share != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Revenue_Per_Share)):
            companies_fundamental_data_obj.Revenue_Per_Share=text_to_num_if_require(self.Revenue_Per_Share)
        elif self.Revenue_Per_Share == 'NA' or self.Revenue_Per_Share == 'N/A':
             companies_fundamental_data_obj.Revenue_Per_Share=0
        if self.Quarterly_Revenue_Growth != 'NA' and self.Quarterly_Revenue_Growth != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Quarterly_Revenue_Growth)):
            companies_fundamental_data_obj.Quarterly_Revenue_Growth=text_to_num_if_require(self.Quarterly_Revenue_Growth)
        elif self.Quarterly_Revenue_Growth == 'NA' or self.Quarterly_Revenue_Growth == 'N/A':
             companies_fundamental_data_obj.Quarterly_Revenue_Growth=0
        if self.Gross_Profit != 'NA' and self.Gross_Profit != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Gross_Profit)):
            companies_fundamental_data_obj.Gross_Profit=text_to_num_if_require(self.Gross_Profit)
        elif self.Gross_Profit == 'NA' or self.Gross_Profit == 'N/A':
             companies_fundamental_data_obj.Gross_Profit=0
        if self.EBITDA != 'NA' and self.EBITDA != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.EBITDA)):
            companies_fundamental_data_obj.EBITDA=text_to_num_if_require(self.EBITDA)
        elif self.EBITDA == 'NA' or self.EBITDA == 'N/A':
             companies_fundamental_data_obj.EBITDA=0
        if self.Net_Income_Avi_to_Common != 'NA' and self.Net_Income_Avi_to_Common != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Net_Income_Avi_to_Common)):
            companies_fundamental_data_obj.Net_Income_Avi_to_Common=text_to_num_if_require(self.Net_Income_Avi_to_Common)
        elif self.Net_Income_Avi_to_Common == 'NA' or self.Net_Income_Avi_to_Common == 'N/A':
             companies_fundamental_data_obj.Net_Income_Avi_to_Common=0
        if self.Diluted_EPS != 'NA' and self.Diluted_EPS != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Diluted_EPS)):
            companies_fundamental_data_obj.Diluted_EPS=text_to_num_if_require(self.Diluted_EPS)
        elif self.Diluted_EPS == 'NA' or self.Diluted_EPS == 'N/A':
             companies_fundamental_data_obj.Diluted_EPS=0
        if self.Quarterly_Earnings_Growth != 'NA' and self.Quarterly_Earnings_Growth != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Quarterly_Earnings_Growth)):
            companies_fundamental_data_obj.Quarterly_Earnings_Growth=text_to_num_if_require(self.Quarterly_Earnings_Growth)
        elif self.Quarterly_Earnings_Growth == 'NA' or self.Quarterly_Earnings_Growth == 'N/A':
             companies_fundamental_data_obj.Quarterly_Earnings_Growth=0
        if self.Total_Cash != 'NA' and self.Total_Cash != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Total_Cash)):
            companies_fundamental_data_obj.Total_Cash=text_to_num_if_require(self.Total_Cash)
        elif self.Total_Cash == 'NA' or self.Total_Cash == 'N/A':
             companies_fundamental_data_obj.Total_Cash=0
        if self.Total_Cash_Per_Share != 'NA' and self.Total_Cash_Per_Share != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Total_Cash_Per_Share)):
            companies_fundamental_data_obj.Total_Cash_Per_Share=text_to_num_if_require(self.Total_Cash_Per_Share)
        elif self.Total_Cash_Per_Share == 'NA' or self.Total_Cash_Per_Share == 'N/A':
             companies_fundamental_data_obj.Total_Cash_Per_Share=0
        if self.Total_Debt != 'NA' and self.Total_Debt != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Total_Debt)):
            companies_fundamental_data_obj.Total_Debt=text_to_num_if_require(self.Total_Debt)
        elif self.Total_Debt == 'NA' or self.Total_Debt == 'N/A':
             companies_fundamental_data_obj.Total_Debt=0
        if self.Total_Debt_Equity != 'NA' and self.Total_Debt_Equity != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Total_Debt_Equity)):
            companies_fundamental_data_obj.Total_Debt_Equity=text_to_num_if_require(self.Total_Debt_Equity)
        elif self.Total_Debt_Equity == 'NA' or self.Total_Debt_Equity == 'N/A':
             companies_fundamental_data_obj.Total_Debt_Equity=0
        if self.Current_Ratio != 'NA' and self.Current_Ratio != 'N/A':
            companies_fundamental_data_obj.Current_Ratio=text_to_num_if_require(self.Current_Ratio)
        elif self.Current_Ratio == 'NA' or self.Current_Ratio == 'N/A':
             companies_fundamental_data_obj.Current_Ratio=0
        if self.Book_Value_Per_Share != 'NA' and self.Book_Value_Per_Share != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Book_Value_Per_Share)):
            companies_fundamental_data_obj.Book_Value_Per_Share=text_to_num_if_require(self.Book_Value_Per_Share)
        elif self.Book_Value_Per_Share == 'NA' or self.Book_Value_Per_Share == 'N/A':
             companies_fundamental_data_obj.Book_Value_Per_Share=0
        if self.Operating_Cash_Flow != 'NA' and self.Operating_Cash_Flow != 'N/A':
            companies_fundamental_data_obj.Operating_Cash_Flow=text_to_num_if_require(self.Operating_Cash_Flow)
        elif self.Operating_Cash_Flow == 'NA' or self.Operating_Cash_Flow == 'N/A':
             companies_fundamental_data_obj.Operating_Cash_Flow=0
        if self.Levered_Free_Cash_Flow != 'NA' and self.Levered_Free_Cash_Flow != 'N/A':
            companies_fundamental_data_obj.Levered_Free_Cash_Flow=text_to_num_if_require(self.Levered_Free_Cash_Flow)
        elif self.Levered_Free_Cash_Flow == 'NA' or self.Levered_Free_Cash_Flow == 'N/A':
             companies_fundamental_data_obj.Levered_Free_Cash_Flow=0
        if self.Beta != 'NA' and self.Beta != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Beta)):
            companies_fundamental_data_obj.Beta=text_to_num_if_require(self.Beta)
        elif self.Beta == 'NA' or self.Beta == 'N/A':
             companies_fundamental_data_obj.Beta=0
        if self.Week_52_Change != 'NA' and self.Week_52_Change != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Week_52_Change)):
            companies_fundamental_data_obj.Week_52_Change=text_to_num_if_require(self.Week_52_Change)
        elif self.Week_52_Change == 'NA' or self.Week_52_Change == 'N/A':
             companies_fundamental_data_obj.Week_52_Change=0
        if self.SP500_52_Week_Change != 'NA' and self.SP500_52_Week_Change != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.SP500_52_Week_Change)):
            companies_fundamental_data_obj.SP500_52_Week_Change=text_to_num_if_require(self.SP500_52_Week_Change)
        elif self.SP500_52_Week_Change == 'NA' or self.SP500_52_Week_Change == 'N/A':
             companies_fundamental_data_obj.SP500_52_Week_Change=0
        if self.Week_52_High != 'NA' and self.Week_52_High != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Week_52_High)):
            companies_fundamental_data_obj.Week_52_High=text_to_num_if_require(self.Week_52_High)
        elif self.Week_52_High == 'NA' or self.Week_52_High == 'N/A':
             companies_fundamental_data_obj.Week_52_High=0
        if self.Week_52_Low != 'NA' and self.Week_52_Low != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Week_52_Low)):
            companies_fundamental_data_obj.Week_52_Low=text_to_num_if_require(self.Week_52_Low)
        elif self.Week_52_Low == 'NA' or self.Week_52_Low == 'N/A':
             companies_fundamental_data_obj.Week_52_Low=0
        if self.Day_50_Moving_Average != 'NA' and self.Day_50_Moving_Average != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Day_50_Moving_Average)):
            companies_fundamental_data_obj.Day_50_Moving_Average=text_to_num_if_require(self.Day_50_Moving_Average)
        elif self.Day_50_Moving_Average == 'NA' or self.Day_50_Moving_Average == 'N/A':
             companies_fundamental_data_obj.Day_50_Moving_Average=0
        if self.Day_200_Moving_Average != 'NA' and self.Day_200_Moving_Average != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Day_200_Moving_Average)):
            companies_fundamental_data_obj.Day_200_Moving_Average=text_to_num_if_require(self.Day_200_Moving_Average)
        elif self.Day_200_Moving_Average == 'NA' or self.Day_200_Moving_Average == 'N/A':
             companies_fundamental_data_obj.Day_200_Moving_Average=0
        if self.Avg_Vol_3_month != 'NA' and self.Avg_Vol_3_month != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Avg_Vol_3_month)):
            companies_fundamental_data_obj.Avg_Vol_3_month=text_to_num_if_require(self.Avg_Vol_3_month)
        elif self.Avg_Vol_3_month == 'NA' or self.Avg_Vol_3_month == 'N/A':
             companies_fundamental_data_obj.Avg_Vol_3_month=0
        if self.Avg_Vol_10_day != 'NA' and self.Avg_Vol_10_day != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Avg_Vol_10_day)):
            companies_fundamental_data_obj.Avg_Vol_10_day=text_to_num_if_require(self.Avg_Vol_10_day)
        elif self.Avg_Vol_10_day == 'NA' or self.Avg_Vol_10_day == 'N/A':
             companies_fundamental_data_obj.Avg_Vol_10_day=0
        if self.Shares_Outstanding != 'NA' and self.Shares_Outstanding != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Shares_Outstanding)):
            companies_fundamental_data_obj.Shares_Outstanding=text_to_num_if_require(self.Shares_Outstanding)
        elif self.Shares_Outstanding == 'NA' or self.Shares_Outstanding == 'N/A':
             companies_fundamental_data_obj.Shares_Outstanding=0
        if self.Float != 'NA' and self.Float != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Float)):
            print("##########3FLOAT###########33")
            print(self.Float)
            companies_fundamental_data_obj.Float=text_to_num_if_require(self.Float)
        elif self.Float == 'NA' or self.Float == 'N/A':
             companies_fundamental_data_obj.Float=0
        if self.Held_by_Insiders != 'NA' and self.Held_by_Insiders != 'N/A':
            companies_fundamental_data_obj.Held_by_Insiders=text_to_num_if_require(self.Held_by_Insiders)
        elif self.Held_by_Insiders == 'NA' or self.Held_by_Insiders == 'N/A':
             companies_fundamental_data_obj.Held_by_Insiders=0
        if self.Held_by_Institutions != 'NA' and self.Held_by_Institutions != 'N/A':
            companies_fundamental_data_obj.Held_by_Institutions=text_to_num_if_require(self.Held_by_Institutions)
        elif self.Held_by_Institutions == 'NA' or self.Held_by_Institutions == 'N/A':
             companies_fundamental_data_obj.Held_by_Institutions=0
        if self.Shares_Short != 'NA' and self.Shares_Short != 'N/A':
            companies_fundamental_data_obj.Shares_Short=text_to_num_if_require(self.Shares_Short)
        elif self.Shares_Short == 'NA' or self.Shares_Short == 'N/A':
             companies_fundamental_data_obj.Shares_Short=0
        if self.Short_Ratio != 'NA' and self.Short_Ratio != 'N/A':
            companies_fundamental_data_obj.Short_Ratio=text_to_num_if_require(self.Short_Ratio)
        elif self.Short_Ratio == 'NA' or self.Short_Ratio == 'N/A':
             companies_fundamental_data_obj.Short_Ratio=0
        if self.Short_of_Float != 'NA' and self.Short_of_Float != 'N/A':
            companies_fundamental_data_obj.Short_of_Float=text_to_num_if_require(self.Short_of_Float)
        elif self.Short_of_Float == 'NA' or self.Short_of_Float == 'N/A':
             companies_fundamental_data_obj.Short_of_Float=0
        if self.Shares_Short_prior_month != 'NA' and self.Shares_Short_prior_month != 'N/A':
            companies_fundamental_data_obj.Shares_Short_prior_month=text_to_num_if_require(self.Shares_Short_prior_month)
        elif self.Shares_Short_prior_month == 'NA' or self.Shares_Short_prior_month == 'N/A':
             companies_fundamental_data_obj.Shares_Short_prior_month=0
        if self.Forward_Annual_Dividend_Rate != 'NA' and self.Forward_Annual_Dividend_Rate != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Forward_Annual_Dividend_Rate)):
            companies_fundamental_data_obj.Forward_Annual_Dividend_Rate=text_to_num_if_require(self.Forward_Annual_Dividend_Rate)
        elif self.Forward_Annual_Dividend_Rate == 'NA' or self.Forward_Annual_Dividend_Rate == 'N/A':
             companies_fundamental_data_obj.Forward_Annual_Dividend_Rate=0
        if self.Forward_Annual_Dividend_Yield != 'NA' and self.Forward_Annual_Dividend_Yield != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Forward_Annual_Dividend_Yield)):
            companies_fundamental_data_obj.Forward_Annual_Dividend_Yield=text_to_num_if_require(self.Forward_Annual_Dividend_Yield)
        elif self.Forward_Annual_Dividend_Yield == 'NA' or self.Forward_Annual_Dividend_Yield == 'N/A':
             companies_fundamental_data_obj.Forward_Annual_Dividend_Yield=0
        if self.Trailing_Annual_Dividend_Yield != 'NA' and self.Trailing_Annual_Dividend_Yield != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Trailing_Annual_Dividend_Yield)):
            companies_fundamental_data_obj.Trailing_Annual_Dividend_Yield=text_to_num_if_require(self.Trailing_Annual_Dividend_Yield)
        elif self.Trailing_Annual_Dividend_Yield == 'NA' or self.Trailing_Annual_Dividend_Yield == 'N/A':
             companies_fundamental_data_obj.Trailing_Annual_Dividend_Yield=0
        if self.Trailing_Annual_Dividend_Rate != 'NA' and self.Trailing_Annual_Dividend_Rate != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Trailing_Annual_Dividend_Rate)):
            companies_fundamental_data_obj.Trailing_Annual_Dividend_Rate=text_to_num_if_require(self.Trailing_Annual_Dividend_Rate)
        elif self.Trailing_Annual_Dividend_Rate == 'NA' or self.Trailing_Annual_Dividend_Rate == 'N/A':
             companies_fundamental_data_obj.Trailing_Annual_Dividend_Rate=0
        if self.Year_5_Average_Dividend_Yield != 'NA' and self.Year_5_Average_Dividend_Yield != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Year_5_Average_Dividend_Yield)):
            companies_fundamental_data_obj.Year_5_Average_Dividend_Yield=text_to_num_if_require(self.Year_5_Average_Dividend_Yield)
        elif self.Year_5_Average_Dividend_Yield == 'NA' or self.Year_5_Average_Dividend_Yield == 'N/A':
             companies_fundamental_data_obj.Year_5_Average_Dividend_Yield=0
        if self.Payout_Ratio != 'NA' and self.Payout_Ratio != 'N/A' and is_number_tryexcept(text_to_num_if_require(self.Payout_Ratio)):
            companies_fundamental_data_obj.Payout_Ratio=text_to_num_if_require(self.Payout_Ratio)
        elif self.Payout_Ratio == 'NA' or self.Payout_Ratio == 'N/A':
             companies_fundamental_data_obj.Payout_Ratio=0
        if self.Dividend_Date != 'NA' and self.Dividend_Date != 'N/A':
            companies_fundamental_data_obj.Dividend_Date=self.Dividend_Date
        if self.Ex_Dividend_Date != 'NA' and self.Ex_Dividend_Date != 'N/A':
            companies_fundamental_data_obj.Ex_Dividend_Date=self.Ex_Dividend_Date
        if self.Last_Split_Factor_new_per_old != 'NA' and self.Last_Split_Factor_new_per_old != 'N/A':
           companies_fundamental_data_obj.Last_Split_Factor_new_per_old=self.Last_Split_Factor_new_per_old
        elif self.Last_Split_Factor_new_per_old != 'NA' or self.Last_Split_Factor_new_per_old != 'N/A':
             companies_fundamental_data_obj.Last_Split_Factor_new_per_old='N/A'
        if self.Last_Split_Date != 'NA' and self.Last_Split_Date != 'N/A':
            companies_fundamental_data_obj.Last_Split_Date=self.Last_Split_Date
        print("################ SEVING VALUE###############")
        print("################ SAVING #########################")
        companies_fundamental_data_obj.save()
        print('An error occured.')
            ##companies_fundamental_data_obj.update()
        print("################ VALUE SAVED#########################")


def text_to_num_if_require(text):
    print("##### inside text_to_num_if_require ")
    if(is_number_tryexcept(text)):
        return text
    d = {'K':3,'k':3,'M': 6,'B': 9,'T': 12,'m':6,'b':9,'t':12} 
    if text[-1] in d:
        num, magnitude = text[:-1], text[-1]
        print("Nummmm")
        print(num)
        if is_number_tryexcept(num):
            val = Decimal(num) * 10 ** d[magnitude]
            print(val)
            return val
    elif text[-1] == '%':
        num, magnitude = text[:-1], text[-1]
        if is_number_tryexcept(num):
            return float(num)
        else: return 0
    else:
        return text       

def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False