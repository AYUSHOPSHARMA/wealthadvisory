import pandas as pd
import os
import datetime as dt
import numpy as np
import portfoliooptimization.plots as plots
#Reportlab dependencies
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import *
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch
import portfoliooptimization.performance as performance
from dateutil.relativedelta import relativedelta
import portfoliooptimization.exposure as exposure
import portfoliooptimization.metrics as metrics
import matplotlib.pyplot as plt

#RF Syntax: 6 MO, 2 YR etc.
rate = '1 YR'
#CUR, AVG
method = "AVG"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

#Create Reports Folder
if not os.path.exists(root_path + '/Reports'):
    os.mkdir(root_path + '/Reports')

end_date = dt.date.today()

class rep():

    def __init__(self, fname, fund_name,portfolioobj, logo_path=0):
        self.width, self.height = landscape(letter)
        self.logo_path = logo_path
        self.c = canvas.Canvas(fname)
        self.fund_name = fund_name
        self.portfolioobj = portfolioobj

    def cover(self):
        fund_name = self.fund_name
        c = self.c
        logo = self.logo_path
        c.setPageSize(landscape(letter))

        #Title
        c.setFontSize(size=24) #choose your font type and font size
        c.setFillColor(aColor=colors.black)
        c.drawString(x=72,y=420,text=fund_name)

        #Subtitle
        c.setFontSize(size=18)  # choose your font type and font size
        c.setFillColor(aColor=colors.cadetblue)
        c.drawString(x=72, y=395, text="Portfolio Daily Report: " + str(end_date))

        #Draw Company Logo
        #if self.logo_path != 0:
           # c.drawImage(logo, x=250, y=500)

        #Line
        c.setFillColor(colors.cadetblue)
        c.rect(x=0, y=385, height="3", width="842", stroke=0, fill=1)

        #Move to next page
        c.showPage()
    
    
    def perf(self,poobj):
        c = self.c
        logo = self.logo_path
        portobj= poobj
        print("###########PERFORMANCE Company Type#########")
        print(portobj.Company_Type)
        #Get Data from module
        port_rets, bench_rets = performance.portfolio(portobj)
        port_rets= port_rets.sort_index(axis=0,ascending=True)
        bench_rets= bench_rets.sort_index(axis=0,ascending=True)
        print("############# port_rets ######")
        print(port_rets) 
        print("############# bench_rets ######")
        print(bench_rets) 
        #Header
        c.setFontSize(size=18)
        c.setFillColor(aColor=colors.cadetblue)
        c.drawString(x=72, y=505, text="Performance")
        c.setFillColor(colors.cadetblue)
        c.rect(x=0, y=500, height="3", width="842", stroke=0, fill=1)

        if self.logo_path != 0:
            c.drawImage(logo,x=250, y=505)

        #Draw price chart
        c.drawImage(root_path + '/Figures/'+portobj.Portfolio_Name+'_port_perf.png',x=50, y=50,width=400,height=400,preserveAspectRatio=1)

        #Draw periodic returns table
        dates = ['2018-01-02']
        pperf =  "{0:.2f}%".format(float(port_rets.iloc[-1:, -1]) * 100)
        bperf = "{0:.2f}%".format(float(bench_rets.iloc[-1:, -1]) * 100)

        port_val = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portobj.Portfolio_Name+'_Portfolio_Value.csv',index_col=0)
        bench_data = pd.read_csv(root_path+'/Daily_Data/Benchmark/Benchmark_Price_Data.csv' ,index_col=0)
        bench_data = bench_data.iloc[::-1]
        bench_data= bench_data.sort_index(axis=0,ascending=True)
        port_val = port_val['Portfolio Value']
        port_val.index = pd.to_datetime(port_val.index)
        bench_data.index = pd.to_datetime(bench_data.index)
        print("########port_val###########3")
        print(port_val)      
        praw = "{0:.2f}%".format((port_val.iloc[-1] / port_val.iloc[0] - 1) * 100)
        pytd = "{0:.2f}%".format((port_val.iloc[-1] / float(port_val[port_val.index.isin(dates)]) - 1) * 100)
        braw = "{0:.2f}%".format((float(bench_data.iloc[-1]) / float(bench_data.iloc[0]) - 1) * 100)
        bytd = "{0:.2f}%".format((float(bench_data.iloc[-1]) / float(bench_data[bench_data.index.isin(dates)].iloc[0]) - 1) * 100)

        prets = []
        brets = []
        nums = [1,3,6,12]
        start_date = dt.date(2017,1,3)
        for x in nums:
            month_add = start_date + relativedelta(months=+x)
            pret = port_val.iloc[port_val.index.get_loc(month_add, method='nearest')]/port_val.iloc[0] - 1
            prets.append("{0:.2f}%".format(pret * 100))
            bret = float(bench_data.iloc[bench_data.index.get_loc(month_add, method='nearest')]) / float(bench_data.iloc[0]) - 1
            brets.append("{0:.2f}%".format(bret * 100))
        print(brets)
        #Labels for Asset Returns
        c.setFontSize(size=12)
        c.setFillColor(aColor=colors.black)
        c.drawString(x=500, y=400, text="Total Return Asset")
        c.drawString(x=625, y=400, text="1 Day Return Asset")

        #Data for table
        data = [['',"YTD","Today's Performance", "1 Month Change", "3 Month Change","6 Month Change", "1 Year Change", "Total Raw Return"],
                ['Portfolio',pytd,pperf, prets[0],prets[1],prets[2],prets[3],praw],
                ['Benchmark',bytd,bperf,brets[0],brets[1],brets[2],brets[3],braw]]

        #Create table with styles
        t1 = Table(data)

        t1.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                               ('BACKGROUND', (0, 0), (0, 0), colors.black),
                                ('ALIGN', (1, 1), (-1, -1), 'CENTER')]))

        #Draw on Canvas
        t1.wrapOn(self.c, self.width, self.height)
        t1.drawOn(c, x=72, y=440)


        #Draw asset Perfomance Tables
        df = performance.asset_performance(portobj)
        df = pd.DataFrame(df)
        df.reset_index(level=0, inplace=True)
        df.columns = ["Symbol", "Return"]

        if len(df) > 21:
            df = df[:21]

        df = df.sort_values(['Return'], ascending=False)
        df['Return'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df['Return']], index=df.index)

        data = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()
        t = Table(data)

        data_len = len(data)

        x = 390

        #Need to do for alternating colors
        for each in range(data_len):

            x -= .25 * inch

            if each % 2 == 0:
                bg_color = colors.cadetblue
            else:
                bg_color = colors.white

            t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.black),
                               ('BACKGROUND', (1, 0), (1, 0), colors.black),
                               ('TEXTCOLOR',(0,0),(0, 0),colors.white),
                               ('LINEBELOW', (0, -1), (-1, -1), 1.5, colors.black),
                               ('TEXTCOLOR', (1, 0), (1, 0), colors.white)
                               ]))

        t.wrapOn(self.c, self.width, self.height)
        t.drawOn(c, x=500, y=x)

        df = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+portobj.Portfolio_Name+'_Portfolio_Returns.csv' )
        data = df.iloc[-1,1:len(df.columns)-1]
        df = pd.DataFrame(data)

        if len(df) > 21:
            df = df[:21]

        df.reset_index(level=0, inplace=True)
        df.columns = ["Symbol", "Return"]
        df = df.sort_values(by='Return',ascending=False)
        df['Return'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df['Return']], index=df.index)
        data = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()

        t = Table(data)

        data_len = len(data)

        x = 390
        #Need to do for alternating colors
        for each in range(data_len):

            x -= .25 * inch

            if each % 2 == 0:
                bg_color = colors.cadetblue
            else:
                bg_color = colors.white

            t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (0, 0), colors.black),
                               ('BACKGROUND', (1, 0), (1, 0), colors.black),
                               ('TEXTCOLOR',(0,0),(0, 0),colors.white),
                               ('LINEBELOW', (0, -1), (-1, -1), 1.5, colors.black),
                               ('TEXTCOLOR', (1, 0), (1, 0), colors.white)
                               ]))

        t.wrapOn(self.c, self.width, self.height)
        t.drawOn(c, x=635, y=x)

        c.showPage()
    def exposurePieChart(self,poobj):
        c = self.c
        exposure.info(poobj)
        c.drawImage(root_path + '/Figures/'+poobj.Portfolio_Name+'_ind_pie.png',x=372, y=200,width=250,height=350,preserveAspectRatio=1)
        c.showPage()
        
    def diversification(self,poobj):
        c = self.c
        logo = self.logo_path

        #Header
        c.setFontSize(size=18)  # choose your font type and font size
        c.setFillColor(aColor=colors.cadetblue)
        c.drawString(x=72, y=505, text="Diversification")
        c.setFillColor(colors.cadetblue)
        c.rect(x=0, y=500, height="3", width="842", stroke=0, fill=1)

        if self.logo_path != 0:
            c.drawImage(logo,x=250, y=505)

        #Correlation plot
        plots.correl(poobj)
        c.drawImage(root_path + '/Figures/'+poobj.Portfolio_Name+'_port_correl.png',x=72, y=200,width=250,height=350,preserveAspectRatio=1)

        #Get exposure plots/data
        exposure.info(poobj)

        #Draw Sector Table
        df = pd.read_csv(root_path+'/Daily_Data/Portfolio/'+poobj.Portfolio_Name+'_Industrial_Weights.csv')
        
        if len(df) > 22:
            df = df[:22]

        df.columns = ["Industry", "Weight"]
        df['Weight'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df['Weight']], index=df.index)

        data = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()
        t = Table(data)
        t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
        data_len = len(data)

        #Start position on canvas
        x = 280
        for each in range(data_len):
            x -= .25 * inch
            if each % 2 == 0:
                bg_color = colors.cadetblue
            else:
                bg_color = colors.white

            t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.black),
                               ('TEXTCOLOR',(0,0),(-1, 0),colors.white),
                               ('ALIGN', (0, 0), (-1, 0), 'CENTER')]))

        #draw table
        t.wrapOn(self.c, self.width, self.height)
        t.drawOn(c, x=72, y=x)
        #c.drawImage(root_path + '/Figures/'+poobj.Portfolio_Name+'_ind_weight.png',x=72, y=200,width=250,height=350,preserveAspectRatio=1)
        
        plt.table(cellText=data,
                      rowColours=None,
                      colLabels=None,
                      loc='bottom')
        
        figure=plt.gcf()
        figure.savefig(root_path + '/Figures/'+poobj.Portfolio_Name+'_ind_weight.png')
        #Draw industry table
        #df = pd.read_csv(root_path+'/Daily Data/Portfolio/Asset Exposure.csv',index_col=0)
        #df.reset_index(level=0, inplace=True)
        #df.columns = ["Symbol", "Sector", "Industry"]
        #data = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()

        #t = Table(data)
        #t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.25, colors.black),
