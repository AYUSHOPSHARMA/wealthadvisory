# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import FundamentalDataForm


def _form_view(request, template_name='Screener.html', form_class=FundamentalDataForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = form_class()
    print(form)
    input = '' 
    #input +=  '{"companyType":"'+form.id_companyType  +'" ,"Trailing_P_E":"'+form.id_Trailing_P_E+'"}'
    #input +=  '"Forward_P_E":"'+screenerdatabean.Forward_P_E+'",'
    #input +=  '"PEG_Ratio" :"'+screenerdatabean.PEG_Ratio+'",'
    #input +=  '"Quarterly_Earnings_Growth":"'+screenerdatabean.Quarterly_Earnings_Growth+'",'
    #input +=  '"Price_Sales":"'+screenerdatabean.Price_Sales+'",'
    #input +=  '"Price_Book":"'+screenerdatabean.Price_Book+'",'
    #input +=  '"Total_Cash_Per_Share":"'+screenerdatabean.Total_Cash_Per_Share+'",'
    #input +=  '"Levered_Free_Cash_Flow":"'+screenerdatabean.Levered_Free_Cash_Flow+'",'
    #input +=  '"Diluted_EPS":"'+screenerdatabean.Diluted_EPS+'",'
    #input +=  '"Return_on_Assets":"'+screenerdatabean.Return_on_Assets+'",'
    #input +=  '"Return_on_Equity":"'+screenerdatabean.Return_on_Equity+'",'
    #input +=  '"Current_Ratio":"'+screenerdatabean.Current_Ratio+'",'
    #input +=  '"Short_Ratio":"'+screenerdatabean.Short_Ratio+'",'
    #input +=  '"Short_of_Float":"'+screenerdatabean.Short_of_Float+'",'
    #input +=  '"Total_Debt":"'+screenerdatabean.Total_Debt+'",'
    #input +=  '"Total_Debt_Equity":"'+screenerdatabean.Total_Debt_Equity+'",'
    #input +=  '"Profit_Margin":"'+screenerdatabean.Profit_Margin+'",'
    ##input +=  '"Operating_Margin":"'+screenerdatabean.Operating_Margin+'",'
    #input +=  '"Payout_Ratio":"'+screenerdatabean.Payout_Ratio+'",'
    #input +=  '"Held_by_Insiders":"'+screenerdatabean.Held_by_Insiders+'",'
    #input +=  '"Held_by_Institutions":"'+screenerdatabean.Held_by_Institutions+'",'
    #input +=  '"companyType":"'+screenerdatabean.companyType+'"}'
    input +=  ''
    
    print("############- JSON DATA - ##############")
    print(input)
    return render(request, template_name, {'form': form,'input':input})

def fundamentalDataHome(request):
    return _form_view(request)


def manual(request):
    return _form_view(request, template_name='manual.html')


def field(request):
    return _form_view(request, template_name='field.html')


def attrs(request):
    return _form_view(request, form_class=FundamentalDataForm)


def tweaks(request):
    return _form_view(request, template_name='tweaks.html')


def bootstrap4(request):
    return _form_view(request, template_name='bootstrap4.html')