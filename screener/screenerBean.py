import json
     
class ScreenerData:
    
    def __init__(request,self,companyType):
             self.companyType= companyType

    companyType= "nse500"
    Trailing_P_E="Any"
    Forward_P_E="Any"
    PEG_Ratio="Any"
    Quarterly_Earnings_Growth="Any"
    Price_Sales="Any"
    Price_Book="Any"
    Total_Cash_Per_Share="Any"
    Levered_Free_Cash_Flow="Any"
    Diluted_EPS="Any"
    Quarterly_Earnings_Growth="Any"
    Return_on_Assets="Any"
    Return_on_Equity="Any"
    Current_Ratio="Any"
    Short_Ratio="Any"
    Short_of_Float="Any"
    Total_Debt="Any"
    Total_Debt_Equity="Any"
    Profit_Margin="Any"
    Operating_Margin="Any"
    Gross_Profit="Any"
    Payout_Ratio="Any"
    Held_by_Insiders="Any"
    Held_by_Institutions="Any"
    companyType="Any"
    Gross_Profit="Any"
    Gross_Profit="Any"
    Gross_Profit="Any"
    Gross_Profit="Any"
    
    def setTrailing_P_E(self,var):
        self.Trailing_P_E =var

    @property
    def getTrailing_P_E(self):
        var= self.Trailing_P_E
        return var
