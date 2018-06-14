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
        print(backdate)
        if form.is_valid():
            smafig = strategylogic.getSMAStrategy(request,company,backdate)
            bbbandGraph=strategylogic.view_indices_chart(request,company,backdate)
            machineLearningGraph=strategylogic.machineLearningChart(request,company,backdate)
            rsiStretagyGraph=strategylogic.rsiStretagy(request,company,backdate)
            emaStretagyGraph=strategylogic.emaStretagy(request,company,backdate)
            rocStretagyGraph=strategylogic.rocStretagy(request,company,backdate)
            macdStretagyGraph=strategylogic.macdStretagy(request,company,backdate)
            soStretagyGraph=strategylogic.soStretagy(request,company,backdate)
            return render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate,"smadata":smafig,"bbbandGraph":bbbandGraph,"rsiStretagyGraph":rsiStretagyGraph,"emaStretagyGraph":emaStretagyGraph,"rocStretagyGraph":rocStretagyGraph,"macdStretagyGraph":macdStretagyGraph,"soStretagyGraph":soStretagyGraph,"machineLearningGraph":machineLearningGraph})
    else:
        form= strategy_form()
        print("inside form")
    return render(request,"stratergyOption.html",{"strategyform":form})