#                               ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)]))
        #data_len = len(data)

        #Start position on canvas
        #x = 440
        #for each in range(data_len):
        #   x -= .25 * inch
        #    if each % 2 == 0:
        #        bg_color = colors.cadetblue
        #    else:
        #        bg_color = colors.white

#            t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

 #       t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.black),
  #                             ('TEXTCOLOR',(0,0),(-1, 0),colors.white),
   #                            ('ALIGN', (0, 0), (-1, 0), 'CENTER')]))

        #draw table
    #    t.wrapOn(self.c, self.width, self.height)
     #   t.drawOn(c, x=360, y=x)
     
    def mets(self,portfolioobj):
        c = self.c
        logo = self.logo_path

        #Header
        c.setFontSize(size=18)  # choose your font type and font size
        c.setFillColor(aColor=colors.cadetblue)
        c.drawString(x=72, y=505, text="Metrics")
        c.setFillColor(colors.cadetblue)
        c.rect(x=0, y=500, height="3", width="842", stroke=0, fill=1)

        if self.logo_path != 0:
            c.drawImage(logo,x=250, y=505)

        c.setFontSize(size=12)  # choose your font type and font size
        c.setFillColor(aColor=colors.black)
        c.drawString(x=425, y=475, text="Risk-Adjusted Metrics")

        c.setFontSize(size=12)  # choose your font type and font size
        c.setFillColor(aColor=colors.black)
        c.drawString(72, 475, text="Weighted Fundamental Metrics")

        data = metrics.fundis(rate=rate,method=method,portfolioobj=portfolioobj)

        t = Table(data)
        t.setStyle(TableStyle([('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                               ('BACKGROUND', (0, 0), (-1, 0), colors.black),
                               ('LINEBELOW', (0, -1), (-1, -1), 1.5, colors.black),
                               ('BACKGROUND', (0, 1), (-1, 1), colors.cadetblue),
                               ('ALIGN', (1, 1), (-1, -1), 'CENTER')]))

        #draw table
        t.wrapOn(self.c, self.width, self.height)
        t.drawOn(c, x=425, y=400)

        #Load data
        df = pd.read_csv(root_path + '/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Portfolio_Fundis.csv',header=None)
        df.columns = ["Metric", "Weighted Sum"]

        #String formatting
        for i, trial in df.iterrows():
            if i == 5:
                df.loc[i, "Weighted Sum"] = "{0:.2f}%".format(df.iloc[i,1] * 100)
            else:
                df.loc[i, "Weighted Sum"] = "{0:.2f}".format(df.iloc[i, 1])

        #Convert to format for reportlab
        data = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()

        t = Table(data)
        t.setStyle(TableStyle([
                                ('TEXTCOLOR',(0,0),(1, 0),colors.white),
                                ('BACKGROUND', (0, 0), (1, 0), colors.black),
                               ('BACKGROUND', (0, 1), (1, 1), colors.cadetblue),
                               ('BACKGROUND', (0, 3), (1, 3), colors.cadetblue),
                                ('BACKGROUND', (0, 5), (1, 5), colors.cadetblue),
                                ('LINEBELOW', (0, -1), (1, -1), 1.5, colors.black),
                               ('ALIGN', (1, 1), (-1, -1), 'CENTER')]))

        #draw table
        t.wrapOn(self.c, self.width, self.height)
        t.drawOn(c, x=72, y=335)

        df = pd.read_csv(root_path + '/Daily_Data/Portfolio/'+portfolioobj.Portfolio_Name+'_Asset_Fundis.csv')

        if len(df) > 15:
            df = df[:15]

        df['Dividend Yield'] = pd.Series(["{0:.2f}%".format(val * 100) for val in df['Dividend Yield']], index=df.index)
        df.columns = ['Symbol','Trailing P/E', 'Forward P/E', 'PEG', 'Price/Book', 'Beta', 'Dividend Yield']

        data = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()

        c.setFontSize(size=12)  # choose your font type and font size
        c.setFillColor(aColor=colors.black)
        c.drawString(72, 315, text="Asset Fundamental Metrics")

        t = Table(data)

        data_len = len(data)

        x = 300

        #Need to loop for alternating colors
        for each in range(data_len):
            x -= .25 * inch
            if each % 2 == 0:
                bg_color = colors.white
            else:
                bg_color = colors.cadetblue

            t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

        t.setStyle(TableStyle([('TEXTCOLOR',(0,0),(-1, 0),colors.white),
                                ('BACKGROUND', (0, 0), (-1, 0), colors.black),
                               ('LINEBELOW', (0, -1), (-1, -1), 1.5, colors.black),
                               ('ALIGN', (1, 1), (-1, -1), 'CENTER')]))

        t.wrapOn(self.c, self.width, self.height)
        t.drawOn(c, x=72, y=x)
        c.showPage()
 

    def savePDF(self):
        self.c.save()