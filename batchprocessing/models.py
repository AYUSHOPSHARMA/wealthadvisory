from django.db import models

# Create your models here.


from mongoengine import *
import datetime
 
connect('wealth_management_indices')

class nifty_500_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)