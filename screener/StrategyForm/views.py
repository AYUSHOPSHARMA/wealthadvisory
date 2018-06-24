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
            submitvalue= request.POST.get("submitvalue")
            print(submitvalue)
            if submitvalue == "MSARd":
                smafig = strategylogic.getSMAStrategy(company,backdate)
                return render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate,"smadata":smafig,"submitvalue":submitvalue})
            elif submitvalue == "BBSRd":
                bbbandGraph=strategylogic.view_indices_chart(company,backdate)
                return render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate,"submitvalue":submitvalue,"bbbandGraph":bbbandGraph})
            elif submitvalue == "MLSRd":
                machineLearningGraph=strategylogic.machineLearningChart(company,backdate)
                return render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate,"submitvalue":submitvalue,"machineLearningGraph":machineLearningGraph})
            elif submitvalue == "RSIRd":
                rsiStretagyGraph=strategylogic.rsiStretagy(company,backdate)
                return render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate,"submitvalue":submitvalue,"rsiStretagyGraph":rsiStretagyGraph})
            #indicesdata.columns = ['UpperBand','MiddleBand','LowerBand','Close','Buy','Sell']
            #print("##########3INDICES DATA###########3")
            #print(indicesdata)      
            #return render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate,"smadata":smafig,"bbbandGraph":bbbandGraph,"rsiStretagyGraph":rsiStretagyGraph,"emaStretagyGraph":emaStretagyGraph,"rocStretagyGraph":rocStretagyGraph,"macdStretagyGraph":macdStretagyGraph,"soStretagyGraph":soStretagyGraph,"indicesdata":indicesdata.to_html(bold_rows=True,index=False)})
    else:
        form= strategy_form()
        print("inside form")
    return render(request,"stratergyOption.html",{"strategyform":form,"submitvalue":"MSARd"})
