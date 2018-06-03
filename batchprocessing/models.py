from django.db import models

# Create your models here.


from mongoengine import *
import datetime
 
connect('wealth_management_indices')

class nifty_500_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)

class nifty_200_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)

class nifty_100_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)

class nifty_50_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)

class nifty_500_companies_fundamental_data(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Market_Cap= StringField(max_length=100,required=True)
        Enterprise_Value= StringField(max_length=100,required=True)
        Trailing_P_E= StringField(required=True)
        Forward_P_E= StringField(required=True)
        PEG_Ratio= StringField(required=True)
        Price_Sales= StringField(required=True)
        Price_Book= StringField(required=True)
        Enterprise_Value_Revenue= StringField(required=True)
        Enterprise_Value_EBITDA= StringField(required=True)
        Fiscal_Year_Ends= StringField(default=datetime.datetime.utcnow)
        Most_Recent_Quarter= StringField(default=datetime.datetime.utcnow)
        Profit_Margin= StringField(required=True)
        Operating_Margin= StringField(required=True)
        Return_on_Assets= StringField(required=True)
        Return_on_Equity= StringField(required=True)
        Revenue= StringField(max_length=100,required=True)
        Revenue_Per_Share= StringField(required=True)
        Quarterly_Revenue_Growth= StringField(required=True)
        Gross_Profit= StringField(max_length=100,required=True)
        EBITDA= StringField(max_length=100,required=True)
        Net_Income_Avi_to_Common= StringField(max_length=100,required=True)
        Diluted_EPS= StringField(required=True)
        Quarterly_Earnings_Growth= StringField(required=True)
        Total_Cash= StringField(max_length=100,required=True)
        Total_Cash_Per_Share= StringField(required=True)
        Total_Debt= StringField(max_length=100,required=True)
        Total_Debt_Equity= StringField(required=True)
        Current_Ratio= StringField(required=True)
        Book_Value_Per_Share= StringField(required=True)
        Operating_Cash_Flow= StringField(max_length=100,required=True)
        Levered_Free_Cash_Flow= StringField(max_length=100,required=True)
        Beta= StringField(required=True)
        Week_52_Change= StringField(required=True)
        SP500_52_Week_Change= StringField(required=True)
        Week_52_High= StringField(required=True)
        Week_52_Low= StringField(required=True)
        Day_50_Moving_Average= StringField(required=True)
        Day_200_Moving_Average= StringField(required=True)
        Avg_Vol_3_month= StringField(max_length=100,required=True)
        Avg_Vol_10_day= StringField(max_length=100,required=True)
        Shares_Outstanding= StringField(max_length=100,required=True)
        Float= StringField(max_length=100,required=True)
        Held_by_Insiders= StringField(required=True)
        Held_by_Institutions= StringField(required=True)
        Shares_Short= StringField(max_length=100,required=True)
        Short_Ratio= StringField(required=True)
        Short_of_Float= StringField(required=True)
        Shares_Short_prior_month= StringField(max_length=100,required=True)
        Forward_Annual_Dividend_Rate= StringField(required=True)
        Forward_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Rate= StringField(required=True)
        Year_5_Average_Dividend_Yield= StringField(required=True)
        Payout_Ratio= StringField(required=True)
        Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Ex_Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Last_Split_Factor_new_per_old= StringField(max_length=100,required=True)
        Last_Split_Date= StringField(default=datetime.datetime.utcnow)

class nifty_200_companies_fundamental_data(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Market_Cap= StringField(max_length=100,required=True)
        Enterprise_Value= StringField(max_length=100,required=True)
        Trailing_P_E= StringField(required=True)
        Forward_P_E= StringField(required=True)
        PEG_Ratio= StringField(required=True)
        Price_Sales= StringField(required=True)
        Price_Book= StringField(required=True)
        Enterprise_Value_Revenue= StringField(required=True)
        Enterprise_Value_EBITDA= StringField(required=True)
        Fiscal_Year_Ends= StringField(default=datetime.datetime.utcnow)
        Most_Recent_Quarter= StringField(default=datetime.datetime.utcnow)
        Profit_Margin= StringField(required=True)
        Operating_Margin= StringField(required=True)
        Return_on_Assets= StringField(required=True)
        Return_on_Equity= StringField(required=True)
        Revenue= StringField(max_length=100,required=True)
        Revenue_Per_Share= StringField(required=True)
        Quarterly_Revenue_Growth= StringField(required=True)
        Gross_Profit= StringField(max_length=100,required=True)
        EBITDA= StringField(max_length=100,required=True)
        Net_Income_Avi_to_Common= StringField(max_length=100,required=True)
        Diluted_EPS= StringField(required=True)
        Quarterly_Earnings_Growth= StringField(required=True)
        Total_Cash= StringField(max_length=100,required=True)
        Total_Cash_Per_Share= StringField(required=True)
        Total_Debt= StringField(max_length=100,required=True)
        Total_Debt_Equity= StringField(required=True)
        Current_Ratio= StringField(required=True)
        Book_Value_Per_Share= StringField(required=True)
        Operating_Cash_Flow= StringField(max_length=100,required=True)
        Levered_Free_Cash_Flow= StringField(max_length=100,required=True)
        Beta= StringField(required=True)
        Week_52_Change= StringField(required=True)
        SP500_52_Week_Change= StringField(required=True)
        Week_52_High= StringField(required=True)
        Week_52_Low= StringField(required=True)
        Day_50_Moving_Average= StringField(required=True)
        Day_200_Moving_Average= StringField(required=True)
        Avg_Vol_3_month= StringField(max_length=100,required=True)
        Avg_Vol_10_day= StringField(max_length=100,required=True)
        Shares_Outstanding= StringField(max_length=100,required=True)
        Float= StringField(max_length=100,required=True)
        Held_by_Insiders= StringField(required=True)
        Held_by_Institutions= StringField(required=True)
        Shares_Short= StringField(max_length=100,required=True)
        Short_Ratio= StringField(required=True)
        Short_of_Float= StringField(required=True)
        Shares_Short_prior_month= StringField(max_length=100,required=True)
        Forward_Annual_Dividend_Rate= StringField(required=True)
        Forward_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Rate= StringField(required=True)
        Year_5_Average_Dividend_Yield= StringField(required=True)
        Payout_Ratio= StringField(required=True)
        Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Ex_Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Last_Split_Factor_new_per_old= StringField(max_length=100,required=True)
        Last_Split_Date= StringField(default=datetime.datetime.utcnow)
        
class nifty_100_companies_fundamental_data(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Market_Cap= StringField(max_length=100,required=True)
        Enterprise_Value= StringField(max_length=100,required=True)
        Trailing_P_E= StringField(required=True)
        Forward_P_E= StringField(required=True)
        PEG_Ratio= StringField(required=True)
        Price_Sales= StringField(required=True)
        Price_Book= StringField(required=True)
        Enterprise_Value_Revenue= StringField(required=True)
        Enterprise_Value_EBITDA= StringField(required=True)
        Fiscal_Year_Ends= StringField(default=datetime.datetime.utcnow)
        Most_Recent_Quarter= StringField(default=datetime.datetime.utcnow)
        Profit_Margin= StringField(required=True)
        Operating_Margin= StringField(required=True)
        Return_on_Assets= StringField(required=True)
        Return_on_Equity= StringField(required=True)
        Revenue= StringField(max_length=100,required=True)
        Revenue_Per_Share= StringField(required=True)
        Quarterly_Revenue_Growth= StringField(required=True)
        Gross_Profit= StringField(max_length=100,required=True)
        EBITDA= StringField(max_length=100,required=True)
        Net_Income_Avi_to_Common= StringField(max_length=100,required=True)
        Diluted_EPS= StringField(required=True)
        Quarterly_Earnings_Growth= StringField(required=True)
        Total_Cash= StringField(max_length=100,required=True)
        Total_Cash_Per_Share= StringField(required=True)
        Total_Debt= StringField(max_length=100,required=True)
        Total_Debt_Equity= StringField(required=True)
        Current_Ratio= StringField(required=True)
        Book_Value_Per_Share= StringField(required=True)
        Operating_Cash_Flow= StringField(max_length=100,required=True)
        Levered_Free_Cash_Flow= StringField(max_length=100,required=True)
        Beta= StringField(required=True)
        Week_52_Change= StringField(required=True)
        SP500_52_Week_Change= StringField(required=True)
        Week_52_High= StringField(required=True)
        Week_52_Low= StringField(required=True)
        Day_50_Moving_Average= StringField(required=True)
        Day_200_Moving_Average= StringField(required=True)
        Avg_Vol_3_month= StringField(max_length=100,required=True)
        Avg_Vol_10_day= StringField(max_length=100,required=True)
        Shares_Outstanding= StringField(max_length=100,required=True)
        Float= StringField(max_length=100,required=True)
        Held_by_Insiders= StringField(required=True)
        Held_by_Institutions= StringField(required=True)
        Shares_Short= StringField(max_length=100,required=True)
        Short_Ratio= StringField(required=True)
        Short_of_Float= StringField(required=True)
        Shares_Short_prior_month= StringField(max_length=100,required=True)
        Forward_Annual_Dividend_Rate= StringField(required=True)
        Forward_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Rate= StringField(required=True)
        Year_5_Average_Dividend_Yield= StringField(required=True)
        Payout_Ratio= StringField(required=True)
        Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Ex_Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Last_Split_Factor_new_per_old= StringField(max_length=100,required=True)
        Last_Split_Date= StringField(default=datetime.datetime.utcnow)

class nifty_50_companies_fundamental_data(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Market_Cap= StringField(max_length=100,required=True)
        Enterprise_Value= StringField(max_length=100,required=True)
        Trailing_P_E= StringField(required=True)
        Forward_P_E= StringField(required=True)
        PEG_Ratio= StringField(required=True)
        Price_Sales= StringField(required=True)
        Price_Book= StringField(required=True)
        Enterprise_Value_Revenue= StringField(required=True)
        Enterprise_Value_EBITDA= StringField(required=True)
        Fiscal_Year_Ends= StringField(default=datetime.datetime.utcnow)
        Most_Recent_Quarter= StringField(default=datetime.datetime.utcnow)
        Profit_Margin= StringField(required=True)
        Operating_Margin= StringField(required=True)
        Return_on_Assets= StringField(required=True)
        Return_on_Equity= StringField(required=True)
        Revenue= StringField(max_length=100,required=True)
        Revenue_Per_Share= StringField(required=True)
        Quarterly_Revenue_Growth= StringField(required=True)
        Gross_Profit= StringField(max_length=100,required=True)
        EBITDA= StringField(max_length=100,required=True)
        Net_Income_Avi_to_Common= StringField(max_length=100,required=True)
        Diluted_EPS= StringField(required=True)
        Quarterly_Earnings_Growth= StringField(required=True)
        Total_Cash= StringField(max_length=100,required=True)
        Total_Cash_Per_Share= StringField(required=True)
        Total_Debt= StringField(max_length=100,required=True)
        Total_Debt_Equity= StringField(required=True)
        Current_Ratio= StringField(required=True)
        Book_Value_Per_Share= StringField(required=True)
        Operating_Cash_Flow= StringField(max_length=100,required=True)
        Levered_Free_Cash_Flow= StringField(max_length=100,required=True)
        Beta= StringField(required=True)
        Week_52_Change= StringField(required=True)
        SP500_52_Week_Change= StringField(required=True)
        Week_52_High= StringField(required=True)
        Week_52_Low= StringField(required=True)
        Day_50_Moving_Average= StringField(required=True)
        Day_200_Moving_Average= StringField(required=True)
        Avg_Vol_3_month= StringField(max_length=100,required=True)
        Avg_Vol_10_day= StringField(max_length=100,required=True)
        Shares_Outstanding= StringField(max_length=100,required=True)
        Float= StringField(max_length=100,required=True)
        Held_by_Insiders= StringField(required=True)
        Held_by_Institutions= StringField(required=True)
        Shares_Short= StringField(max_length=100,required=True)
        Short_Ratio= StringField(required=True)
        Short_of_Float= StringField(required=True)
        Shares_Short_prior_month= StringField(max_length=100,required=True)
        Forward_Annual_Dividend_Rate= StringField(required=True)
        Forward_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Yield= StringField(required=True)
        Trailing_Annual_Dividend_Rate= StringField(required=True)
        Year_5_Average_Dividend_Yield= StringField(required=True)
        Payout_Ratio= StringField(required=True)
        Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Ex_Dividend_Date= StringField(default=datetime.datetime.utcnow)
        Last_Split_Factor_new_per_old= StringField(max_length=100,required=True)
        Last_Split_Date= StringField(default=datetime.datetime.utcnow)


class nifty_50_fundamental_data(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=True)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=False)
        Market_Cap= DecimalField(max_length=100,required=False)
        Enterprise_Value= StringField(max_length=100,required=False)
        Trailing_P_E= DecimalField(required=False)
        Forward_P_E= DecimalField(required=False)
        PEG_Ratio= DecimalField(required=False)
        Price_Sales= DecimalField(required=False)
        Price_Book= DecimalField(required=False)
        Enterprise_Value_Revenue= DecimalField(required=False)
        Enterprise_Value_EBITDA= DecimalField(required=False)
        Fiscal_Year_Ends= DateTimeField(default=datetime.datetime.utcnow)
        Most_Recent_Quarter= DateTimeField(default=datetime.datetime.utcnow)
        Profit_Margin= DecimalField(required=False)
        Operating_Margin= DecimalField(required=False)
        Return_on_Assets= StringField(required=False)
        Return_on_Equity= StringField(required=False)
        Revenue= DecimalField(max_length=100,required=False)
        Revenue_Per_Share= DecimalField(required=False)
        Quarterly_Revenue_Growth= DecimalField(required=False)
        Gross_Profit= DecimalField(max_length=100,required=False)
        EBITDA= DecimalField(max_length=100,required=False)
        Net_Income_Avi_to_Common= DecimalField(max_length=100,required=False)
        Diluted_EPS= DecimalField(required=False)
        Quarterly_Earnings_Growth= DecimalField(required=False)
        Total_Cash= DecimalField(max_length=100,required=False)
        Total_Cash_Per_Share= DecimalField(required=False)
        Total_Debt= DecimalField(max_length=100,required=False)
        Total_Debt_Equity= DecimalField(required=False)
        Current_Ratio= StringField(required=False)
        Book_Value_Per_Share= DecimalField(required=False)
        Operating_Cash_Flow= StringField(max_length=100,required=False)
        Levered_Free_Cash_Flow= StringField(max_length=100,required=False)
        Beta= DecimalField(required=False)
        Week_52_Change= DecimalField(required=False)
        SP500_52_Week_Change= DecimalField(required=False)
        Week_52_High= DecimalField(required=False)
        Week_52_Low= DecimalField(required=False)
        Day_50_Moving_Average= DecimalField(required=False)
        Day_200_Moving_Average= DecimalField(required=False)
        Avg_Vol_3_month= DecimalField(max_length=100,required=False)
        Avg_Vol_10_day= DecimalField(max_length=100,required=False)
        Shares_Outstanding= DecimalField(max_length=100,required=False)
        Float= DecimalField(max_length=100,required=False)
        Held_by_Insiders= StringField(required=False)
        Held_by_Institutions= StringField(required=False)
        Shares_Short= StringField(max_length=100,required=False)
        Short_Ratio= StringField(required=False)
        Short_of_Float= StringField(required=False)
        Shares_Short_prior_month= StringField(max_length=100,required=False)
        Forward_Annual_Dividend_Rate= DecimalField(required=False)
        Forward_Annual_Dividend_Yield= DecimalField(required=False)
        Trailing_Annual_Dividend_Yield= DecimalField(required=False)
        Trailing_Annual_Dividend_Rate= DecimalField(required=False)
        Year_5_Average_Dividend_Yield= DecimalField(required=False)
        Payout_Ratio= DecimalField(required=False)
        Dividend_Date= DateTimeField(default=datetime.datetime.utcnow)
        Ex_Dividend_Date= DateTimeField(default=datetime.datetime.utcnow)
        Last_Split_Factor_new_per_old= StringField(max_length=100,required=False)
        Last_Split_Date= DateTimeField(default=datetime.datetime.utcnow)

class nift50Indices(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Open = DecimalField(max_length=100,required=True)
        High = DecimalField(max_length=100,required=True)
        Low =  DecimalField(max_length=100,required=True)
        Close =DecimalField(max_length=100,required=True)
        Adj_Close =DecimalField(required=False)
        Volume = LongField(required=False)       

class nift100Indices(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Open = DecimalField(max_length=100,required=True)
        High = DecimalField(max_length=100,required=True)
        Low =  DecimalField(max_length=100,required=True)
        Close =DecimalField(max_length=100,required=True)
        Adj_Close =DecimalField(required=False)
        Volume = LongField(required=False)

class nift200Indices(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Open = DecimalField(max_length=100,required=True)
        High = DecimalField(max_length=100,required=True)
        Low =  DecimalField(max_length=100,required=True)
        Close =DecimalField(max_length=100,required=True)
        Adj_Close =DecimalField(required=False)
        Volume = LongField(required=False)


class nift500Indices(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Ticker=  StringField(max_length=100,required=False)
        Company_Name = StringField(max_length=100,required=False)
        Industry = StringField(max_length=100,required=True)
        Open = DecimalField(max_length=100,required=True)
        High = DecimalField(max_length=100,required=True)
        Low =  DecimalField(max_length=100,required=True)
        Close =DecimalField(max_length=100,required=True)
        Adj_Close =DecimalField(required=False)
        Volume = LongField(required=False)