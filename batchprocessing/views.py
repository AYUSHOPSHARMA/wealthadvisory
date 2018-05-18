from batchprocessing.models import nifty_500_companies
from django.http import HttpResponse
import screener.views as fd 

# Create your views here.
def uploadCompany(request):
    result=nifty_500_companies.objects.all()
    print(result)
    i=0
    for companyname in result:
        cname=companyname.Company_Name
        symbol=companyname.Symbol
        print(cname)
        print(symbol)
        fundamentalData=fd.getBatchFundamentalData(symbol)
        j = 0
        while j < len(fundamentalData.columns.values):
             jsonobj= "{'ticker':"+symbol
             jsonobj += ",'keyStatistics':"+fundamentalData.columns.values[i]
             jsonobj +=",'value':"+fundamentalData.values[0][i]+"}"
             print(jsonobj)
             j+=1
        #print(fundamentalData.set_index(symbol).index.is_unique)
        i+=1
        if i>3:
            break
        
    return HttpResponse("Read All Data")