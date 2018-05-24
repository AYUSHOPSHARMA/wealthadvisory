from django.shortcuts import render
from batchprocessing.models import nifty_500_companies
from django.http import HttpResponse
import json
# Create your views here.

def mapswm(request):
    return render(request,"treemapwm.html")

def maps(request):
    return render(request,"treemap.html")
    
def mapsdata(request):
    print("Calling mpsdata######################")
    result=nifty_500_companies.objects.distinct(field="Industry")[0:10]
    if(len(result)>0):
        finaljsononj=""
        j=1
        for ind in result:
            print("####### First Loop####")
            jobj = "{\"name\":\""+ind+"\""
            industryStock=nifty_500_companies.objects(Industry=ind)[0:5]
            if len(industryStock)>0:
                print(len(industryStock))
                jsondataobj=",\"children\":"
                childobjj=""
                i=1
                for child in industryStock:
                    if i<len(industryStock):
                        childobjj+="{\"name\": \""+child.Company_Name+"\", \"size\": 5000},"
                    else:
                        childobjj+="{\"name\": \""+child.Company_Name+"\", \"size\": 5000}"
                    i=i+1
                if j<len(result):   
                    jsondataobj=jsondataobj+"["+childobjj+"]},"
                else:
                    jsondataobj=jsondataobj+"["+childobjj+"]}"
                j=j+1
            finaljsononj= finaljsononj+jobj + jsondataobj
        
        objk = "{\"name\": \"flare\",\"children\": [ "+finaljsononj+"]}"
            #fobj = "{'name': 'MAP",'children'+ ": ["+finaljsononj+"]}"
           # print(fobj)
      #  jsresult=objk.replace("'name'", "\"name\"")
       # jsresult=jsresult.replace("'size'", "\"size\"")
        #jsresult=jsresult.replace("'children'", "\"children\"")
    print(objk)
    print("########### JSON DATA #######################")
    return HttpResponse(objk, content_type="application/json")

