from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from batchprocessing import *

def fundamentalportfolio(request):
    if request.method == 'POST':
        form = fundamental_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/fundamentalportfolio/')
        
    else:
        form= fundamental_form()
        print("inside form")
    return render(request,"fundamentalportfolio.html",{"fundamentalportfolioform":form})
