from django.shortcuts import render
from screener.FundamentalPortfolioForm.models import *
from screener.models import *
from screener.FundamentalPortfolioForm.forms import *
from batchprocessing.models import nifty_500_fundamental_data
from batchprocessing.models import nifty_200_fundamental_data
from batchprocessing.models import nifty_100_fundamental_data
from batchprocessing.models import nifty_50_fundamental_data
from batchprocessing.models import portfolio
from batchprocessing import views as batchprocessingview
from django.http import *
from batchprocessing import *
from mongoengine import Q
from mongoengine import *

connect('wealth_management_indices')

def fundamentalportfolio(request):
    print("READING FORM")
    if request.method == 'POST':
       print("########POST METHODDD###########")
       form = fundamental_form(request.POST)
       print(form['companyType'].value())
       print(form['companyType'].value())
       print(form['Trailing_P_E'].value())
       print(form['Forward_P_E'].value())
       print(form['PEG'].value())
       print(form['PS'].value())
       print(form['PB'].value())
       print(form['Price_Cash'].value())
       if form.is_valid():
           companyType = form['companyType'].value()
           if form['companyType'].value() == "nifty50":
               n50=nifty_50_fundamental_data
               print("######### N50##########")
               print(n50)
               result=filterFormData(form,n50)
           elif form['companyType'].value() == "nifty100":
               result=filterFormData(form,nifty_100_fundamental_data)
           elif form['companyType'].value() == "nifty200":
               result=filterFormData(form,nifty_200_fundamental_data)
           elif form['companyType'].value() == "nifty500":
               result=filterFormData(form,nifty_500_fundamental_data)
           print("########SAVE#########")
           tickerList = getTicker(form,result)
           print("##############submitvalue#############")
           if request.POST.get("submit_button"):
               Portfolio_Name = request.POST.get("Portfolio_Name")
               print("############Portfolio_Name#######")
               print(Portfolio_Name)      
               batchprocessingview.savePortfolio(tickerList,Portfolio_Name,companyType)
           ##form.save()
           print("################DATA SAVED#############")
           return render(request,"fundamentalportfolio.html",{"fundamentalportfolioform":form,"list":result})
    else:
       print("########GET METHOD###########")
       form = fundamental_form()
       print("#############################")
       if form['companyType'].value() == "nifty50":
           result=nifty_50_fundamental_data.objects[0:50]
       elif form['companyType'].value() == "nifty100":
           result=nifty_100_fundamental_data.objects[0:100]
       elif form['companyType'].value() == "nifty200":
           result=nifty_200_fundamental_data.objects[0:200]
       elif form['companyType'].value() == "nifty500":
           result=nifty_500_fundamental_data.objects[0:500]
       print("inside form")
       return render(request,"fundamentalportfolio.html",{"fundamentalportfolioform":form,"list":result})

def filterFormData(form,resultdbobj):
    print("inside filter#################")
    print(resultdbobj)
    return parseValue(form,resultdbobj)

def parseValue(form,resultdbobj):
    filters = None
    for field in form:
        print(field.label)
        if filters is None:
            print("inside first filter")
            ob= getParsedValue(field,form)
            if ob is not None:
                filters = getParsedValue(field,form)
        else:
            print("inside second filter")
            ob= getParsedValue(field,form)
            if ob is not None:
                filters= filters & getParsedValue(field,form)
    print("#######retur FILTER #########")
    print(filters)
    mylist = resultdbobj.objects.filter(filters);
    return mylist;

def getParsedValue(field,form):
    print("### DEBT VALUE##")
    print(form['Debt_Equity'].value())
    if field.label =="Trailing P E" :
        if form['Trailing_P_E'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                print("Returning Trailing PE LT")
                return Q(Trailing_P_E__lte=int(value))
            elif isGT(field):
                value = comparewithValue(field)
                print("Returning Trailing PE GT")
                return Q(Trailing_P_E__gte=value)
    elif field.label =="Forward P E" :
        if form['Forward_P_E'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Forward_P_E__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Forward_P_E__gte=value)
    elif field.label =="Beta" :
        if form['Beta'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Beta__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Beta__gte=value)
    elif field.label =="PEG" :
        if form['PEG'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(PEG_Ratio__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(PEG_Ratio__gte=value)
    elif field.label =="P/S" :
        if form['PS'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Price_Sales__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Price_Sales__gte=value)
    elif field.label =="P/B" :
        if form['PB'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Price_Book__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Price_Book__gte=value)
    elif field.label =="Price/Cash" :
        if form['Price_Free_Cash_Flow'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Total_Cash_Per_Share__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Total_Cash_Per_Share__gte=value)
    elif field.label =="EPS growth this year" :
        if form['EPS_growth_this_year'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Enterprise_Value_Revenue__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Enterprise_Value_Revenue__gte=value)
    elif field.label =="Return on Assets" :
        if form['Return_on_Assets'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Return_on_Assets__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Return_on_Assets__gte=value)
    elif field.label =="Return on Equity" :
        if form['Return_on_Equity'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Return_on_Equity__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Return_on_Equity__gte=value)
    elif field.label =="Current Ratio" :
        if form['Current_Ratio'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Current_Ratio__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Current_Ratio__gte=value)
    elif field.label =="Quick Ratio" :
        if form['Quick_Ratio'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Short_Ratio__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Short_Ratio__gte=value)
    elif field.label =="Lt Debt Equity" :
        if form['Lt_Debt_Equity'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Total_Debt_Equity__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Total_Debt_Equity__gte=value)
    elif field.label =="Debt Equity" :
        if form['Debt_Equity'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Total_Debt__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Total_Debt__gte=value)
            elif isEQ(field):
                print("#### DEBT EQ")
                value = comparewithValue(field)
                print(value)
                return Q(Total_Debt=value)
    elif field.label =="Gross Margin" :
        if form['Gross_Margin'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Gross_Profit__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Gross_Profit__gte=value)
    elif field.label =="Net Profit Margin" :
        if form['Net_Profit_Margin'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Profit_Margin__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Profit_Margin__gte=value)
    elif field.label =="Payout Ratio" :
        if form['Payout_Ratio'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Payout_Ratio__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Payout_Ratio__gte=value)
    elif field.label =="Insider Ownership" :
        if form['Insider_Ownership'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Held_by_Insiders__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Held_by_Insiders__gte=value)
    elif field.label =="Institutional Ownership" :
        if form['Institutional_Ownership'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Held_by_Institutions__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Held_by_Institutions__gte=value)
    else:
        print("############NO CNDITION SATISFIED##########################")
        print(field.label)      
        return None
              
def isLE(field):
    print("###########CHECKING LT##########")
    if  "lt_" in field.value():
        return True
    else:
        return False

def isGT(field):
    print("###########CHECKING GT##########")
    if "gt_" in field.value():
        return True;
    else:
        return False
def isEQ(field):
    print("###########CHECKING GT##########")
    if "eq_" in field.value():
        return True;
    else:
        return False

def comparewithValue(field):
    print("Field valueee#########")
    print(field.value())
    if  "_" in field.value():
        print("INSIDE IF FIND###############")
        splitedvalue=field.value().split("_")
        if is_number_tryexcept(splitedvalue[1]) == True:
            return float(splitedvalue[1])
        else:
             return float(1000)
    return float(1000)     
 

def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False     

def getTicker(form,result):
    print("In Ticker Method#########")
    tickerList=[]
    for element in result:
        tickerList.append(element.Ticker)
    print(tickerList)
    print(str(tickerList))
    return str(tickerList)
    

