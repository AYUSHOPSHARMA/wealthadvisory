# -*- coding: utf-8 -*-

import portfoliooptimization.wealthmanagementreport as wealthmanagementreport
import os
from batchprocessing.models import portfolio
import datetime as dt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root_path = BASE_DIR+"/static/Portfolio_Tracker"

if not os.path.exists(root_path + '/Reports'):
    os.mkdir(root_path + '/Reports')
end_date = dt.date.today()


class report():
   
    def generateReport(poobj):
        print("###########INSIDE generateReport #########")
        filename = root_path + '/Reports/'+poobj.Portfolio_Name+'_ Daily_Report_' + str(end_date) + '.pdf'
        print(filename)
        reportObj= wealthmanagementreport.rep(fname=filename,fund_name="Wealth Advisory",portfolioobj=poobj,logo_path=0)
        reportObj.cover()
        print("###########Company#########")
        print(poobj.Company_Type)
        reportObj.perf(poobj)
        reportObj.diversification(poobj)
        reportObj.mets(poobj)
        reportObj.savePDF()