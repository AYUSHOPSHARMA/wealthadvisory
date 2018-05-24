from django.shortcuts import render

# Create your views here.


def actualvstargetallocation(request):
    return render(request,"actualvstargetallocation.html")

def allocations(request):
    return render(request,"allocations.html")

def positions(request):
    return render(request,"positions.html")

def summary(request):
    return render(request,"summary.html")

