# -*- coding: utf-8 -*-
from django.shortcuts import render
import screener.portfoliooptimization as po
from django.http import HttpResponse
import datetime
import pdfkit , os
from django.views.decorators.cache import cache_page
from mpld3._display import display_d3,fig_to_html,save_json
import io
import portfoliooptimization.dataportfolio as dataportfolio

def getportfolio(request):
    stocks = ['AAPL','AMZN','MSFT','ACC']
    end = datetime.date(2018,5,27)
    begin = datetime.date(2017,1,1)
    allocations = [10,10]
    	#timestamp format and get apple stock.
    
    st=begin.strftime('%Y-%m-%d')
    
    ed=end.strftime('%Y-%m-%d')
    
    #set number of runs of random portfolio weights
    num_portfolios = 25000
    result_HTML=fig_to_html(po.portfolioOptimization(stocks,st,ed,num_portfolios))
    result_corr_HTML = fig_to_html(dataportfolio.correlData(stocks,allocations,begin))
    result_riskreturn_HTML = fig_to_html(dataportfolio.risk_return(stocks,allocations,begin))
    result_violin_HTML = fig_to_html(dataportfolio.violin(stocks,allocations,begin))
    result_violin_HTML = fig_to_html(dataportfolio.benchmark(begin))
    
    return render(request,"portfolio.html",{"data":result_HTML,"result_corr_HTML":result_corr_HTML,"result_riskreturn_HTML":result_riskreturn_HTML,"result_violin_HTML":result_violin_HTML})

def getportfolioPDF(request):
    return render(request,"portfolioPDF.html")

def getPortfolioChart(request):
    stocks = ['AAPL','AMZN','MSFT','ACC']
    end = datetime.date(2018,5,27)
    begin = datetime.date(2017,1,1)
    
    	#timestamp format and get apple stock.
    
    st=begin.strftime('%Y-%m-%d')
    
    ed=end.strftime('%Y-%m-%d')
    byte_file = io.BytesIO()
    #set number of runs of random portfolio weights
    num_portfolios = 25000
    result_image=po.portfolioOptimization(stocks,st,ed,num_portfolios)
    result_image.savefig(byte_file, format='png')
    image_file= byte_file.getvalue()
    return HttpResponse(image_file, content_type="image/png")


def downloadPortfolioPDF(request):
    filename = "portfolio.pdf"
    print("###################downloadPortfolioPDF#################")
    path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    #urlhtml="C:\\wealthmanagement_data\\html\\Wealth_View.html"
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_url("http://127.0.0.1:7000/screener/portfolioPDF/", filename, configuration=config)
    print("###################PDF#################")
    pdfDownload = open(filename, 'rb').read()
    #os.remove(filename)
    response = HttpResponse(pdfDownload , content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="portfolio.pdf"'
    return response