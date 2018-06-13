from django.shortcuts import render
from .models import *
from .aforms import *
from django.http import *
from batchprocessing import *
from batchprocessing.models import nifty_50_companies
from datetime import datetime as datetime

def strategy(request):
    if request.method == 'POST':
        print("#########Inside POST#############3")
        form = strategy_form(request.POST)
        company = form['companyName'].value();
        backdate = form['backdate'].value();
        print(backdate)
        if form.is_valid():
            #form.save()
           render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":backdate})
        
    else:
        form= strategy_form()
        print("inside form")
    return render(request,"stratergyOption.html",{"strategyform":form})
