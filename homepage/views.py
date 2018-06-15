from django.shortcuts import render
from batchprocessing.models import portfolio,portfolioAsset
from screener import fundamentalData
import numpy as np
# Create your views here.


def actualvstargetallocation(request):
    return render(request,"actualvstargetallocation.html")

def allocations(request):
    return render(request,"allocations.html")

def positions(request):
    return render(request,"positions.html")

def summary(request):
    portfolioAssetList=portfolioAsset.objects.all()
    totalcost= 0
    for asset in portfolioAssetList:
        totalcost = totalcost + asset.TotalAsset
    return render(request,"summary.html", {"portfolioList":portfolioAssetList,"totalcost":totalcost})

def homepage(request):
    portfolioAssetList=portfolioAsset.objects.all()
    totalcost= 0
    for asset in portfolioAssetList:
        totalcost = totalcost + asset.TotalAsset
    return render(request,"homepage.html", {"portfolioList":portfolioAssetList,"totalcost":totalcost})

def news(request):
    return render(request,"news.html")

