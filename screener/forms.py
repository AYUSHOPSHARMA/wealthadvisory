from django import forms


class FundamentalDataForm(forms.Form):
    companyType= forms.CharField(max_length=100)
    Trailing_P_E=forms.CharField(max_length=100)
   # Forward_P_E=forms.CharField(max_length=100)
   # PEG_Ratio=forms.CharField(max_length=100)
   # Quarterly_Earnings_Growth=forms.CharField(max_length=100)
   # Price_Sales=forms.CharField(max_length=100)
   # Price_Book=forms.CharField(max_length=100)
   # Total_Cash_Per_Share=forms.CharField(max_length=100)
   # Levered_Free_Cash_Flow=forms.CharField(max_length=100)
   # Diluted_EPS=forms.CharField(max_length=100)
   # Quarterly_Earnings_Growth=forms.CharField(max_length=100)
   # Return_on_Assets=forms.CharField(max_length=100)
    #Return_on_Equity=forms.CharField(max_length=100)
    #Current_Ratio=forms.CharField(max_length=100)
    #Short_Ratio=forms.CharField(max_length=100)
    ##Short_of_Float=forms.CharField(max_length=100)
    #Total_Debt=forms.CharField(max_length=100)
    #Total_Debt_Equity=forms.CharField(max_length=100)
    #Profit_Margin=forms.CharField(max_length=100)
    #Operating_Margin=forms.CharField(max_length=100)
    #Gross_Profit=forms.CharField(max_length=100)
    #Payout_Ratio=forms.CharField(max_length=100)
    #Held_by_Insiders=forms.CharField(max_length=100)
    #Held_by_Institutions=forms.CharField(max_length=100)
    #companyType=forms.CharField(max_length=100)
    #Gross_Profit=forms.CharField(max_length=100)
    #Gross_Profit=forms.CharField(max_length=100)
    #Gross_Profit=forms.CharField(max_length=100)
    #Gross_Profit=forms.CharField(max_length=100)
   

    def clean(self):
        cleaned_data = super(FundamentalDataForm, self).clean()
        Trailing_P_E = cleaned_data.get('Trailing_P_E')
        if not Trailing_P_E:
            raise forms.ValidationError('You have to select something!')
        companyType = cleaned_data.get('companyType')
        if not companyType:
            raise forms.ValidationError('You have to select something!')

