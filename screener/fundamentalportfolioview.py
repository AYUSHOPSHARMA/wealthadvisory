from django.shortcuts import render
from screener.FundamentalPortfolioForm.models import *
from screener.models import *
from screener.FundamentalPortfolioForm.forms import *
from batchprocessing.models import nifty_500_companies_fundamental_data
from batchprocessing.models import nifty_200_companies_fundamental_data
from batchprocessing.models import nifty_100_companies_fundamental_data
from batchprocessing.models import nifty_50_companies_fundamental_data
from django.http import *
from batchprocessing import *
from mongoengine import Q

def fundamentalportfolio(request):
    print("READING FORM")
    if request.method == 'POST':
       print("########POST METHODDD###########")
       form = fundamental_form(request.POST)
       print(form['companyType'].value())
       print(form['Trailing_P_E'].value())
       print(form['Forward_P_E'].value())
       print(form['PEG'].value())
       print(form['PS'].value())
       print(form['PB'].value())
       print(form['Price_Cash'].value())
       if form.is_valid():
           if form['companyType'].value() == "nifty50":
               n50=nifty_50_companies_fundamental_data
               print("######### N50##########")
               print(n50)
               result=filterFormData(form,n50)
           elif form['companyType'].value() == "nifty100":
               result=filterFormData(form,nifty_100_companies_fundamental_data.objects.all())
           elif form['companyType'].value() == "nifty200":
               result=filterFormData(form,nifty_200_companies_fundamental_data.objects.all())
           elif form['companyType'].value() == "nifty500":
               result=filterFormData(form,nifty_500_companies_fundamental_data.objects.all())
           print("########SAVE#########")
           ##form.save()
           print("################DATA SAVED#############")
           return render(request,"fundamentalportfolio.html",{"fundamentalportfolioform":form,"list":result})
    else:
       print("########GET METHOD###########")
       form = fundamental_form()
       print("#############################")
       if form['companyType'].value() == "nifty50":
           result=nifty_50_companies_fundamental_data.objects[0:50]
       elif form['companyType'].value() == "nifty100":
           result=nifty_100_companies_fundamental_data.objects[0:100]
       elif form['companyType'].value() == "nifty200":
           result=nifty_200_companies_fundamental_data.objects[0:200]
       elif form['companyType'].value() == "nifty500":
           result=nifty_500_companies_fundamental_data.objects[0:500]
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
        print("#######return#########")
    return resultdbobj.objects.filter(filters);

def getParsedValue(field,form):
    if field.label =="Trailing P E" :
        if form['Trailing_P_E'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                print("Returning Trailing PE LT")
                return Q(Trailing_P_E__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                print("Returning Trailing PE GT")
                return Q(Trailing_P_E__gte=value)
        else:
            return Q(Trailing_P_E__lte=1000)
    if field.label =="Forward P E" :
        if form['Forward_P_E'].value() != "Any":
            if isLE(field):
                value = comparewithValue(field)
                return Q(Forward_P_E__lte=value)
            elif isGT(field):
                value = comparewithValue(field)
                return Q(Forward_P_E__gte=value)
        else:
            return Q(Forward_P_E__lte=1000)
    else:
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

def comparewithValue(field):
    print("Field valueee#########")
    print(field.value())
    if  "_" in field.value():
        print("INSIDE IF FIND###############")
        splitedvalue=field.value().split("_")
        if is_number_tryexcept(splitedvalue[1]) == True:
            return int(splitedvalue[1])
        else:
             return 1000
    return 1000     
 

def is_number_tryexcept(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False         
           