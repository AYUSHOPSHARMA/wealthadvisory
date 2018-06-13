from django.db import models
from mongoengine import *
from batchprocessing.models import nifty_500_companies
from django.contrib.admin.widgets import AdminDateWidget

connect('wealth_management_indices')

class strategy(models.Model):
    COMPANY_CHOICES = (
            nifty_500_companies.objects.all().values_list('Symbol','Company_Name')
    )
    
    companyName= models.CharField(max_length=100,choices= COMPANY_CHOICES)
    backdate=models.DateField()
    