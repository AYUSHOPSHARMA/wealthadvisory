from django.db import models
from mongoengine import *
from django.contrib.admin.widgets import AdminDateWidget
from batchprocessing.models import mutualfund_company as mfc

connect('wealth_management_indices')

class mutualfund_company_schema(models.Model):
        COMPANY_CHOICES = (
                ('Aditya Birla Sun Life Mutual Fund','Aditya Birla Sun Life Mutual Fund'),
                ('ICICI Prudential Mutual Fund', 'ICICI Prudential Mutual Fund'),
                ('Reliance Mutual Fund','Reliance Mutual Fund'),
                ('Baroda Pioneer Mutual Fund','Baroda Pioneer Mutual Fund'),
                ('HDFC Mutual Fund','HDFC Mutual Fund'),
        )
        SCHEMA_CHOICES = (
                ('',''),
        )

        Company_Name= models.CharField(max_length=100,choices= COMPANY_CHOICES)
        Scheme_Name= models.CharField(max_length=100,choices= SCHEMA_CHOICES)


class mutualfund_schema(models.Model):
    Schema_Code=models.CharField(max_length=100) 
    Scheme_Name= models.CharField(max_length=100)       