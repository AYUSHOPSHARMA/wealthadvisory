from django.shortcuts import render
from .models import *
from .aforms import *
from django.http import *
from batchprocessing import *
from batchprocessing.models import nifty_50_companies
from datetime import datetime as datetime
from screener import strategy as strategylogic

def strategy(request):
    if request.method == 'POST':
        print("#########Inside POST#############3")
        form = strategy_form(request.POST)
        company = form['companyName'].value();
        backdate = form['backdate'].value();
        #form.full_clean
        #setattr(form,'companyName',company)
        #setattr(form,'backdate',backdate)
        print(backdate)
        print(company)
        if form.is_valid():
            smafig = strategylogic.getSMAStrategy(company,backdate)
            bbbandGraph, indicesdata=strategylogic.view_indices_chart(company,backdate)
            machineLearningGraph=strategylogic.machineLearningChart(company,backdate)
            rsiStretagyGraph=strategylogic.rsiStretagy(company,backdate)
            emaStretagyGraph=strategylogic.emaStretagy(company,backdate)
            rocStretagyGraph=strategylogic.rocStretagy(company,backdate)
            macdStretagyGraph=strategylogic.macdStretagy(company,backdate)
            soStretagyGraph=strategylogic.soStretagy(company,backdate)
            indicesdata=indicesdata.dropna(how='any')
            indicesdata.columns = ['UpperBand','MiddleBand','LowerBand','Close','Buy','Sell']
            print("##########3INDICES DATA###########3")
            print(indicesdata)      
            return render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate,"smadata":smafig,"bbbandGraph":bbbandGraph,"rsiStretagyGraph":rsiStretagyGraph,"emaStretagyGraph":emaStretagyGraph,"rocStretagyGraph":rocStretagyGraph,"macdStretagyGraph":macdStretagyGraph,"soStretagyGraph":soStretagyGraph,"machineLearningGraph":machineLearningGraph,"indicesdata":indicesdata.to_html(bold_rows=True,index=False)})
    else:
        form= strategy_form()
        print("inside form")
    return render(request,"stratergyOption.html",{"strategyform":form})
