from django import forms
from .models import *


class fundamental_form(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(fundamental_form, self).__init__(*args, **kwargs)
        self.fields['PS'].label = "P/S"
        self.fields['PB'].label = "P/B"
        self.fields['Price_Cash'].label = "Price/Cash"
        self.fields['companyType'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Trailing_P_E'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Trailing_P_E'].widget.attrs["name"]="id_Trailing_P_E"
        self.fields['Forward_P_E'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Beta'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['PEG'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['PS'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['PB'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Price_Free_Cash_Flow'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['EPS_growth_this_year'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Return_on_Assets'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Return_on_Equity'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Current_Ratio'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Quick_Ratio'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Lt_Debt_Equity'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Debt_Equity'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Gross_Margin'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Net_Profit_Margin'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Payout_Ratio'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Insider_Ownership'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['Institutional_Ownership'].widget.attrs["onchange"]="javascript:change(this);"
        self.fields['companyType'].widget.attrs["name"]="companyType"
        self.fields['Trailing_P_E'].widget.attrs["name"]="Trailing_P_E"
        self.fields['Forward_P_E'].widget.attrs["name"]="Forward_P_E"
        self.fields['Beta'].widget.attrs["name"]="Beta"
        self.fields['PEG'].widget.attrs["name"]="PEG"
        self.fields['PS'].widget.attrs["name"]="PS"
        self.fields['PB'].widget.attrs["name"]="PB"
        self.fields['Price_Cash'].widget.attrs["name"]="Price_Cash"
        self.fields['Price_Free_Cash_Flow'].widget.attrs["name"]="Price_Free_Cash_Flow"
        self.fields['EPS_growth_this_year'].widget.attrs["name"]="EPS_growth_this_year"
        self.fields['Return_on_Assets'].widget.attrs["name"]="Return_on_Assets"
        self.fields['Return_on_Equity'].widget.attrs["name"]="Return_on_Equity"
        self.fields['Current_Ratio'].widget.attrs["name"]="Current_Ratio"
        self.fields['Quick_Ratio'].widget.attrs["name"]="Quick_Ratio"
        self.fields['Current_Ratio'].widget.attrs["name"]="Current_Ratio"
        self.fields['Lt_Debt_Equity'].widget.attrs["name"]="LT_Debt_Equity"
        self.fields['Debt_Equity'].widget.attrs["name"]="Debt_Equity"
        self.fields['Gross_Margin'].widget.attrs["name"]="Gross_Margin"
        self.fields['Net_Profit_Margin'].widget.attrs["name"]="Net_Profit_Margin"
        self.fields['Payout_Ratio'].widget.attrs["name"]="Payout_Ratio"
        self.fields['Insider_Ownership'].widget.attrs["name"]="Insider_Ownership"
        self.fields['Institutional_Ownership'].widget.attrs["name"]="Institutional_Ownership"
        self.fields['Trailing_P_E'].widget.attrs["name"]="id_Trailing_P_E"
        self.fields['companyType'].widget.attrs["style"]="width: 100px;margin-left: 45px;margin-right: -1px;"
        self.fields['Trailing_P_E'].widget.attrs["style"]="width: 100px;margin-left: 94px;margin-right: 35px;"
        self.fields['Forward_P_E'].widget.attrs["style"]="width: 100px;margin-left: 83px;"
        self.fields['Beta'].widget.attrs["style"]="width: 100px;margin-left: 107px;"
        self.fields['PEG'].widget.attrs["style"]="width: 100px;margin-left: 134px;margin-right: 35px;"
        self.fields['Price_Cash'].widget.attrs["style"]="width: 100px;margin-left: 67px;"
        self.fields['PS'].widget.attrs["style"]="width: 100px;margin-left: 138px;margin-right: 35px;"
        self.fields['PB'].widget.attrs["style"]="width: 100px;margin-left: 120px;margin-right: 34px;"
        self.fields['Price_Free_Cash_Flow'].widget.attrs["style"]="width: 100px;margin-left: 30px;margin-right: 34px;;"
        self.fields['Return_on_Assets'].widget.attrs["style"]="width: 100px;margin-left: 35px;margin-right: 34px;"
        self.fields['Return_on_Equity'].widget.attrs["style"]="width: 100px;margin-left: 31px;"
        self.fields['Current_Ratio'].widget.attrs["style"]="width: 100px;margin-left: 81px;margin-right: 34px;"
        self.fields['Quick_Ratio'].widget.attrs["style"]="width: 100px;margin-left: 89px;margin-right: 34px;"
        self.fields['Lt_Debt_Equity'].widget.attrs["style"]="width: 100px;margin-left: 56px;margin-right: 35px;"
        self.fields['Debt_Equity'].widget.attrs["style"]="width: 100px;margin-left: 62px;margin-right: 1px;"
        self.fields['Gross_Margin'].widget.attrs["style"]="width: 100px;margin-left: 81px;margin-right: 34px;"
        self.fields['EPS_growth_this_year'].widget.attrs["style"]="width: 100px;margin-left: 31px;margin-right: 35px;"
        self.fields['Net_Profit_Margin'].widget.attrs["style"]="width: 100px;margin-left: 56px;margin-right: 35px;"
        self.fields['Payout_Ratio'].widget.attrs["style"]="width: 100px;margin-left: 62px;margin-right: 35px;"
        self.fields['Insider_Ownership'].widget.attrs["style"]="width: 100px;margin-left: 22px;"
        self.fields['Institutional_Ownership'].widget.attrs["style"]="width: 100px;margin-left: 23px;"
       
        
    class Meta():
        model= fundamentalportfolio
        fields= ['companyType','Trailing_P_E','Forward_P_E','Beta','PEG','PS','PB','Price_Cash','Price_Free_Cash_Flow','EPS_growth_this_year',
        'Return_on_Assets',
        'Return_on_Equity',
        'Current_Ratio',
        'Quick_Ratio',
        'Lt_Debt_Equity',
        'Debt_Equity',
        'Gross_Margin',
        'Net_Profit_Margin',
        'Payout_Ratio',
        'Insider_Ownership',
        'Institutional_Ownership']