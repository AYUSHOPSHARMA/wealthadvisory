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
           result=filterFormData(form)
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

def filterFormData(form):
    if form.has_changed:
        if form['companyType'].value() == "nifty50":
            db=nifty_50_companies_fundamental_data.objects[0:50]
            return parseValue(form)
        elif form['companyType'].value() == "nifty100":
            db=nifty_100_companies_fundamental_data.objects[0:100]
        elif form['companyType'].value() == "nifty200":
            db=nifty_200_companies_fundamental_data.objects[0:200]
        elif form['companyType'].value() == "nifty500":
            db=nifty_500_companies_fundamental_data.objects[0:500]
        print(db)
    return db

def parseValue(form):
        return getParsedValue(form['Trailing_P_E'],form)
    

def getParsedValue(field,form):
    if field == form['Trailing_P_E'] :
        print("inside parse######")
        db=nifty_50_companies_fundamental_data.objects.filter(Trailing_P_E__lt=15)
        print("######### Value Found")
        return db
    else:
        print("######### Value Not Found")
           