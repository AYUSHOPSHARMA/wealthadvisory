from django.shortcuts import render
from .models import *
from .aforms import *
from django.http import *
from batchprocessing import *
from batchprocessing.models import nifty_50_companies
from datetime import datetime as datetime
from screener import strategy as strategylogic
from batchprocessing.models import mutualfund_company as mfc
from batchprocessing.models import mutualfund as mf
from batchprocessing.models import scheme

import numpy as np
import pandas as pd
import talib
import os
from pylab import plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

def mutualfund(request):
    if request.method == 'POST':
        print("#########Inside POST#############3")
        form = mutualfund_form(request.POST)
        company = form['Company_Name'].value();
        schema = form['Scheme_Name'].value();
        submitvalue= request.POST.get("submitvalue")
        schema = request.POST.get("Scheme_Name")
        #form.full_clean
        #setattr(form,'companyName',company)
        #setattr(form,'backdate',backdate)
        print(company)
        print(submitvalue)
        print(schema)
        print("##### inside submit value####")    
        if submitvalue == "False" and company!=None:
           schemaarry= []
           objschema=  mfc.objects.filter(Company_Name=company).values_list("Scheme_Code","Scheme_Name")
           for schm in objschema:
                print(schm)
                sch = scheme()
                sch.Schema_Code = schm[0]
                sch.Scheme_Name = schm[1]
                schemaarry.append(sch)
           return render(request,"MutualFund.html",{"mutualfundform":form,"company":company})
        if submitvalue == "True" and schema != None:
            print("inside iffffffffff#####3")
            print(schema)
            print(company)
            companyname= "\""+company+"\""
            objmutualfund=mf.objects.filter(Scheme_Code=int(schema)).values_list('NAV','Date')
            #mutualfundfig = strategylogic.getSMAStrategy(company,backdate)
            plt.style.use('seaborn')
            data=pd.DataFrame(list(objmutualfund),columns=['NAV','Date'])
            data=data.set_index('Date')
            print("######## DATA BEFORE############")
            print(data)
            data = data.astype(float)
            data = data.fillna(data.mean())
            print("NP ARRAY##########")
            print(np.asarray(data['NAV']))
            data['SMA200'] = talib.SMA(np.asarray(data['NAV']), 50)
            data['SMA50'] = talib.SMA(np.asarray(data['NAV']), 20)
            data = data.fillna(data.mean())
            print("######## DATA AFTER SMA############")
            print(data)
            data.head()
            data.tail()
            data[['NAV', 'SMA50', 'SMA200']].plot(figsize=(10, 6));
            data['BUY'] = np.where(data['SMA50'] > data['SMA200'], 1, -1)
            data.dropna(inplace=True)
            data.head()
            data[['NAV', 'SMA50', 'SMA200', 'BUY']].plot(figsize=(10, 6), secondary_y='BUY');
            plt.title(company+" Mutual Fund")
            imgsrc= root_path + "/Figures/"+schema+"_mutualfund.png"
            plt.savefig(imgsrc)
            imgsrc = "/static/Portfolio_Tracker/Figures/"+schema+"_mutualfund.png"
            return render(request,"MutualFund.html",{"mutualfundform":form,"company":company,"objmutualfund":objmutualfund, "imgsrc":imgsrc})
    else:
        form= mutualfund_form()
        print("inside form")
    return render(request,"MutualFund.html",{"mutualfundform":form})


def loadSchemeNames(request):
    company = request.GET.get('Company_Name')
    print(company)
    schemaarry= []
    objschema=  mfc.objects.filter(Company_Name=company).values_list("Scheme_Code","Scheme_Name")
    for schm in objschema:
        print(schm)
        sch = scheme()
        sch.Schema_Code = schm[0]
        sch.Scheme_Name = schm[1]
        schemaarry.append(sch)
    print("### objschema ##")
    print(objschema)
    return render(request,"MutualFundAjax.html",{"Company_Name":company,"scheme":schemaarry})

def loadSchemeDetail(request):
    company = request.GET.get('Company_Name')
    print(company)
    schemaarry= []
    objschema=  mfc.objects.filter(Company_Name=company).values_list("Scheme_Code","Scheme_Name")
    for schm in objschema:
        mfd = mutualfunddetail()
        mfd.Company_Name= company
        mfd.Schema_Code = schm[0]
        mfd.Scheme_Name = schm[1]
        schema = schm[0]
        objmutualfund=mf.objects.filter(Scheme_Code=int(schema)).values_list('NAV','Date')
        data=pd.DataFrame(list(objmutualfund),columns=['NAV','Date'])
        data=data.set_index('Date')
        print("######## DATA BEFORE############")
        print(data)
        data = data.astype(float)
        data = data.fillna(data.mean())
        print("NP ARRAY##########")
        print(np.asarray(data['NAV']))
        data['SMA200'] = talib.SMA(np.asarray(data['NAV']), 50)
        data['SMA50'] = talib.SMA(np.asarray(data['NAV']), 20)
        data = data.fillna(data.mean())
        print("######## DATA AFTER SMA############")
        print(data)
        data.head()
        data.tail()
        data[['NAV', 'SMA50', 'SMA200']].plot(figsize=(10, 6));
        data['BUY'] = np.where(data['SMA50'] > data['SMA200'], 1, -1)
        data.dropna(inplace=True)
        data.head()
        data[['NAV', 'SMA50', 'SMA200', 'BUY']].plot(figsize=(10, 6), secondary_y='BUY');
        plt.title(company+" Mutual Fund")
        imgsrc= root_path + "/Figures/"+schema+"_mutualfund.png"
        plt.savefig(imgsrc)
        imgsrc = "/static/Portfolio_Tracker/Figures/"+schema+"_mutualfund.png"
        data = data.fillna(data.mean())
        mfd.NAV = data['NAV'].mean()
        mfd.Day_50_Moving_Average = data['SMA50'].mean()
        mfd.Day_200_Moving_Average = data['SMA200'].mean()
        mfd.Buy = np.where( mfd.Day_50_Moving_Average > mfd.Day_200_Moving_Average, 1, -1)
        mfd.ImageUrl = imgsrc
        schemaarry.append(mfd)
    print("### objschema ##")
    print(objschema)
    return render(request,"MutualFundAjax.html",{"Company_Name":company,"scheme":schemaarry})
