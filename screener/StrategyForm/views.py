from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from batchprocessing import *
from batchprocessing.models import nifty_500_companies
from datetime import datetime as datetime

def strategy(request):
    if request.method == 'POST':
        print("#########Inside POST#############3")
        form = strategy_form(request.POST)
        company = form['companyName'].value();
        date =request.POST.get("start_date")
        print(date)
        startdate=datetime.strptime(date, '%Y-%m-%d')
        if form.is_valid():
            #form.save()
           render(request,"stratergyOption.html",{"strategyform":form,"company":company,"date":startdate})
        
    else:
        print("#########Inside GET#############3")
        print(nifty_500_companies.objects.all().values_list('Symbol','Company_Name'))
        form= strategy_form()
        print("inside form")
    return render(request,"stratergyOption.html",{"strategyform":form})
